
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    # Include the robot_state_publisher launch file, provided by our own package.
    # Force sim time to be enabled.

    package_name    = "my_bot"
    world_file_name = "room.world"

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_share      = get_package_share_directory(package_name)

    world_path = os.path.join(pkg_share, 'worlds', world_file_name)

    ###

    world = LaunchConfiguration('world')
    declare_world_cmd = DeclareLaunchArgument(
        name='world',
        default_value=world_path,
        description="Full path to the world model file to load"
    )

    ###
    
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_share, 'launch', 'rsp.launch.py'
        )]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_gazebo_ros, 'launch', 'gazebo.launch.py'
        )]),
        launch_arguments={'world': world}.items()
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=[
                            '-topic', 'robot_description',
                            '-entity', 'my_bot'
                        ],
                        output='screen'
    )

    ###

    ld = LaunchDescription()

    ld.add_action(declare_world_cmd)

    ld.add_action(rsp)
    ld.add_action(gazebo)
    ld.add_action(spawn_entity)

    return ld