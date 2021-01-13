#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image as ImageMsg
from cv_bridge import CvBridge
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def change_color_and_text(msg):
    bridge = CvBridge()
    fontpath = 'yumin.ttf'
    cascade_path = "/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml"
    orig = bridge.imgmsg_to_cv2(msg, "bgr8")
    gray_img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    gray_bgr_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    cascade = cv2.CascadeClassifier(cascade_path)
    face = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

    if len(face) > 0:
                          
        font = ImageFont.truetype(fontpath, 600)
        img_pil = Image.fromarray(gray_bgr_img)
        draw = ImageDraw.Draw(img_pil)
      
        draw.text((290, 170), '35歳の', font=font, fill=(0,0,255))
        draw.text((290, 760), '少女', font=font, fill=(0,0,255))

        gray_bgr_img = np.array(img_pil)

        imgmsg = bridge.cv2_to_imgmsg(gray_bgr_img, "bgr8")

    else:
        imgmsg = bridge.cv2_to_imgmsg(orig, "bgr8")
    
    pub = rospy.Publisher('gray_img', ImageMsg, queue_size = 1)
    pub.publish(imgmsg)


def main():
    rospy.init_node('change_color_and_text')
    sub = rospy.Subscriber('/cv_camera/image_raw', ImageMsg, change_color_and_text)
    pub = rospy.Publisher('gray_img', ImageMsg, queue_size=1)
    rospy.spin()

if __name__=='__main__':
    main()
