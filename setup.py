from setuptools import setup, find_packages


setup(
    name='mnff',
    version='0.0.1',
    author='yupix',
    description='',
    packages=find_packages(),
    install_requires=['mi.py'],
    entry_points={
        'console_scripts': [
            'mnff=mnff.cli:main',
        ]
    }

)
