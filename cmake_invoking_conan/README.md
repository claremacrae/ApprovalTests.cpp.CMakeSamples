<!--
GENERATED FILE - DO NOT EDIT
This file was generated by [MarkdownSnippets](https://github.com/SimonCropp/MarkdownSnippets).
Source File: /cmake_invoking_conan/mdsource/README.source.md
To change this file edit the source file and then execute ./run_markdown_templates.sh.
-->

# cmake_invoking_conan

 <!-- include: cmake_invoking_conan. path: /cmake_invoking_conan/mdsource/cmake_invoking_conan.include.md -->
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [cmake_invoking_conan](/cmake_invoking_conan/)               |
| Purpose      | Demo how to build your tests by getting CMake to invoke Conan, to download single headers for specific releases of ApprovalTests.cpp and Catch2.<br />The released headers of those dependencies will be downloaded inside your CMake build space, and will not be shown inside your IDE. |
| Dependencies | ApprovalTests.cpp - downloaded automatically by CMake invoking Conan<br/>Catch2 - downloaded automatically by CMake invoking Conan |
| Mechanism    | Uses the [cmake-conan](https://github.com/conan-io/cmake-conan) CMake module to invoke Conan automatically from within CMake. |
| More Detail  | See [Example 3. Making CMake invoke Conan](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/ConanIntegration.md#example-3-making-cmake-invoke-conan) |
 <!-- endInclude -->

The conanfile.txt file is:

 <!-- include: inc_cmake_invoking_conan_conanfile. path: /cmake_invoking_conan/mdsource/inc_cmake_invoking_conan_conanfile.include.md -->

```
# See CMake/Conan.cmake for how 'conan install' is launched from cmake

[requires]
catch2/2.13.4
approvaltests.cpp/10.7.0

# Note that we don't say what generator we want.
# CMake code will take care of that for us.
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/conanfile.txt' title='File snippet was copied from'>snippet source</a></sup>
 <!-- endInclude -->

There is a CMake file called `CMake/Conan.cmake` which contains instructions for downloading a specific version of the cmake-conan CMake module:

 <!-- include: inc_cmake_invoking_conan_CMake_conan. path: /cmake_invoking_conan/mdsource/inc_cmake_invoking_conan_CMake_conan.include.md -->

```cmake
macro(run_conan)
# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
  message(
    STATUS
      "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
  file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.15/conan.cmake"
       "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_add_remote(NAME bincrafters URL
                 https://api.bintray.com/conan/bincrafters/public-conan)

conan_cmake_run(
  CONANFILE conanfile.txt
  BASIC_SETUP
  CMAKE_TARGETS # individual targets to link to
  BUILD
    missing
)
endmacro()
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/CMake/Conan.cmake' title='File snippet was copied from'>snippet source</a></sup>
 <!-- endInclude -->
 
The top-level CMakeLists.txt file includes the above `CMake/Conan.cmake` file, and runs the macro that it contained:

 <!-- include: inc_cmake_invoking_conan_cmakelists. path: /cmake_invoking_conan/mdsource/inc_cmake_invoking_conan_cmakelists.include.md -->

```cmake
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(conan_cmake)

# Load CMake/Conan.cmake, which sets up a 'run_conan()' macro to download dependencies.
include(CMake/Conan.cmake)
run_conan()

enable_testing()

add_subdirectory(tests)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>
 <!-- endInclude -->

And the CMakeLists.txt that builds the tests is:

 <!-- include: inc_cmake_invoking_conan_tests_cmakelists. path: /cmake_invoking_conan/mdsource/inc_cmake_invoking_conan_tests_cmakelists.include.md -->

```cmake
add_executable(tests
        main.cpp
        tests.cpp
)

# Note the Conan-specific library namees, beginning with CONAN_PKG.
# Conan sets up these names when its cmake generator is used.
# This ties your project to using Conan.
target_link_libraries(
        tests
        CONAN_PKG::approvaltests.cpp
        CONAN_PKG::catch2)

target_compile_features(tests PUBLIC cxx_std_11)
set_target_properties(tests PROPERTIES CXX_EXTENSIONS OFF)

add_test(
        NAME tests
        COMMAND tests)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/tests/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>
 <!-- endInclude -->

The build script is:

 <!-- include: inc_cmake_invoking_conan_build. path: /cmake_invoking_conan/mdsource/inc_cmake_invoking_conan_build.include.md -->

```bash
#!/bin/bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

mkdir -p build
cd       build
# Note that we do not need to invoke conan.
# However, we do need to say what build configuration we want.
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .
ctest --output-on-failure . -C Debug
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./cmake_invoking_conan/build.sh' title='File snippet was copied from'>snippet source</a></sup>
 <!-- endInclude -->
