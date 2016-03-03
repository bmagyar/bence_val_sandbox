#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray, MultiArrayDimension

commands = [0.2, 0.0, -0.2, 0.0]

def talker():
    pub = rospy.Publisher('/right_arm_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('publish_to_controller', anonymous=True)
    rate = rospy.Rate(1) # 10hz


    msg = Float64MultiArray()
    msg.data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    dim = MultiArrayDimension()
    dim.size = len(msg.data)
    dim.label = "command"
    dim.stride = len(msg.data)
    msg.layout.dim.append(dim)
    msg.layout.data_offset = 0

    i = 0
    while not rospy.is_shutdown():
        hello_str = "sent command %d %s" % (i, rospy.get_time())
        rospy.loginfo(hello_str)

        msg.data[0] = commands[i]
        i = (i+1)%len(commands)
        print msg
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
