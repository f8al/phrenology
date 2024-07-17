#!/bin/env python3
from .component.header import HeaderService

class Main:
    def __init__(self, output, config):
        # output here represents the output abstract class implemented in common.output.py
        self.output = output
        self.service_config = config

    def engage(self, url):
        """
        Engages the header checking process and maps output to objects.

        Args:
            url (str): The URL to check headers.
        """
        session = HeaderService(self.service_config)
        headers_model = session.run_request(url)
        if headers_model:
            expected_headers = ["X-Frame-Options", "X-Content-Type-Options", "Strict-Transport-Security",
                                "Permissions-Policy", "X-Frame-Options", "Strict-Transport-Security",
                                "Content-Security-Policy", "Cross-Origin-Embedder-Policy", "Cross-Origin-Resource-Policy",
                                "Cross-Origin-Opener-Policy","Referrer-Policy"]
            
            deprecated_headers = ["X-XSS-Protection", "Expect-CT", "X-Permitted-Cross-Domain-Policies"]
            
            information_headers = ["X-Powered-By", "Server", "x-AspNet-Version", "X-AspNetMvc-Version"]
            cache_headers = ["Cache-Control", "Pragma", "Last-Modified", "Expires", "ETag"]
            query_result = headers_model.query(expected_headers)

            self.output.render_output('counts', query_result["counts"])
            self.output.render_output('list', {
                "does_exist": headers_model.does_exist,
                "not_exist": headers_model.not_exist,
                "more_exist": headers_model.more_exist
            })
            self.output.render_output('read', {
                'Content-Type': headers_model.read('Content-Type')
            })
        else:
            self._output = {
                "type": "error",
                "message": "Failed to retrieve headers."
            }
