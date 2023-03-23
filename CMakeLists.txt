cmake_minimum_required(VERSION 3.13)

file(STRINGS "${CMAKE_SOURCE_DIR}/version.txt" projectVersion)
project(exploration
  LANGUAGES CXX
  VERSION "${projectVersion}"
  DESCRIPTION "Exploration test project")

add_library(exploration src/somecode.cpp)
target_include_directories(exploration PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>)

set_target_properties(exploration PROPERTIES
  PUBLIC_HEADER "include/exploration/space.hpp"
  WINDOWS_EXPORT_ALL_SYMBOLS true
  )

install(TARGETS exploration
  LIBRARY DESTINATION lib
  PUBLIC_HEADER DESTINATION include/exploration
  )
