from gym.envs.registration import register

register(
    id='gomoku-large-v0',
    entry_point='gym_gomoku.envs:GomokuLargeEnv',
    timestep_limit=361,
)
register(
    id='gomoku-medium-v0',
    entry_point='gym_gomoku.envs:GomokuMediumEnv',
    timestep_limit=225,
)
register(
    id='gomoku-small-v0',
    entry_point='gym_gomoku.envs:GomokuSmallEnv',
    timestep_limit=121,
)