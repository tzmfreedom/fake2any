from setuptools import setup, find_packages

setup(
    name='fake2any',
    version='1.0.0',
    url='https://github.com/tzmfreedom/fake2any',
    install_requires=["pyforce","pyyaml","faker"]
    packages=find_packages(exclude=['tests*']),
)