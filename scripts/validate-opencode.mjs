#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const errors = [];
const warnings = [];
const skillCatalogDescriptionLimit = 900_000;

function rel(file) {
  return path.relative(root, file).replaceAll(path.sep, '/');
}

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function walk(dir, predicate, out = []) {
  if (!fs.existsSync(dir)) return out;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git' || entry.name === 'node_modules') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, out);
    else if (!predicate || predicate(full)) out.push(full);
  }
  return out;
}

function splitFrontmatter(file) {
  const text = read(file);
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!match) {
    errors.push(`${rel(file)}: missing YAML frontmatter`);
    return null;
  }
  return match[1];
}

function field(frontmatter, key) {
  const match = frontmatter.match(new RegExp(`^${key}\\s*:\\s*(.*)$`, 'm'));
  return match ? match[1].trim().replace(/^['"]|['"]$/g, '') : '';
}

function checkConfig() {
  const file = path.join(root, 'opencode.json');
  if (!fs.existsSync(file)) {
    errors.push('opencode.json: missing');
    return;
  }
  let config;
  try {
    config = JSON.parse(read(file));
  } catch (err) {
    errors.push(`opencode.json: invalid JSON: ${err.message}`);
    return;
  }
  if (config.$schema !== 'https://opencode.ai/config.json') errors.push('opencode.json: missing opencode schema URL');
  for (const required of ['AGENTS.md', 'references/zitierweise.md', 'references/methodik-buergerliches-recht.md']) {
    if (!config.instructions?.includes(required)) errors.push(`opencode.json: instructions missing ${required}`);
  }
  if (!config.skills?.paths?.includes('.opencode/skills')) errors.push('opencode.json: skills.paths missing .opencode/skills');
  for (const [name, server] of Object.entries(config.mcp || {})) {
    if (!/^[a-z0-9-]+$/.test(name)) errors.push(`opencode.json: invalid MCP name ${name}`);
    if (server.type !== 'remote') errors.push(`opencode.json: MCP ${name} must use type remote`);
    if (typeof server.url !== 'string' || !server.url.startsWith('https://')) errors.push(`opencode.json: MCP ${name} must use HTTPS url`);
    if (server.enabled !== false) warnings.push(`opencode.json: MCP ${name} is enabled; check confidentiality and provider approval`);
  }
}

function checkGeneratedSkills() {
  const dir = path.join(root, '.opencode', 'skills');
  if (!fs.existsSync(path.join(dir, '.generated'))) errors.push('.opencode/skills: missing generated marker');
  const seen = new Set();
  const skills = walk(dir, (file) => path.basename(file) === 'SKILL.md');
  let catalogChars = 0;
  if (skills.length === 0) errors.push('.opencode/skills: no generated skills found');
  for (const skill of skills) {
    const fm = splitFrontmatter(skill);
    if (!fm) continue;
    const name = field(fm, 'name');
    const description = field(fm, 'description');
    if (!/^[a-z0-9-]{1,64}$/.test(name)) errors.push(`${rel(skill)}: invalid opencode skill name ${name}`);
    if (path.basename(path.dirname(skill)) !== name) errors.push(`${rel(skill)}: folder name does not match frontmatter name`);
    if (seen.has(name)) errors.push(`${rel(skill)}: duplicate opencode skill name ${name}`);
    seen.add(name);
    if (!description) errors.push(`${rel(skill)}: missing description`);
    catalogChars += `${name}: ${description}\n`.length;
    for (const line of fm.split(/\r?\n/)) {
      const match = line.match(/^([A-Za-z][\w-]*)\s*:/);
      if (match && !['name', 'description'].includes(match[1])) errors.push(`${rel(skill)}: unsupported skill frontmatter field ${match[1]}`);
    }
  }
  if (catalogChars > skillCatalogDescriptionLimit) {
    errors.push(`.opencode/skills: generated skill name/description catalog is ${catalogChars} chars, above safe limit ${skillCatalogDescriptionLimit}; use plugin router skills instead of per-source-skill copies`);
  }
}

function checkGeneratedAgents() {
  const dir = path.join(root, '.opencode', 'agent');
  if (!fs.existsSync(path.join(dir, '.generated'))) errors.push('.opencode/agent: missing generated marker');
  for (const agent of walk(dir, (file) => file.endsWith('.md'))) {
    const fm = splitFrontmatter(agent);
    if (!fm) continue;
    const name = field(fm, 'name') || path.basename(agent, '.md');
    if (!/^[a-z0-9-]{1,64}$/.test(name)) errors.push(`${rel(agent)}: invalid agent name ${name}`);
    if (field(fm, 'mode') !== 'subagent') errors.push(`${rel(agent)}: generated agents must use mode: subagent`);
    if (/^tools\s*:/m.test(fm)) errors.push(`${rel(agent)}: generated opencode agent must not carry Claude tools frontmatter`);
    const model = field(fm, 'model');
    if (model && !model.includes('/')) errors.push(`${rel(agent)}: model must be provider-prefixed or omitted`);
  }
}

function checkOpencodeLoadsConfig() {
  const env = { ...process.env, OPENCODE_DISABLE_DEFAULT_PLUGINS: '1' };
  for (const key of [
    'OPENCODE_DISABLE_PROJECT_CONFIG',
    'OPENCODE_CONFIG_CONTENT',
    'OPENCODE_CONFIG_DIR',
  ]) {
    delete env[key];
  }
  const result = spawnSync('opencode', ['--pure', 'debug', 'config'], {
    cwd: root,
    encoding: 'utf8',
    env,
  });
  if (result.error?.code === 'ENOENT') {
    warnings.push('opencode executable not found; skipped opencode debug config');
    return;
  }
  if (result.status !== 0) {
    errors.push(`opencode debug config failed:\n${result.stderr || result.stdout}`.trim());
  } else if (!result.stdout.includes('AGENTS.md') || !result.stdout.includes('arbeitsrecht-fehlzeiten-register')) {
    errors.push('opencode debug config did not include project AGENTS.md or generated agents; project config may not be loading');
  }
}

checkConfig();
checkGeneratedSkills();
checkGeneratedAgents();
checkOpencodeLoadsConfig();

console.log(`validate-opencode: ${errors.length} Fehler, ${warnings.length} Warnungen`);
for (const warning of warnings) console.log(`  WARN: ${warning}`);
if (errors.length) {
  for (const error of errors) console.error(`  FEHLER: ${error}`);
  process.exit(1);
}
console.log('OK');
