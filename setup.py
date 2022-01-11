from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
  readme = readme_file.read()

requirements = []

setup(
    name="notebookc",
    version="0.0.1",
    author="Abram Flansburg",
    author_email="abeflansburg@gmail.com",
    description="Useful data science snippets - that you can import!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/aflansburg/dsnippets",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)