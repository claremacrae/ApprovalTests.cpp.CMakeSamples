# vcpkg_cmake

include: vcpkg_cmake

The vcpkg.json manifest file, which states dependencies, is:

include: inc_vcpkg_cmake_vcpkg

The top-level CMakeLists.txt file, which clones and builds vcpkg, is:

include: inc_vcpkg_cmake_cmakelists

And the CMakeLists.txt that builds the tests is:

include: inc_vcpkg_cmake_tests_cmakelists

The build script - which notably contains no vcpkg-specific commands - is:

include: inc_vcpkg_cmake_build
