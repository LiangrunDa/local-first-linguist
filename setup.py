from setuptools import setup, find_packages

setup(
    name='local-first-linguist',
    version='0.1',
    author_email='me@liangrunda.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
          'console_scripts': [
              'translate=src.cli:cli'
          ]
      }
)
