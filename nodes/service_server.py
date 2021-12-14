#! /usr/bin/env python3

import rospy
from service_first.srv import addtwoints,addtwointsResponse
import numpy as np

def callback_dis(req):
    rospy.loginfo('%s ,%s' % (req.a,req.b))
    return addtwointsResponse(req.a*req.b)

def callback_rad(req):
    rospy.loginfo('%s ' % (req.a))
    return addtwointsResponse(req.a*np.pi/180)

def servi():
    rospy.init_node('distance_server')
    rospy.Service('distance',addtwoints,callback_dis)
    rospy.Service('degree',addtwoints,callback_rad)

    rospy.spin()

if __name__ == '__main__':
    servi()
# import rospy
# # custom service messsage
# from service_first.srv import addtwoints, addtwointsResponse

# def fun_callback(req):
#     rospy.loginfo('%s, %s' % (req.a, req.b))
#     return addtwointsResponse(req.a + req.b)

# if __name__ == '__main__':
#     # server 선언
#     rospy.init_node('addtwo_server')
#     # server 기다리기
#     rospy.Service('addtwo',addtwoints,fun_callback)

#     rospy.spin()
#     pass
