#!/usr/bin/env node
/**
 * Zero-dependency Node.js CLI wrapper for Product Design Intelligence (PDI).
 * Supports: npx pdi-skills, pnpm dlx pdi-skills, bunx pdi-skills, or global npm/Homebrew install.
 */
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
const rootDir = path.resolve(__dirname, '..');
const installScript = path.join(rootDir, 'scripts', 'install_pdi.py');
const auditScript = path.join(rootDir, 'scripts', 'audit_artifact.py');
const manifestScript = path.join(rootDir, 'scripts', 'build_manifest.py');

function runPython(scriptPath, scriptArgs) {
  const pyCandidates = ['python3', 'python'];
  for (const cmd of pyCandidates) {
    const check = spawnSync(cmd, ['--version'], { stdio: 'ignore' });
    if (check.status === 0) {
      const res = spawnSync(cmd, [scriptPath, ...scriptArgs], { stdio: 'inherit' });
      process.exit(res.status ?? 0);
    }
  }
  console.error('Error: Python 3 is required to run PDI scripts.');
  process.exit(1);
}

if (args[0] === 'audit') {
  runPython(auditScript, args.slice(1));
} else if (args[0] === 'build-manifest') {
  runPython(manifestScript, args.slice(1));
} else if (args[0] === 'install') {
  runPython(installScript, args.slice(1));
} else {
  // Default to install_pdi.py so `npx pdi-skills /path/to/project --hosts all` works directly
  runPython(installScript, args);
}
