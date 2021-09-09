
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [conan_cmake](/conan_cmake/)                                 |
| Purpose      | Demo how to build your tests using Conan's `cmake`  generator to download single headers for specific releases of ApprovalTests.cpp and Catch2.<br />The released headers of those dependencies will be downloaded inside your CMake build space, and will not be shown inside your IDE. |
| Dependencies | ApprovalTests.cpp - downloaded automatically by Conan<br/>Catch2 - downloaded automatically by Conan |
| Mechanism    | Uses Conan's [`cmake`](https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_generator.html) generator. |
| More Detail  | See [Example 2. Using Conan's cmake generator](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/ConanIntegration.md#example-2-using-conans-cmake-generator) |

