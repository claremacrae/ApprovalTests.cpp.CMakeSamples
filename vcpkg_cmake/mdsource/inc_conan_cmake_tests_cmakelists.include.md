

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
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./conan_cmake/tests/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

