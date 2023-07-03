#!/usr/bin/env bash
set -e 
pushd . > /dev/null
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR" 
export REDIS_PASSWORD=test
export REDIS_URL=redis://:$REDIS_PASSWORD@localhost:6379
./main.py
popd > /dev/null