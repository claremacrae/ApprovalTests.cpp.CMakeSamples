add_executable(tests
        main.cpp
        tests.cpp
)
target_link_libraries(tests ApprovalTests::ApprovalTests Catch2v2::Catch2v2)

target_compile_features(tests PUBLIC cxx_std_11)
set_target_properties(tests PROPERTIES CXX_EXTENSIONS OFF)

add_test(
        NAME tests
        COMMAND tests)
