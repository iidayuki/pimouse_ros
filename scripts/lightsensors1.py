#!/usr/bin/env python
#encoding: utf8
import sys, rospy
from pimouse_ros.msg import LightSensorValues

def get_freq():
    f = rospy.get_param('lightsensors_freq',10)
    try:
       if f <= 0.0:
           raise Exception()

    except:
       rospy.logerr("value error: lightsensors_freq")
       sys.exit(1)

    return f

if __name__ == "__main__":
   devfile = '/dev/rtlightsensor0'
   rospy.init_node('lightsensors')
   pub = rospy.Publisher('lightsensors', LightSensorValue, queue_size=1)

  freq = get_freq()
  rate = rospy.Rate(freq)
  while not rospy.is_shutdown():
        try:
      

rospy.init_node('lightsensors')

