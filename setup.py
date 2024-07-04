from setuptools import find_packages, setup

setup(
    name='magshimimlib',
    packages=find_packages(include=["magshimimlib"]),
    version='0.1.0',
    description='A Magshimim explanatory library',
    author='A magshimim student, Kineret',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)