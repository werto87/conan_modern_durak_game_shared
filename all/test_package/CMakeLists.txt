cmake_minimum_required(VERSION 3.12)
project(test_package LANGUAGES CXX)

find_package(modern_durak_game_shared REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE modern_durak_game_shared::modern_durak_game_shared)