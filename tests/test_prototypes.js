const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.join(__dirname, '..');
function script(file) {
  const html = fs.readFileSync(path.join(root, file), 'utf8');
  return html.match(/<script>([\s\S]*?)<\/script>/)[1];
}
{
  const listeners = {};
  const nodes = Object.fromEntries(['#status', '#settings'].map(id => [id, {textContent: '', addEventListener: (name, fn) => {listeners[name] = fn;}}]));
  const document = {querySelector: id => nodes[id]};
  class FormData { get(key) { return {email:'Off', density:'Compact'}[key]; } }
  vm.runInNewContext(script('examples/audit-scenarios/settings.html'), {document, FormData});
  listeners.submit({preventDefault() {}, currentTarget: {}});
  assert.match(nodes['#status'].textContent, /off.*compact/i);
  assert.ok(listeners.change, 'changing a setting should clear outdated feedback');
  listeners.change();
  assert.equal(nodes['#status'].textContent, '');
}
{
  const nodes = Object.fromEntries(['active','review','checkins','insight-count','update','account-count'].map(id => [id, {textContent:''}]));
  const weekly = Array.from({length:4}, () => ({cells:[{}, {}, {}]}));
  const accounts = Array.from({length:2}, () => ({cells:[{}, {}, {}]}));
  const bars = Array.from({length:4}, () => ({children:[{style:{}},{style:{}}]}));
  let change;
  const document = {
    getElementById: id => nodes[id],
    querySelector: id => id === '#period' ? {addEventListener: (_, fn) => {change = fn;}} : nodes[id.slice(1)],
    querySelectorAll: id => ({'#weekly tr':weekly,'#accounts tr':accounts,'.bar-group':bars})[id]
  };
  vm.runInNewContext(script('examples/analytics-dashboard/index.html'), {document});
  assert.equal(nodes['account-count'].textContent, 'Showing 2 of 12 accounts');
  change({target:{value:'previous'}});
  assert.equal(nodes.active.textContent, 76);
  assert.equal(nodes.review.textContent, 9);
  assert.equal(nodes['account-count'].textContent, 'Showing 2 of 9 accounts');
  assert.equal(nodes.checkins.textContent, 29);
  assert.equal(weekly[0].cells[1].textContent, 38);
  assert.equal(accounts[0].cells[0].textContent, 'Cedar Works');
  assert.match(nodes.update.textContent, /previous 30 days/);
}
console.log('Prototype state checks passed');
