import setuptools


with open("requirements.txt", "r", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("HISTORY.md", "r", encoding="utf-8") as f:
    history = f.read()



setuptools.setup(
    name="bit_help",
    version="0.0.3",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="daveusa31",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": "https://github.com/daveusa31/bit-help"
    },
)