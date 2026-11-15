#!/usr/bin/env python3
"""Create an independent local copy of the onboarding prototype."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path, help='new HTML file; parent directory must exist')
args = parser.parse_args()
source = Path(__file__).resolve().parents[1] / 'examples/onboarding/index.html'
try:
    data = source.read_bytes()
    with args.output.open('xb') as output:
        output.write(data)
except OSError as error:
    parser.exit(1, f'Could not create {args.output}: {error}\n')
print(f'Created {args.output}')
