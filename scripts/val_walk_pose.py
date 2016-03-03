#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray, MultiArrayDimension

def talker():
    torso_pub = rospy.Publisher('/torso_controller/command', Float64MultiArray, queue_size=10)
    left_leg_pub = rospy.Publisher('/left_leg_controller/command', Float64MultiArray, queue_size=10)
    right_leg_pub = rospy.Publisher('/right_leg_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('publish_to_controller', anonymous=True)
    rate = rospy.Rate(1)

    msg = Float64MultiArray()
    # hipyaw, hiproll, hippitch, kneepitch, anklepitch, ankleroll
    msg.data = [0.0, 0.0, -0.63, 1.03, -0.44, 0.0]
#    msg.data = [0.0, 0.0, 0., 0.0, 0., 0.0]
    dim = MultiArrayDimension()
    dim.size = len(msg.data)
    dim.label = "command"
    dim.stride = len(msg.data)
    msg.layout.dim.append(dim)
    msg.layout.data_offset = 0

    torso_msg = Float64MultiArray()
    torso_msg.data = [0.0, 0.2, 0.0]
    dim = MultiArrayDimension()
    dim.size = len(torso_msg.data)
    dim.label = "command"
    dim.stride = len(torso_msg.data)
    torso_msg.layout.dim.append(dim)
    torso_msg.layout.data_offset = 0



    while not rospy.is_shutdown():
        print msg
        left_leg_pub.publish(msg)
        right_leg_pub.publish(msg)
        torso_pub.publish(torso_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
