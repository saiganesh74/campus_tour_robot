import rclpy 
from rclpy.node import Node 
class SimulatorNode(Node):
    def __init__(self):
        super().__init__('simulator_node')
        self.get_logger().info('Simulator Node is started and running')
def main():
    rclpy.init()
    node = SimulatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()