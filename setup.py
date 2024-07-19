from setuptools import setup, find_packages

# Replace with your project information
project_name = "phrenology"
version = "0.1.0"
description = "A tool for analyzing your security HEADers"
author = "SecurityShrimp"
author_email = "securityshrimp@proton.me"
url = "https://github.com/f8al/phrenology"  # Optional
# license = "MIT"  # Optional

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.13',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Security',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]

# Dependencies (replace with your required packages)
dependencies = [
    "requests",
    "urllib"
]

setup(
    name=project_name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    #license=license,
    packages=find_packages(exclude=("tests*",)),  # Exclude test directories
    install_requires=dependencies,
)