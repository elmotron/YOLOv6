from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='yolov6',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_data={"": ["*.yaml", "*.sh", "*.md", "*.jpg", "*.ttf"]}, # NOTE: use this for non-pythonic files needed, such as configs, demo data etc...
    description='YOLOv6 object detection framework'
)
