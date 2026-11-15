#!/usr/bin/env sh
# Universal one-line curl/sh installer for Product Design Intelligence (PDI)
# Usage: ./scripts/install.sh [TARGET_DIR] [--hosts all] [--mode solo|team|enterprise] [--standalone-skills]
set -e

SCRIPT_DIR="$(CDPATH= command -v cd >/dev/null 2>&1 && cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

if [ "$#" -eq 0 ]; then
  set -- "." --hosts all --mode solo --standalone-skills
fi

exec python3 "$ROOT_DIR/scripts/install_pdi.py" "$@"
