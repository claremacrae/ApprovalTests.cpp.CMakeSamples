cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

project(dev_approvals_fetch_content)

enable_testing()

set(CMAKE_VERBOSE_MAKEFILE off)

# Prevent ctest creating cluttering up CLion with nearly 30 CTest targets
# (Continuous, ContinuousBuild etc) when it does:
#   include(CTest)
# This hack taken from https://stackoverflow.com/a/57240389/104370
set_property(GLOBAL PROPERTY CTEST_TARGETS_ADDED 1) # hack to prevent CTest added targets

# Needs CMake 3.14 or above
include(FetchContent)

# -------------------------------------------------------------------
# Program Version Numbers - and/or commit IDs

# TODO Update these notes for sunsetting of bintray
# Oldest Boost in dl.bintray.com is 1.63.0
# Tested with versions in range: 1.63.0 ... 1.74.0
# NOTE: With gcc, and Boost 1.73.0, 1.74.0 and 1.75.0, tests in the following directory
#       exit with error code 200:
#           ApprovalTests.cpp.CMakeSamples/ApprovalTests.cpp/tests/Boost_Tests/
#       See https://github.com/claremacrae/ApprovalTests.cpp.CMakeSamples/issues/1
set(BoostVersion
        "1.72.0")

# Tested with versions in range: v2.3.0 ... v2.13.3
# Does not work with devel, and v3 releases
set(Catch2Version
        "v2.x")

# Tested with versions in range: v4.0
set(CppUTestVersion
        "master")

# Tested with versions in range: 2.3.4 ... 2.4.1
set(DocTestVersion
        "master")

# Tested with versions in range: 6.0.0 ... 7.1.2
set(FmtVersion
        "7.1.3")

# Tested with versions in range: release-1.8.0 ... release-1.10.0
set(GoogleTestVersion
        "main")

# Tested with v1.5.4
set(GulrakFileSystemVersion
        "master")

# Tested with versions in range: 1.1.7 ... 1.1.8
set(UtVersion
        "master")

# -------------------------------------------------------------------
# boost
message(NOTICE "Fetching Boost...")
string(REPLACE . _ BoostVersionUnderscored ${BoostVersion})
FetchContent_Declare(
        Boost
        URL https://boostorg.jfrog.io/artifactory/main/release/${BoostVersion}/source/boost_${BoostVersionUnderscored}.tar.gz
)
FetchContent_MakeAvailable(Boost)
# This is needed because there is not a CMakeLists.txt in the Boost download,
# so we have to teach find_package() to find Boost
set(BOOST_ROOT ${boost_SOURCE_DIR})

# -------------------------------------------------------------------
# Catch2
message(NOTICE "Fetching Catch2...")
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
FetchContent_Declare(Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG ${Catch2Version})
FetchContent_MakeAvailable(Catch2)

# -------------------------------------------------------------------
# CppUTest
message(NOTICE "Fetching cpputest...")

# Prevent CppUTest's own tests from being built
set(TESTS OFF CACHE BOOL "")

# Prevent build of CppUTest from generating thousands of lines of
# -Wc++98-compat and -Wc++98-compat-pedantic warnings:
set(C++11 ON CACHE BOOL "Compile with C++11 support")

FetchContent_Declare(cpputest
        GIT_REPOSITORY https://github.com/cpputest/cpputest.git
        GIT_TAG ${CppUTestVersion})
FetchContent_MakeAvailable(cpputest)

# -------------------------------------------------------------------
# doctest
message(NOTICE "Fetching doctest...")
FetchContent_Declare(
        doctest
        GIT_REPOSITORY  https://github.com/onqtam/doctest.git
        GIT_TAG         ${DocTestVersion}
)
FetchContent_MakeAvailable(doctest)
set_target_properties(doctest_with_main PROPERTIES FOLDER "external")

# -------------------------------------------------------------------
# fmt
message(NOTICE "Fetching fmt...")
set(CATCH_BUILD_TESTING OFF CACHE BOOL "")
FetchContent_Declare(fmt
        GIT_REPOSITORY https://github.com/fmtlib/fmt.git
        GIT_TAG ${FmtVersion})
FetchContent_MakeAvailable(fmt)

# -------------------------------------------------------------------
# googletest
message(NOTICE "Fetching googletest...")
# GoogleTest
# Prevent GoogleTest from overriding our compiler/linker options
# when building with Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" )
FetchContent_Declare(googletest
        GIT_REPOSITORY https://github.com/abseil/googletest.git
        GIT_TAG ${GoogleTestVersion})
FetchContent_MakeAvailable(googletest)

# -------------------------------------------------------------------
# gulrak's filesystem
message(NOTICE "Fetching gulrak's filesystem...")
FetchContent_Declare(
        filesystem
        GIT_REPOSITORY  https://github.com/gulrak/filesystem.git
        GIT_TAG         ${GulrakFileSystemVersion}
)
FetchContent_MakeAvailable(filesystem)

# -------------------------------------------------------------------
# Boost.ut
message(NOTICE "Fetching boost.ut...")
set(BUILD_BENCHMARKS OFF CACHE BOOL "")
set(BUILD_EXAMPLES OFF CACHE BOOL "")
set(BUILD_TESTS OFF CACHE BOOL "")
FetchContent_Declare(boost.ut
        GIT_REPOSITORY https://github.com/boost-ext/ut.git
        GIT_TAG ${UtVersion})
FetchContent_MakeAvailable(boost.ut)

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
