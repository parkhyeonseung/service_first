#! /usr/bin/env python3

import rospy
from service_first.srv import addtwoints

def servi(velo,time):
    rospy.wait_for_service('distance')
    add_two_ints = rospy.ServiceProxy('distance',addtwoints)
    result = add_two_ints(velo,time)
    print('distance')
    print(result)

if __name__ == '__main__':
    velo = float(input('velocity :'))
    time = float(input('time : '))
    servi(velo,time)



########################################33
# import rospy
# from service_first.srv import addtwoints

# if __name__ == '__main__':
#     rospy.wait_for_service('addtwo')

#     add_two_ints = rospy.ServiceProxy('addtwo',addtwoints)
#     result = add_two_ints(3,4)
#     print(result)