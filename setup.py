import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getv",
    version="0.1.0",
    author="FUNNYDMAN",
    author_email="crazy-dzmitry@mail.ru",
    description="Display release info somewhere in your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FUNNYDMAN/getv.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
