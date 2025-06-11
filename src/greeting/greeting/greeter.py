#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import pyttsx3

class CampusGreeter(Node):
    def __init__(self):
        super().__init__('campus_greeter')
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        self.get_logger().info('👋 Welcome to the Campus Tour!')
        self.speak('Welcome to the Campus Tour...')
        self.get_logger().info('🤖 I am your tour guide robot.')
        self.speak('I am your tour guide robot....')
    def speak(self , text):
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    rclpy.init()
    greeter = CampusGreeter()
    rclpy.spin(greeter)
    rclpy.shutdown()

if __name__ == '__main__':
    main()