import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pytmpfile",
    version="0.2.1",
    description="Extremely simple helper for the memory-tempfile package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jordiae/pytmpfile",
    authors=["mbello <mbello@users.noreply.github.com>"],
    mantainers=["jordiae <jordiae@users.noreply.github.com>"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.0",

    ],
    packages=["pytmpfile"],
    include_package_data=True,
    install_requires=[
        'memory-tempfile'
    ]

)