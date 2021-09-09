
| Topic        | Detail                                                       |
| ------------ | ------------------------------------------------------------ |
| Directory    | [vcpkg_cmake](/vcpkg_cmake/)                                 |
| Purpose      | Demo how to build your tests using vcpkg to obtain Catch2 and ApprovalTests.cpp.<p />Vcpkg is obtained automatically via `FetchContent()` in the top level CMakeLists.txt, and built inside your CMake build space.<br /><p />The first time this is run in any given build space, there is a significant wait, but subsequent runs are much faster.<p />If you have multiple build spaces, vcpkg will be cloned and built multiple times, so this may be best used when you are only building one or two configurations.|
| Dependencies | ApprovalTests.cpp - obtained automatically by vcpkg<br/>Catch2 - obtained automatically by vcpkg |
| Mechanism    | Uses CMake's `FetchContent()` to obtain and build a specific version of vcpkg inside the build space.<p />Uses vcpkg's [manifest mode](https://vcpkg.readthedocs.io/en/latest/users/manifests/) to specify the dependencies. |
| More Detail  | See [ApprovalTests.cpp Vcpkg Integration docs](https://github.com/approvals/ApprovalTests.cpp/blob/master/doc/VcpkgIntegration.md#top) - TODO Update that page to add descriptive info for this example|

