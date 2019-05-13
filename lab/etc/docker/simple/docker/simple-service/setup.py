import setuptools

VERSION = '0.0.1'

setuptools.setup(
    name = 'simple_service',
    version = VERSION,
    description = '',
    long_description = '',
    packages = [
        '.',
    ],
    setup_requires = [
    ],
    install_requires = [
        'tornado==4.3'
    ],
)
