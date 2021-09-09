cmake_minimum_required(VERSION 3.11)

include(FetchContent)
FetchContent_Declare(
  vcpkg
  GIT_REPOSITORY https://github.com/microsoft/vcpkg
  GIT_TAG b295670e4bab14debe88d92cd5364b21ce26232c # 2021-09-09
)
if(NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  FetchContent_Populate(vcpkg)
  set(CMAKE_TOOLCHAIN_FILE "${vcpkg_SOURCE_DIR}/scripts/buildsystems/vcpkg.cmake")
endif()

project(vcpkg_cmake CXX)

enable_testing()

add_subdirectory(tests)
