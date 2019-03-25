import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="moyasar",
    version="0.6.1",
    author="Moyasar",
    author_email="developers@moyasar.com",
    description="Moyasar Python language wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moyasar/moyasar-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    tests_require=[
        'httpretty',
        'pytest'
    ],
    download_url='https://github.com/moyasar/moyasar-python/archive/v0.6.1.tar.gz'
)
