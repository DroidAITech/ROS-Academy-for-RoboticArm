#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        
        # 初始化需要使用move group控制的机械臂中的gripper group
        gripper_1 = moveit_commander.MoveGroupCommander('gripper_1')
        gripper_2 = moveit_commander.MoveGroupCommander('gripper_2')
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001)
        gripper_1.set_goal_joint_tolerance(0.001)
        gripper_2.set_goal_joint_tolerance(0.001)

        # 设置夹爪的目标位置，并控制夹爪运动
        gripper_1.set_joint_value_target([0.01])
        gripper_1.go()
        rospy.sleep(1)

        gripper_2.set_joint_value_target([0.01])
        gripper_2.go()
        rospy.sleep(1)
         
        # 设置机械臂的目标位置，使用4轴的位置数据进行描述（单位：弧度）
        joint_positions = [0, 0, 1.57, 1.50]
        arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)
        
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
