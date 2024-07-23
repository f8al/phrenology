#!/bin/env python3
# pylint: disable=wrong-import-position



"""
**************************************************************
*                   package initialization.                  *
**************************************************************
*                                                            *
*   This file is the top-level package initializer for the   *
*   src module. You can perform package-level imports here   *
*   or initialization code if necessary.                     *
**************************************************************
"""

"""
**************************************************************
*                   import section                           *
**************************************************************
*                                                            *
*       Example of importing submodules or specific items    *
*       for easier access:                                   *
*                                                            *
*       from .common.output import OutputClass               *
*       from .registry.headers import HEADERS_SECURITY       *
*       from .main import Main                               *
*                                                            *
**************************************************************
"""

# Importing submodules or specific objects in this section
from . import common
from . import component
from . import registry
from .main import Main

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
*                                                            *
*                                                            *
*                  Example Usage of __all__:                 *
*    ----------------------------------------------------    *
*                      Without __all__                       *
*    ----------------------------------------------------    *
*       src/common/output.py:                                *
*       class OutputClass:                                   *
*           pass                                             *
*       def _private_function():                             *
*            pass                                            *
*                                                            *
*        In another script:                                  *
*        from src.common import *                            *
*        OutputClass is imported                             *
*        output = OutputClass()                              *
*        _private_function is also imported,                 *
*            which is not intended                           *
*        _private_function()                                 *
*                                                            *
*                      With __all__                          *
*    ----------------------------------------------------    *
*        src/common/__init__.py:                             *
*        from .output import OutputClass                     *
*        __all__ = ['OutputClass']                           *
*                                                            *
*        src/common/output.py:                               *
*        class OutputClass:                                  *
*            pass                                            *
*        def _private_function():                            *
*            pass                                            *
*                                                            *
*        In another script:                                  *
*        from src.common import *                            *
*        OutputClass is imported                             *
*        output = OutputClass()                              *
*        _private_function is not                            *
*            imported, which is the intended behavior        *
*        try:                                                *
*            _private_function()                             *
*                # This will raise a NameError               *
*        except NameError:                                   *
*            print("This function is not accessible.")       *
*                                                            *
**************************************************************
"""

# Defining the public interface of this package
__all__ = ['common', 'component', 'registry', 'Main']

# pylint: enable=wrong-import-position
