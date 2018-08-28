from setuptools import setup

setup(name='gym_gomoku',
      version='0.0.1',
      url='https://github.com/Pankaic/gym-gomoku',
      author='Patrick Lin',
      license='MIT',
      packages=['gym_gomoku', 'gym_gomoku.envs'],
      install_requires=['gym', 'numpy']  # And any other dependencies foo needs
)  