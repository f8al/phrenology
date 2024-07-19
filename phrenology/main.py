#!/bin/env python3
from .component.header import HeaderService

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

    def engage(self, url, cookie, cache, deprecated, information, get, json):
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
        """
        session = HeaderService(self.service_config)
        session.url = url
        headers_model = session.run_request()
        if headers_model:
            expected_headers = {"result":["success","error"],"items":["X-Frame-Options", "X-Content-Type-Options", "Strict-Transport-Security",
                                "Permissions-Policy", "X-Frame-Options", "Strict-Transport-Security",
                                "Content-Security-Policy", "Cross-Origin-Embedder-Policy", "Cross-Origin-Resource-Policy",
                                "Cross-Origin-Opener-Policy","Referrer-Policy"]}
            
            deprecated_headers = {"result":["warn","success"],"items":["X-XSS-Protection", "Expect-CT", "X-Permitted-Cross-Domain-Policies"]}
            
            information_headers = {"result":["info","info"],"items":["X-Powered-By", "Server", "x-AspNet-Version", "X-AspNetMvc-Version"]}
            cache_headers = {"result":["info","info"],"items":["Cache-Control", "Pragma", "Last-Modified", "Expires", "ETag"]}
          
            self.run('Expected headers',expected_headers, headers_model)
            if(deprecated):
                self.run('Deprecated headers', deprecated_headers, headers_model)
            if(information):
                self.run('Informational headers', information_headers, headers_model)
            if(cache):
                self.run('Cacheing headers', cache_headers, headers_model)
        else:
            self._output = {
                "type": "error",
                "message": "Failed to retrieve headers."
            }

    def run(self, name, headers, headers_model):
        """
        Processes and outputs header data based on the provided name, headers configuration, and headers model.

        This method is likely called internally by engage() for each type of header (expected, deprecated, etc.).

        Args:
            name (str): The name of the header category (e.g., "Expected Headers").
            headers (dict): A dictionary containing configuration for the header category (e.g., result type, expected items).
            headers_model (object): An instance of the HeaderService model containing retrieved headers data.

        # Logic for processing and rendering header types block remains unchanged
        """


        query_result = headers_model.query(headers["items"])
        # render header types block

        self.output.render_output('counts', name, headers["result"], query_result["counts"])
        self.output.render_output('list', name, headers["result"], {
            "expected": headers_model.expected,
            "missing": headers_model.missing,
            "present": headers_model.present
        })
        #self.output.render_output('read', name, headers["result"], {
        #    'Content-Type': headers_model.read('Content-Type')
        #})