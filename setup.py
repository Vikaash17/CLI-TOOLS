from setuptools import setup, find_packages

setup(
    name='cli-tool',
    version='0.1.0',
    description='A simple CLI tool for managing tasks',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'argparse',
        # Add other dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'cli-tool=main:main',  # Adjust this based on your main function location
        ],
    },
)