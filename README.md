# RealLinting

This action checks a repo with clang-tidy. The checked repo is expect to have .clang-tidy file in place. There must be no errors and no warnings reported for the action to succeed.

## Usage

CMake configuration must succeed on the project to be checked and it must [export compile commands](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html) for the files to be checked.

```yaml
- uses: ZADNE/RealLinting@v0.1
  with:
    # The clang-tidy to use (default: clang-tidy)
    clang-tidy:
    # Absolute file path to the compile_commands.json file generated by CMake
    compile-commands-json:
    # The file that will contain errors and warnings reported by clang-tidy (default: ./clang-tidy-report.txt)
    report-file:
```