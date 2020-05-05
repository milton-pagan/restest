import main
from setuptools import setup


setup(name='restest',
      version='0.0.1',
      description='Programming Language for testing restful apis',
      author='Milton Pagan, Kenneth Rosario, Dionel Martinez, Javier Cuebas',
      author_email='',
      url='',
      install_requires=['ply', 'requests'],
      entry_points={
          'console_scripts': [
              'restest=main:main'
          ]
      }
    )

