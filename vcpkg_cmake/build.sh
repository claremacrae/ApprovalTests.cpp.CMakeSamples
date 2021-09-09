#!/bin/bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
srcdir="$scriptdir"
builddir="$scriptdir/build"

cmake -DCMAKE_BUILD_TYPE=Debug -B "$builddir" -S "$srcdir"
cmake --build "$builddir"
ctest --output-on-failure "$builddir" -C Debug
