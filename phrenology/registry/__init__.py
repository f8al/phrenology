import importlib

owasp_header_dictionary = importlib.import_module(
    ".owasp-header-dictionary", package=__name__
)
