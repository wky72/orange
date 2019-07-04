# from distutils.core import setup
from setuptools import setup
from setuptools import find_packages

setup(name="orange",
      version='0.0.1',
      description='python tools',
      author='wky',
      author_email='1351654450@qq.com',
      url='https://github.com/wky72/orange.git',
      license='MIT',
      install_requires=["re>=2.2.1",],
      packages=find_packages(exclude=["logs"]),)