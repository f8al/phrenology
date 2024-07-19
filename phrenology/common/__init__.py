#!/bin/env python3

"""
**************************************************************
*             src.common package initialization.             *
**************************************************************
*                                                            *
*   This file initializes the common subpackage and makes    *
*   its contents accessible from the common package level.   *
**************************************************************
"""

"""
**************************************************************
*                   import section                           *
**************************************************************
*                                                            *
*       Importing classes to include in the Output namespace:*
*                                                            *
*       from .output import Output                           *
*       from .output_template import OutputTemplate          *
*                                                            *
**************************************************************
"""

# Importing classes to include in the Output namespace
from .output import OutputAbstract
from .output_template import OutputTemplate


"""
**************************************************************
*                  namespace creation                        *
**************************************************************
*                                                            *
*    Dynamically creating a namespace for classes.           *
**************************************************************
"""

# Creating a namespace for Output classes
class _Namespace:
    pass

output = _Namespace()
output.Abstract = OutputAbstract
output.Template = OutputTemplate

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
__all__ = ['output']


#**************************************************************
# Clean up the module namespace
del _Namespace, Output, OutputTemplate
