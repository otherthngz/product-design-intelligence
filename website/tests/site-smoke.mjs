import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import test from 'node:test';

const base = process.env.PDI_SITE_URL ?? 'http://localhost:3000';

async function read(path) {
  const response = await fetch(new URL(path, base));
  assert.equal(response.status, 200, path);
  return response.text();
}

test('visitors can navigate from home to the documentation and changelog', async () => {
  const home = await read('/');
  assert.match(home, /Give your AI assistant a better way to approach product design/);
  for (const href of ['/#how-it-works', '/docs/installation', '/docs', '/changelog']) {
    assert.ok(home.includes(`href="${href}"`), `missing navigation to ${href}`);
  }
  for (const path of ['/docs', '/docs/first-task', '/docs/guides/skills', '/docs/guides/agents', '/docs/guides/modes', '/docs/reference/installer-options', '/docs/reference/troubleshooting', '/docs/reference/limitations', '/changelog']) {
    await read(path);
  }
});

test('installation guidance identifies the local prerequisite and selected host', async () => {
  const guide = await read('/docs/installation.md');
  assert.match(guide, /public installation source is not available yet/i);
  assert.match(guide, /--hosts agents --standalone-skills/);
  assert.match(guide, /installer skips existing files and folders/i);
  assert.doesNotMatch(guide, /github:otherthngz\/pdi/);
});

test('agent discovery describes PDI and points to the matching skill', async () => {
  const index = JSON.parse(await read('/.well-known/agent-skills/index.json'));
  const skill = index.skills.find(item => item.name === 'pdi');
  assert.ok(skill);
  const body = await read('/.well-known/agent-skills/site-skill.md');
  assert.equal(skill.digest, `sha256:${createHash('sha256').update(body).digest('hex')}`);
  assert.match(body, /Public installation is not available yet/);
});
