
colcon build --symlink-install

ros2 launch my_bot rsp.launch.py
rviz2 -d /home/andre/Documents/Embedded/ROS/dev_ws/src/my_bot/my_bot.rviz
ros2 run joint_state_publisher_gui joint_state_publisher_gui

# ros2 launch gazebo_ros gazebo.launch.py
# ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name

### Launch Gazebo with my bot.
ros2 launch my_bot launch_sim.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard