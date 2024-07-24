from setuptools import setup, find_packages
'''
**phrenology - A tool for analyzing your security HEADers**

**phrenology** is a Python package that helps you analyze the security headers of a website. It provides functionalities to fetch headers, 
parse them, and identify potential security vulnerabilities.

**Key Features:**

* Fetches website headers using requests library.
* Parses retrieved headers and extracts relevant information.
* Analyzes headers for potential security weaknesses based on best practices.

**Installation:**

You can install phrenology using pip:

```bash
pip install phrenology
```
'''

# Replace with your project information
PROJECT_NAME = "phrenology"
VERSION = "0.1.2"
DESCRIPTION = "A tool for analyzing your security HEADers"
AUTHOR = "SecurityShrimp"
AUTHOR_EMAIL = "securityshrimp@proton.me"
URL = "https://github.com/f8al/phrenology"  # Optional
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
    "pylint"
]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    #license=license,
    packages=find_packages(exclude=("tests*",)),  # Exclude test directories
    install_requires=dependencies,
)
