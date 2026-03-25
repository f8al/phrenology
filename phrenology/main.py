#!/bin/env python3
from .component.header import HeaderService
from .registry import owasp_header_dictionary as owasp
from .registry.headers import (
    EXPECTED_HEADERS,
    DEPRECATED_HEADERS,
    INFORMATION_HEADERS,
    CACHE_HEADERS,
)


class Main:
    """
    The main class responsible for initiating the header checking process and presenting the results.

    Attributes:
        output (object): An instance of an output class used for rendering the results (likely from common.output.py)
        service_config (dict): A dictionary containing configuration options for the header checking service.
    """

    def __init__(self, output, config):
        # output here represents the output abstract class implemented in common.output.py
        self.output = output
        self.service_config = config

    def engage(self, url, cookie, cache, deprecated, information, get, json, owasp_guidance=False):
        """
        Initiates the process of checking headers for a provided URL and generates output based on user preferences.

        Args:
            url (str): The URL to check headers for.
            cookie (str, optional): A custom cookie to include in the request. Defaults to None.
            cache (bool, optional): Flag indicating whether to display cache headers in the output. Defaults to False.
            deprecated (bool, optional): Flag indicating whether to display deprecated headers in the output. Defaults to False.
            information (bool, optional): Flag indicating whether to display informational headers in the output. Defaults to False.
            get (bool, optional): Flag indicating whether to use the GET request method instead of HEAD (default). Defaults to False.
            json (bool, optional): Flag indicating whether to output the results in JSON format. Defaults to False.
            owasp_guidance (bool, optional): Flag indicating whether to display OWASP guidance for each header. Defaults to False.
        """
        session = HeaderService(self.service_config)

        if get:
            session.method = "GET"

        if cookie:
            session.headers = {"Cookie": cookie}

        session.url = url
        headers_model = session.run_request()

        # Build combined OWASP lookup when guidance is requested
        owasp_lookup = {}
        if owasp_guidance:
            owasp_lookup.update(owasp.expected_security_responses)
            owasp_lookup.update(owasp.bad_security_headers)
            owasp_lookup.update(owasp.potentially_interesting_headers)

        if headers_model:
            self.run("Expected headers", session.url, EXPECTED_HEADERS, headers_model, owasp_lookup, show_present=True)
            if deprecated:
                self.run(
                    "Deprecated headers", session.url, DEPRECATED_HEADERS, headers_model, owasp_lookup
                )
            if information:
                self.run(
                    "Informational headers",
                    session.url,
                    INFORMATION_HEADERS,
                    headers_model,
                    owasp_lookup,
                )
            if cache:
                self.run("Cacheing headers", session.url, CACHE_HEADERS, headers_model, owasp_lookup)
        else:
            self._output = {"type": "error", "message": "Failed to retrieve headers."}

    def run(self, name, url, headers, headers_model, owasp_lookup=None, show_present=False):
        """
        Processes and outputs header data based on the provided name, headers configuration, and headers model.

        This method is likely called internally by engage() for each type of header (expected, deprecated, etc.).

        Args:
            name (str): The name of the header category (e.g., "Expected Headers").
            headers (dict): A dictionary containing configuration for the header category (e.g., result type, expected items).
            headers_model (object): An instance of the HeaderService model containing retrieved headers data.
            owasp_lookup (dict): OWASP guidance lookup, or None/empty if not requested.
            show_present (bool): Whether to include non-queried headers in the output. Defaults to False.

        # Logic for processing and rendering header types block remains unchanged
        """

        query_result = headers_model.query(headers["items"])
        # render header types block

        self.output.render_output(
            "counts", name, url, headers["result"], query_result["counts"]
        )
        self.output.render_output(
            "list",
            name,
            url,
            headers["result"],
            {
                "expected": headers_model.expected,
                "missing": headers_model.missing,
                "present": headers_model.present if show_present else {},
                "owasp": owasp_lookup or {},
            },
        )
