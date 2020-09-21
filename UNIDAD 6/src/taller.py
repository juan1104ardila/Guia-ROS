import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu

class CommandControl():

    def __init__(self):
        rospy.loginfo("Starting node")
        rospy.on_shutdown(self.safety_stop)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber('phone1/android/imu', Imu, self.callback)
        rospy.spin()

    def callback(self, data):
        arriba_atras=data.linear_acceleration.x
        izquierda_derecha=data.linear_acceleration.y

        if arriba_atras>1.0 and izquierda_derecha<1.0 and izquierda_derecha>-1.0:
            linear_x=arriba_atras #RIGHT_ANALOG_VER
            angular_z=0.0 #LEFT_ANALOG_HOR
            print(linear_x)
            print(angular_z)
        elif arriba_atras<-1.0 and izquierda_derecha<1.0 and izquierda_derecha>-1.0:
            linear_x=arriba_atras #RIGHT_ANALOG_VER
            angular_z=0.0 #LEFT_ANALOG_HOR
            print(linear_x)
            print(angular_z)
        elif izquierda_derecha>1.0 and arriba_atras<1.0 and arriba_atras>-1.0:
            linear_x=0.0 #RIGHT_ANALOG_VER
            angular_z=izquierda_derecha #LEFT_ANALOG_HOR
            print(linear_x)
            print(angular_z)
        elif izquierda_derecha<-1.0 and arriba_atras<1.0 and arriba_atras>-1.0:
            linear_x=0.0 #RIGHT_ANALOG_VER
            angular_z=izquierda_derecha #LEFT_ANALOG_HOR
            print(linear_x)
            print(angular_z)
        else:
            linear_x=0
            angular_z=0
        self.send_velocities(linear_x, angular_z)

    def send_velocities(self,linear_x,angular_z):
        twist_msg = Twist()
        twist_msg.linear.x=linear_x*0.5
        twist_msg.linear.y=0.0
        twist_msg.linear.z=0.0
        twist_msg.angular.x=0.0
        twist_msg.angular.y=0.0
        twist_msg.angular.z=angular_z*0.5
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
