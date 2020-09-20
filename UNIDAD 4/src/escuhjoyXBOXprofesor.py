import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class CommandControl():

    def __init__(self):
        rospy.loginfo("Starting node")
        rospy.on_shutdown(self.safety_stop)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber('joy', Joy, self.callback)
        rospy.spin()

    def callback(self, data):
        # Charectization GamePad Logitech F710
        # READ BUTTONS
        A=data.buttons[0]
        B=data.buttons[1]
        X=data.buttons[2]
        Y=data.buttons[3]
        LB=data.buttons[4]
        RB=data.buttons[5]
        BACK=data.buttons[6]
        START=data.buttons[7]
        LOGITECH=data.buttons[8]
        ANALOG_L=data.buttons[9]
        ANALOG_R=data.buttons[10]
        # READ Axes
        #LEFT_ANALOG_HOR=data.axes[0] # <<(+)
        LEFT_ANALOG_VER=data.axes[1] # ^^(+)
        LT=data.axes[2] #[1 -1]
        RIGHT_ANALOG_HOR=data.axes[3] # <<(+)
        #RIGHT_ANALOG_VER=data.axes[4] # ^^(+)
        RT=data.axes[5] #[1 -1]
        LEFT_RIGHT = data.axes[0] # left=1, right=-1
        FRONT_BACK = data.axes[4] # front=1, back=-1
        ##
        if LB==1:
            linear_x=FRONT_BACK #RIGHT_ANALOG_VER
            angular_z=LEFT_RIGHT #LEFT_ANALOG_HOR
            print(linear_x)
            print(angular_z)
        else:
            linear_x=0
            angular_z=0
        self.send_velocities(linear_x, angular_z)

    def send_velocities(self,linear_x,angular_z):
        twist_msg = Twist()
        twist_msg.linear.x=linear_x
        twist_msg.linear.y=0.0
        twist_msg.linear.z=0.0
        twist_msg.angular.x=0.0
        twist_msg.angular.y=0.0
        twist_msg.angular.z=angular_z
        self.pub.publish(twist_msg)

    def stop(self):
        twist_msg = Twist()
        twist_msg.linear.x=0.0
        twist_msg.linear.y=0.0
        twist_msg.linear.z=0.0
        twist_msg.angular.x=0.0
        twist_msg.angular.y=0.0
        twist_msg.angular.z=0.0
        self.pub.publish(twist_msg)

    def safety_stop(self):
        for i in range(0,5):
            self.stop()
            rospy.sleep(0.5)


if __name__ == '__main__':
    rospy.init_node("command_control")
    cv = CommandControl()
