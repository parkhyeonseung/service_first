#! /usr/bin/env python3

import rospy
from service_first.srv import addtwoints

def servi(deg):
    rospy.wait_for_service('degree')
    add_two_ints = rospy.ServiceProxy('degree',addtwoints)
    result = add_two_ints(deg,0.0)
    print('radian')
    print(result)

if __name__ == '__main__':
    deg = float(input('degree? :'))
    servi(deg)



########################################33
# import rospy
# from service_first.srv import addtwoints

# if __name__ == '__main__':
#     rospy.wait_for_service('addtwo')

#     add_two_ints = rospy.ServiceProxy('addtwo',addtwoints)
#     result = add_two_ints(3,4)
#     print(result)