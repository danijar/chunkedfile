import setuptools
import pathlib


setuptools.setup(
    name='chunkedfile',
    version='0.3.0',
    description='Save file writes into multiple chunks.',
    url='http://github.com/danijar/chunkedfile',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['chunkedfile'],
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
