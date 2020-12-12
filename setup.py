import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guid", # Replace with your own username
    version="1.0.0",
    author="Marcus Turewicz",
    description="A Python package to generate a guid",
    url="https://github.com/marcusturewicz/python-github-packages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
