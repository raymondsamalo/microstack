#!/usr/bin/env bash
set -e 
pushd . > /dev/null
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR" 
huey_consumer app.worker.huey "$@"
popd > /dev/null