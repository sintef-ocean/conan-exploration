[![Linux GCC](https://github.com/sintef-ocean/conan-exploration/workflows/Linux%20GCC/badge.svg)](https://github.com/sintef-ocean/conan-exploration/actions?query=workflow%3A"Linux+GCC")
[![Linux Clang](https://github.com/sintef-ocean/conan-exploration/workflows/Linux%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-exploration/actions?query=workflow%3A"Linx+Clang")
[![Windows MSVC](https://github.com/sintef-ocean/conan-exploration/workflows/Windows%20MSVC/badge.svg)](https://github.com/sintef-ocean/conan-exploration/actions?query=workflow%3A"Windows+MSVC")
[![Windows MSVC Clang](https://github.com/sintef-ocean/conan-exploration/workflows/Windows%20MSVC%20Clang/badge.svg)](https://github.com/sintef-ocean/conan-exploration/actions?query=workflow%3A"Windows+MSVC+Clang")
[![Macos Apple-Clang](https://github.com/sintef-ocean/conan-exploration/workflows/Macos%20Apple-Clang/badge.svg)](https://github.com/sintef-ocean/conan-exploration/actions?query=workflow%3A"Macos+Apple-Clang")

[Conan.io](https://conan.io) recipe for a "hello world" library.

## How to use this package

1. Add remote to conan's package [remotes](https://docs.conan.io/2/reference/commands/remote.html)

   ```bash
   $ conan remote add sintef https://artifactory.smd.sintef.no/artifactory/api/conan/conan-local
   ```

2. Using [*conanfile.txt*](https://docs.conan.io/2/reference/conanfile_txt.html) and *cmake* in your project.

   Add *conanfile.txt*:
   ```
   [requires]
   exploration/[~1.0.0]@sintef/stable

   [tool_requires]
   cmake/[>=3.25.0]

   [options]

   [layout]
   cmake_layout

   [generators]
   CMakeDeps
   CMakeToolchain
   VirtualBuildEnv
   ```
   Insert into your *CMakeLists.txt* something like the following lines:
   ```cmake
   cmake_minimum_required(VERSION 3.13)
   project(TheProject CXX)

   find_package(exploration REQUIRED)

   add_executable(the_executor code.cpp)
   target_link_libraries(the_executor exploration::exploration)
   ```
   Install and build e.g. a Release configuration:
   ```bash
   $ conan install . -s build_type=Release -pr:b=default
   $ source build/Release/generators/conanbuild.sh
   $ cmake --preset conan-release
   $ cmake --build build/Release
   $ source build/Release/generators/deactivate_conanbuild.sh
   ```

## Package options

Option | Default | Allowed
---|---|---
`shared`      | False |     [True, False]
`fPIC`        | True  |     [True, False]

## Known recipe issues
