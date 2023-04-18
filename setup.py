from setuptools import setup, find_packages

setup(
    name='example_publish_pypi_medium',
    version='0.0.1',
    license='GNU General Public License v3.0',
    author="Benedict Saunders",
    author_email='benedictsaunders@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/benedictsaunders/PyFINPUT',
    keywords='input, file, keywords',
    install_requires=[],
    description = "A simple parser for a file input, akin to the format of argparse",
)