#! /usr/bin/env python3

"""
    Description: 
        This ROS2 node periodically publishes "Hello World" messages to a topic.
    ----------------------------------------------------------------------------
    Publishing Topics:
        The channel containing the "Hello World" messages
        /py_example_topic - std_msgs/String
    
    Subscriptions Topics:
        None
    -------------------------------------------
    Author: David Brigido-Gonzalez
    Date: September 4, 2026
"""
import rclpy # Import the ROS 2 client library for python
from rclpy.node import Node # Import the Node class, used for creating nodes

from std_msgs.msg import String # Import String message type for ROS 2

class MinimalPyPublisher(Node):
    """Create a minimal publisher node

    """
    def __init__(self):
        """Create a custom node class for publishing messages
        """
        # Initialize the node with a name
        super().__init__('minimal_py_publisher')

        #Create a publisher on the topic with a queue size of 10 message
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        # Create a timer with a perido of 0.5 seconds to trigger publishing of messages
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Initialize a counter variable for message content
        self.i = 0

    def timer_callback(self):
        """Callback function executed periodically by the timer
        """
        # Create a new String message object
        msg = String()

        # Set the message data with a counter 
        msg.data = 'Hello World: %d' % self.i

        #Publish the message you created above to a topic
        self.publisher_1.publish(msg)

        # Log a message indicating the message has been published
        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.i = self.i + 1

def main(args=None):
    """Main function to start the ROS 2 node

    Args:
        args (_type_, optional): Command-line argument. Default to none

    """
    rclpy.init(args=args)

    # Create an instance of the Minimal Publisher Node
    minimal_py_publisher = MinimalPyPublisher()

    rclpy.spin(minimal_py_publisher)

    # Destroy the node explicity
    minimal_py_publisher.destroy_node()

    # Shutdown Ros 2 Comunication
    rclpy.shutdown()

if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()
