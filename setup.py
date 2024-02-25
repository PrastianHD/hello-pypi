from setuptools import setup, find_packages

setup(
    name='hello-pypi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Dependencies
    ],
    entry_points={
        'console_scripts': [
            'hello-pypi=hello_pypi.main:main',
        ],
    },
    author='PrastianHD',
    author_email='prastianhidayat08@gmail.com',
    description='A simple Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prastianhd/hello-pypi',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
