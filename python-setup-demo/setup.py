from setuptools import setup, find_packages

setup(
    name='python-setup-demo',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'python-setup-demo = python_setup_demo.main:main',
        ],
    },
)
