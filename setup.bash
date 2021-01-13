#!/bin/bash

roscore &
rosrun cv_camera cv_camera_node &
rosrun web_video_server web_video_server &
rosrun robosys_ros shirokuro.py
