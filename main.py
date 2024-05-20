#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
from factory_context import factory_context

planner = factory_context.run(11, 11, 4, 3, [(5, 1), (4, 5), (1, 7), (7, 9)])
def talker():
    pub = rospy.Publisher('path', Int16MultiArray, queue_size=10)

    data = Int16MultiArray()
    path = planner.get_path((0, 0, 0, 0, 0, 0, 0))
    path = np.array(path)
    data.data = path.flatten()

    rospy.init_node('path_planning', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass