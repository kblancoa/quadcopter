from task import Task

class EuclideanDistanceTask(Task):
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, init_angle_velocities=None, runtime=5., target_pos=None):
        Task.__init__(self, init_pose=init_pose, init_velocities=init_velocities,
                      init_angle_velocities=init_angle_velocities, runtime=runtime, target_pos=target_pos)

        position = self.sim.pose[0:3]
        self.init_distance =  0
        for axis in range(0,3):
            self.init_distance += abs(self.sim.pose[axis] - self.target_pos[axis]) ** 2

  

    def get_reward(self):
        """
        Euclidean based reward. Closer to the target but included instability on rotors as penalized behavior.
        :return:
        """
        position = self.sim.pose[0:3]
        distance = 0
        for axis in range(0,3):
            distance += abs(position[axis] - self.target_pos[axis]) ** 2
        
        
        return 1 - (self.init_distance - distance) / self.init_distance