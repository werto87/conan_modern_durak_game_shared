cmake_minimum_required(VERSION 3.12)
project(test_package LANGUAGES CXX)

find_package(small_memory_tree REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE small_memory_tree::small_memory_tree)
if(confu_json_VERSION VERSION_LESS "1.0.0")
    target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20)
else()
    target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
endif()