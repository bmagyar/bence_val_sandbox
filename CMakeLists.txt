cmake_minimum_required(VERSION 2.8.3)
project(bence_val_sandbox)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  control_msgs
  controller_interface
  urdf
  realtime_tools
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES bence_controller
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_library(bence_controller src/bence_controller.cpp)
target_link_libraries(bence_controller ${catkin_LIBRARIES})

install(TARGETS bence_controller
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )

install(FILES bence_plugins.xml
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
