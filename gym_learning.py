import gym
env = gym.make('MountainCar-v0',new_step_api=True)

# Observation and action space
obs_space = env.observation_space
action_space = env.action_space
print(f"The observation space: {obs_space}")
print(f"The action space: {action_space}")