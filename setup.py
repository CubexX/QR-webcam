from setuptools import setup

setup(name='RTQR',
      version='0.1',
      description='Decode QR code from webcam',
      url='https://github.com/CubexX/RTQR',
      author='CubexX',
      author_email='CubexX@404.pm',
      license='MIT',
      install_requires=[
          'zbarlight',
          'opencv-python',
          'pillow'
      ],
      packages=['RTQR'],
      zip_safe=False)
