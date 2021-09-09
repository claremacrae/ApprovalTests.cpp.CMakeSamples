

```cmake
cmake_minimum_required(VERSION 3.8 FATAL_ERROR)

project(dev_approvals)

enable_testing()

set(CMAKE_VERBOSE_MAKEFILE off)

# Prevent ctest creating cluttering up CLion with nearly 30 CTest targets
# (Continuous, ContinuousBuild etc) when it does:
#   include(CTest)
# This hack taken from https://stackoverflow.com/a/57240389/104370
set_property(GLOBAL PROPERTY CTEST_TARGETS_ADDED 1) # hack to prevent CTest added targets

# -------------------------------------------------------------------
# boost
# This will be used by find_package() in ApprovalTests.cpp/tests/Boost_Tests
# If there is a local boost directory, use tat.
# Otherwise, require the user to have installed boost (as is done in CI builds)
if (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../boost)
    set(BOOST_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/../boost)
endif()

# -------------------------------------------------------------------
# Catch2
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
add_subdirectory(
        ../Catch2
        ${CMAKE_CURRENT_BINARY_DIR}/catch2_build
)

# -------------------------------------------------------------------
# CppUTest

# Prevent CppUTest's own tests from being built
set(TESTS OFF CACHE BOOL "")

# Prevent build of CppUTest from generating thousands of lines of
# -Wc++98-compat and -Wc++98-compat-pedantic warnings:
set(C++11 ON CACHE BOOL "Compile with C++11 support")

add_subdirectory(
        ../cpputest
        ${CMAKE_CURRENT_BINARY_DIR}/cpputest_build
)

# -------------------------------------------------------------------
# doctest
add_subdirectory(
        ../doctest
        ${CMAKE_CURRENT_BINARY_DIR}/doctest_build
)

# -------------------------------------------------------------------
# filesystem
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
add_subdirectory(
        ../filesystem
        ${CMAKE_CURRENT_BINARY_DIR}/filesystem_build
)

# -------------------------------------------------------------------
# fmt
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
add_subdirectory(
        ../fmt
        ${CMAKE_CURRENT_BINARY_DIR}/fmt_build
)

# -------------------------------------------------------------------
# GoogleTest
# Prevent GoogleTest from overriding our compiler/linker options
# when building with Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" )
add_subdirectory(
        ../googletest
        ${CMAKE_CURRENT_BINARY_DIR}/googletest_build
)

# -------------------------------------------------------------------
# Boost.ut
set(BUILD_BENCHMARKS OFF CACHE BOOL "")
set(BUILD_EXAMPLES OFF CACHE BOOL "")
set(BUILD_TESTS OFF CACHE BOOL "")

add_subdirectory(
        ../ut
        ${CMAKE_CURRENT_BINARY_DIR}/ut_build
)

if(TARGET Boost::ut)
    add_library(boost.ut ALIAS ut)
endif()

if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
    # Turn off some checks off for boost.ut
    target_compile_options(ut INTERFACE
            -Wno-c99-extensions # Needed for Boost.ut, at least in v1.1.6
            -Wno-documentation-unknown-command # unknown command tag name \userguide
            -Wno-weak-vtables
            -Wno-comma # See https://github.com/boost-ext/ut/issues/398
            )
endif()

# -------------------------------------------------------------------
# ApprovalTests.cpp

set(APPROVAL_TESTS_BUILD_TESTING ON CACHE BOOL "")
set(APPROVAL_TESTS_BUILD_EXAMPLES ON CACHE BOOL "")

add_subdirectory(
        ../ApprovalTests.cpp
        ${CMAKE_CURRENT_BINARY_DIR}/approvaltests.cpp_build
)
```
<sup><a href='https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/blob/main/./dev_approvals/CMakeLists.txt' title='File snippet was copied from'>snippet source</a></sup>

