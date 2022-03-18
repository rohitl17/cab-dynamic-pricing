import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cab-dynamic-pricing",
    version="1.0.0",
    author=["Nayantara Mohan", "Rohit Lokwani", "Shubha Changappa Palachanda"],
    author_email="rlokwani@uw.edu",
    description="A web application for calculating dynamic \
                 price of Uber and Lyft cabs depending on various parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohitl17/cab-dynamic-pricing",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                      "tests.*", "tests"]),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
