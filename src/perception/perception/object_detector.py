import rclpy 
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
import numpy as np 
from sensor_msgs.msg import Image

class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector_node')
        self.subscription = self.create_subscription(
            Image , 
            '/camera/image_raw',
            self.image_callback,
            20
        )         
        self.bridge = CvBridge()   
        self.get_logger().warn('Object detection Node started !!!')
    def image_callback(self,msg):
        return 