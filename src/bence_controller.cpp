#include <bence_val_sandbox/bence_controller.h>
#include <ros/console.h>

namespace bence_val_sandbox
{

  BenceController::BenceController()
  {
  }
  
  bool BenceController::init(hardware_interface::EffortJointInterface* hw,
            ros::NodeHandle& root_nh,
            ros::NodeHandle &controller_nh)
  {
    return true;
  }

  void BenceController::update(const ros::Time& time, const ros::Duration& period)
  {
    ROS_INFO_STREAM_THROTTLE(1.0, "Hello");
  }

  void BenceController::starting(const ros::Time& time)
  {}

  void BenceController::stopping(const ros::Time& /*time*/)
  {}

}
