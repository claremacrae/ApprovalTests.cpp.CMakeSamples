add_executable(tests
  main.cpp
  tests.cpp
)

find_path(approvaltests.cpp_INCLUDE_DIR
  NAMES "ApprovalTests.hpp")
find_package(Catch2 REQUIRED)
target_include_directories(tests
  PRIVATE "${approvaltests.cpp_INCLUDE_DIR}"
)
target_link_libraries(tests
  PRIVATE Catch2::Catch2
)

target_compile_features(tests PUBLIC cxx_std_11)
set_target_properties(tests PROPERTIES CXX_EXTENSIONS OFF)

add_test(
  NAME tests
  COMMAND tests
)
