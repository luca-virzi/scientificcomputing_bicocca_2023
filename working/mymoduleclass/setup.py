from setuptools import setup, find_packages

setup(name='mymoduleclass',
      description='Exercise on test modules for the SciComp class held by Prof. D. Gerosa @ UniMiB',
      author='Luca Virzì',
      author_email='l.virzi1@campus.unimib.it',
      license='MIT',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])