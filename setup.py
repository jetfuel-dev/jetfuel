import setuptools

setuptools.setup(
    name="jetfuel",
    version="0.0.14",
    author="Jared Zhao",
    description="Python Performance Profiling for Production",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jetfuel-dev/jetfuel",
    license="Apache 2.0",
    python_requires=">=3.6",
    install_requires=[
        "requests >= 2.0.0",
    ],
    packages=["jetfuel"],
)
