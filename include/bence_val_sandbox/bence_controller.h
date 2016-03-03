#include <controller_interface/controller.h>
#include <hardware_interface/joint_command_interface.h>
#include <pluginlib/class_list_macros.h>

#include <realtime_tools/realtime_buffer.h>
#include <realtime_tools/realtime_publisher.h>

namespace bence_val_sandbox
{
class BenceController
      : public controller_interface::Controller<hardware_interface::EffortJointInterface>
{
  public: 
    BenceController();
    bool init(hardware_interface::EffortJointInterface* hw,
              ros::NodeHandle& root_nh,
              ros::NodeHandle &controller_nh);
    void update(const ros::Time& time, const ros::Duration& period);

    void starting(const ros::Time& time);

    void stopping(const ros::Time& /*time*/);

  private:

    std::vector<hardware_interface::JointHandle> joints_;
}; // class BenceController
} // namespace bence_val_sandbox
PLUGINLIB_EXPORT_CLASS(bence_val_sandbox::BenceController, controller_interface::ControllerBase);
