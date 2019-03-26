from setuptools import setup, find_packages
import re

with open('snet_common_utils/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='snet_common_utils',
    version=version,
    packages=find_packages(),
    url='https://github.com/singnet/snet-sdk-python',
    license='MIT',
    author='SingularityNET Foundation',
    author_email='info@singularitynet.io',
    description='SingularityNET Common Utils'
)
