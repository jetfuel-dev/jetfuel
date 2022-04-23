import setuptools

setuptools.setup(
    name="mocha-time",
    version="0.0.5",
    author="Jared Zhao",
    description="Python Performance Profiling for Production",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mocha-dev/mocha",
    license="Apache 2.0",
    python_requires=">=3.6",
    packages=["mocha"],
)
