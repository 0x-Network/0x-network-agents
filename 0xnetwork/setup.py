# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oxnetwork",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="A Python client for interacting with 0x-network Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/oxnetwork",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
