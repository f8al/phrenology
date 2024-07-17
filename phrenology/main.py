#!/bin/env python3
from .component.header import HeaderService

class Main:
    def __init__(self):
        self.service_config = {
            "method": "GET",
            "allow_redirects": False
        }
        self._output = None

    @property
    def output(self):
        return self._output

    def engage(self, url):
        """
        Engages the header checking process and maps output to objects.

        Args:
            url (str): The URL to check headers.
        """
        session = HeaderService(self.service_config)
        headers_model = session.run_request(url)
        if headers_model:
            expected_headers = ["Content-Type", "Cache-Control", "X-Frame-Options", "Strict-Transport-Security", "Content-Security-Policy"]
            query_result = headers_model.query(expected_headers)

            self._output = self.count(query_result)
            self._output = self.list(headers_model)
            self._output = self.read(headers_model, 'Content-Type')
        else:
            self._output = {
                "type": "error",
                "message": "Failed to retrieve headers."
            }

    def count(self, query_result):
        """
        Maps the query result to an output object.

        Args:
            query_result (dict): The query result from HeaderModel.

        Returns:
            dict: The output object.
        """
        return {
            "type": "counts",
            "payload": {
                "counts": query_result["counts"]
            }
        }

    def list(self, headers_model):
        """
        Maps the headers model to a list output object.

        Args:
            headers_model (HeaderModel): The headers model.

        Returns:
            dict: The output object.
        """
        return {
            "type": "list",
            "payload": {
                "does_exist": headers_model.does_exist,
                "not_exist": headers_model.not_exist,
                "more_exist": headers_model.more_exist
            }
        }

    def read(self, headers_model, header_name):
        """
        Maps a single header read to an output object.

        Args:
            headers_model (HeaderModel): The headers model.
            header_name (str): The header to read.

        Returns:
            dict: The output object.
        """
        header_value = headers_model.read(header_name)
        return {
            "type": "read",
            "payload": {
                header_name: header_value
            }
        }
