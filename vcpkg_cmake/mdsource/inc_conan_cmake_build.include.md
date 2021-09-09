

```bash
#!/bin/bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

mkdir -p build
cd       build
conan install ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest --output-on-failure . -C Debug
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./conan_cmake/build.sh' title='File snippet was copied from'>snippet source</a></sup>

