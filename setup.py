from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

requirements = ['pandas']

setup(
    name="dsnippets",
    version="0.0.1",
    author="Abram Flansburg",
    author_email="abeflansburg@gmail.com",
    description="Useful data science snippets - that you can import!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aflansburg/dsnippets",
    package_dir={'': 'src'},
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.7, <4',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)