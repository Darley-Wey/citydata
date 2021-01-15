import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="citydata",
    version="0.0.1",
    author="Darley-Wey",
    author_email="darley.wey@gmail.com",
    description="get the Chinese city data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Darley-Wey/citydata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)