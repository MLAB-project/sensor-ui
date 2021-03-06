#!/usr/bin/env python

import rospy
import pymlab
from pymlab import config
import sys
import sensor_server
from std_msgs.msg import String
from std_msgs.msg import Float32
import std_msgs
from sensor_server.srv import *
from sensor_server.msg import *

def Data(msg, callback_args=None):
    callback_args['send'][str(msg.name)].publish(msg.value)

def main():
    #sender.publish(name=str(devices[x]), value=data)
    rospy.init_node('pymlab_plotter_connector')
    values = rospy.get_param("values")
    send = {}
    for x in values:
        send[x]=rospy.Publisher("pymlab/"+str(x), Float32)
    print "send >>>", send
    rospy.Subscriber("pymlab_data", SensorValues, Data, callback_args={'values': values, 'send': send})
    rospy.spin()

if __name__ == "__main__":
    main()




#   [{'lts': <rospy.topics.Publisher object at 0xb64e89b0>,
#    'sht': <rospy.topics.Publisher object at 0xb64e87f0>},
#    {'lts': "LTS01(name = 'lts01', address = 72)",
#    'sht': "SHT25(name = 'sht25', address = 64)"}]
#    msg: name: SHT25(name = 'sht25', address = 64)
