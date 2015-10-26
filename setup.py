from setuptools import setup

setup(
    name='i3-swap',
    version='1.0.0',
    description='Swap workspaces with a dual monitor setup',
    url='https://github.com/saneki/i3-swap',
    author='saneki',
    author_email='s@neki.me',
    license='GPL-3.0',
    install_requires=['i3-py'],
    scripts=['i3-swap'],
)
