

```cmake
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Conan's cmake generator creates a conanbuildinfo.cmake file, which we
# need to include, and then use:
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_subdirectory(tests)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./conan_cmake/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

