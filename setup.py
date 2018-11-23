from setuptools import setup

setup(
    name        = 'pretty_number',
    version     = '0.1',
    author      = 'szsdk',
    package_dir = {'': 'src'},
    packages    = ['pretty_number'],
    py_modules  = ['pretty_number'],
    setup_requires=["pytest-runner"], 
    tests_require=["pytest"],
)
