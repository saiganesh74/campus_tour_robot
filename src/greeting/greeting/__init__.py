#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class CampusGreeter(Node):
    def __init__(self):
        super().__init__('campus_greeter')
        self.get_logger().info('👋 Welcome to the Campus Tour!')
        self.get_logger().info('🤖 I am your tour guide robot.')

def main():
    rclpy.init()
    greeter = CampusGreeter()
    rclpy.spin(greeter)
    rclpy.shutdown()

if __name__ == '__main__':
    main()