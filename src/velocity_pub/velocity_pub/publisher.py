import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('Vel_publisher_node')
        self.publisher = self.create_publisher(
            Twist , 
            '/cmd_vel',
            10
        )
        self.get_logger().warn("Velocity publisher node has started")
        self.get_logger().info("Use WADF keys to move")
    def send_velocity(self , linear_x , angular_z):
        twist = Twist()
        twist.linear.x = linear_x
        twist.angular.z = angular_z
        self.publisher.publish(twist)
        self.get_logger().warn(f'Publisher linear:{linear_x} and angular {angular_z}')
def main():
    rclpy.init()
    vel_pub = VelocityPublisher()
    print("🕹️ Controls:")
    print("W - Forward")
    print("S - Backward")
    print("A - Left Turn")
    print("D - Right Turn")
    print("X - Stop")
    print("Q - Quit")
    try:
        while True:
            key = input("Enter command W A S D ").lower()
            if key == 'w':
                vel_pub.send_velocity(0.5, 0.0)  # Move forward
            elif key == 's':
                vel_pub.send_velocity(-0.5, 0.0)  # Move backward
            elif key == 'a':
                vel_pub.send_velocity(0.0, 0.5)  # Turn left
            elif key == 'd':
                vel_pub.send_velocity(0.0, -0.5)  # Turn right
            elif key == 'x':
                vel_pub.send_velocity(0.0, 0.0)  # Stop
            elif key == 'q':
                vel_pub.get_logger().info("🛑 Shutting down.")
                break
            else:
                print("Invalid key. Use W/A/S/D/X/Q.")
    except KeyboardInterrupt:
        vel_pub.get_logger().error("User interrupted")
    finally :
        vel_pub.send_velocity(0.0,0.0)
        rclpy.shutdown()
if __name__ == '__main__':
    main()