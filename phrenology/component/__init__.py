#!/bin/env python3
# pylint: disable=wrong-import-position
"""
**************************************************************
*           src.component package initialization.            *
**************************************************************
*                                                            *
*   This file initializes the component subpackage and makes *
*   its contents accessible from the component package level.*
**************************************************************
"""

"""
**************************************************************
*                   import section                           *
**************************************************************
*                                                            *
*       Importing classes to include in the Header namespace:*
*                                                            *
*       from .header import HeaderModel                      *
*       from .header import HeaderService                    *
*                                                            *
**************************************************************
"""

# Importing classes to include in the Header namespace
from .header import HeaderModel
from .header import HeaderService

"""
**************************************************************
*                  namespace creation                        *
**************************************************************
*                                                            *
*    Dynamically creating a namespace for Header classes.    *
**************************************************************
"""

# Creating a namespace for Header classes
class _Namespace:
    pass

Header = _Namespace()
Header.Model = HeaderModel
Header.Service = HeaderService

"""
**************************************************************
*                   export section                           *
**************************************************************
*              Understanding __all__ in python:              *
*    ----------------------------------------------------    *
*       __all__ is a list of strings defining what is        *
*       considered "public" in this package. When you        *
*       use 'from package import *', only the names          *
*       included in __all__ are imported. This helps to      *
*       control the namespace and prevent the exposure of    *
*       internal components that are not meant to be used    *
*       directly by users of the module or package.          *
**************************************************************
"""

# Defining the public interface of this package
__all__ = ['Header']

# Clean up the module namespace
del _Namespace, HeaderModel, HeaderService

# pylint: enable=wrong-import-position
