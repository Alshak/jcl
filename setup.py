from setuptools import setup

setup(
    name='jcl',
    version='0.1',
    include_package_data=True,
    license='MIT License',
    packages=['jcl'],
    description='Package providing jcl widgets for ClowdFlows 2.0',
    
    install_requires=[
        'JPype1>=0.6.1',
    ],
    author='',
    author_email='',
)
