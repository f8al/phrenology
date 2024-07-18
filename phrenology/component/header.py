import requests
import re
from requests.exceptions import HTTPError, Timeout, RequestException


class HeaderModel:
    """
    A model for handling HTTP headers.

    This class is designed to store and manipulate HTTP headers
    retrieved from an HTTP response. It provides methods to read
    individual headers and query expected headers to determine
    which ones exist, do not exist, and which additional headers
    are present.

    Attributes:
        _headers (dict): The dictionary of headers.
        expected (dict): Headers that are expected and exist.
        missing (dict): Headers that are expected but do not exist.
        present (dict): Headers that are not expected but exist.
    """

    def __init__(self, headers_dict):
        """
        Initializes the HeaderModel with a dictionary of headers.

        Args:
            headers_dict (dict): The dictionary of HTTP headers.
        """
        self._headers = headers_dict
        self.expected = {}
        self.missing = {}
        self.present = {}

    def read(self, item):
        """
        Reads the value of a specified header.

        Args:
            item (str): The header to retrieve.

        Returns:
            str: The value of the specified header, or None if not found.
        """
        return self._headers.get(item)

    def query(self, expected):
        """
        Queries the headers to check for expected headers and categorize them.

        Args:
            expected (list): A list of headers expected to be in the response.

        Returns:
            dict: A dictionary containing the counts of existing, non-existing,
                  and additional headers.
        """
        self.expected = {}
        self.missing = {}
        self.present = {}

        for key in expected:
            if key in self._headers:
                self.expected[key] = self._headers[key]
            else:
                self.missing[key] = None

        for key in self._headers:
            if key not in expected:
                self.present[key] = self._headers[key]

        counts = {
            "counts": {
                "expected": len(self.expected),
                "missing": len(self.missing),
                "present": len(self.present)
            }
        }

        return counts

class HeaderService:
    """
    A service for making HTTP requests and handling headers.

    This class is designed to facilitate making HTTP requests
    and processing the headers from the responses. It uses getters
    and setters to simplify interacting with various request
    parameters while abstracting operations that may be needed
    to make things work correctly.

    Attributes:
        _method (str): The HTTP method to use for the request.
        _config (dict): Configuration parameters for the request.
        session (requests.Session): The requests session used to make HTTP requests.
    """

    def __init__(self, config=None):
        """
        Initializes the HeaderService with a configuration dictionary.

        Args:
            config (dict): A dictionary containing configuration parameters.
                           Must include the 'method' key.

        Raises:
            ValueError: If 'method' is not included in the configuration.
        """
        self._method = ""
        self._url =""
        self._config = {}
        try:
            if config:
                self.config = config
            if 'method' not in config:
                raise ValueError("Configuration must include 'method'.")
        except Exception as e:
            raise ValueError(f"Invalid configuration: {e}")
        self.session = requests.Session()

    @property
    def config(self):
        """
        Returns a copy of the configuration dictionary.

        Returns:
            dict: A copy of the configuration dictionary.
        """
        return self._config.copy()

    @config.setter
    def config(self, value):
        """
        Sets the configuration dictionary and updates the session.

        Args:
            value (dict): The configuration dictionary.
        """
        for key, val in value.items():
            setter_name = f'{key}'
            if hasattr(self, setter_name):
                setattr(self, setter_name, val)
            else:
                self._config[key] = val

    @property
    def method(self):
        """
        Gets the HTTP method for the request.

        Returns:
            str: The HTTP method.
        """
        return self._method

    @method.setter
    def method(self, value):
        """
        Sets the HTTP method for the request.

        Args:
            value (str): The HTTP method.

        Example:
            >>> service.method = "GET"
        """
        self._method = value

    @property
    def proxy(self):
        """
        Gets the proxy configuration for the session.

        Returns:
            dict: The proxy configuration.

        Example:
            >>> service.proxy = {
            ...     "http": "http://10.10.1.10:3128",
            ...     "https": "http://10.10.1.10:1080"
            ... }
        """
        return self._config.get('proxy')

    @proxy.setter
    def proxy(self, value):
        """
        Sets the proxy configuration for the session.

        Args:
            value (dict): The proxy configuration.

        Example:
            >>> service.proxy = {
            ...     "http": "http://10.10.1.10:3128",
            ...     "https": "http://10.10.1.10:1080"
            ... }
        """
        self._config['proxy'] = value
        self.session.proxies.update(value)

    @property
    def params(self):
        """
        Gets the query parameters for the request.

        Returns:
            dict: The query parameters.

        Example:
            >>> service.params = {"key1": "value1", "key2": "value2"}
        """
        return self._config.get('params')

    @params.setter
    def params(self, value):
        """
        Sets the query parameters for the request.

        Args:
            value (dict): The query parameters.

        Example:
            >>> service.params = {"key1": "value1", "key2": "value2"}
        """
        self._config['params'] = value

    @property
    def headers(self):
        """
        Gets the headers for the request.

        Returns:
            dict: The headers.

        Example:
            >>> service.headers = {
            ...     "User-Agent": "my-app",
            ...     "Accept": "application/json"
            ... }
        """
        return self._config.get('headers')

    @headers.setter
    def headers(self, value):
        """
        Sets the headers for the request.

        Args:
            value (dict): The headers.

        Example:
            >>> service.headers = {
            ...     "User-Agent": "my-app",
            ...     "Accept": "application/json"
            ... }
        """
        self._config['headers'] = value

    @property
    def auth(self):
        """
        Gets the authentication credentials for the request.

        Returns:
            tuple: The authentication credentials (username, password).

        Example:
            >>> service.auth = ("user", "pass")
        """
        return self._config.get('auth')

    @auth.setter
    def auth(self, value):
        """
        Sets the authentication credentials for the request.

        Args:
            value (tuple): The authentication credentials (username, password).

        Example:
            >>> service.auth = ("user", "pass")
        """
        self._config['auth'] = value

    @property
    def timeout(self):
        """
        Gets the timeout for the request.

        Returns:
            int or float: The timeout value in seconds.

        Example:
            >>> service.timeout = 5
        """
        return self._config.get('timeout')

    @timeout.setter
    def timeout(self, value):
        """
        Sets the timeout for the request.

        Args:
            value (int or float): The timeout value in seconds.

        Example:
            >>> service.timeout = 5
        """
        self._config['timeout'] = value

    @property
    def allow_redirects(self):
        """
        Gets the flag indicating whether redirects are allowed.

        Returns:
            bool: True if redirects are allowed, False otherwise.

        Example:
            >>> service.allow_redirects = False
        """
        return self._config.get('allow_redirects', True)

    @allow_redirects.setter
    def allow_redirects(self, value):
        """
        Sets the flag indicating whether redirects are allowed.

        Args:
            value (bool): True if redirects are allowed, False otherwise.

        Example:
            >>> service.allow_redirects = False
        """
        self._config['allow_redirects'] = value

    @property
    def verify(self):
        """
        Gets the SSL verification setting.

        Returns:
            bool or str: True if SSL verification is enabled, False otherwise, or a path to a CA_BUNDLE file.

        Example:
            >>> service.verify = True
            >>> service.verify = "/path/to/certfile"
        """
        return self._config.get('verify')

    @verify.setter
    def verify(self, value):
        """
        Sets the SSL verification setting.

        Args:
            value (bool or str): True to enable SSL verification, False to disable, or a path to a CA_BUNDLE file.

        Example:
            >>> service.verify = True
            >>> service.verify = "/path/to/certfile"
        """
        self._config['verify'] = value

    @property
    def cert(self):
        """
        Gets the SSL certificate configuration.

        Returns:
            str or tuple: The path to the SSL certificate file, or a tuple containing the path to the certificate file and the path to the key file.

        Example:
            >>> service.cert = "/path/to/certfile"
            >>> service.cert = ("/path/client.cert", "/path/client.key")
        """
        return self._config.get('cert')

    @cert.setter
    def cert(self, value):
        """
        Sets the SSL certificate configuration.

        Args:
            value (str or tuple): The path to the SSL certificate file, or a tuple containing the path to the certificate file and the path to the key file.

        Example:
            >>> service.cert = "/path/to/certfile"
            >>> service.cert = ("/path/client.cert", "/path/client.key")
        """
        self._config['cert'] = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        url_regex = r"^[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#\[\]@!$&'()*+,;=.]+$"
        if not re.match(url_regex, value):
            # Check if it starts with http or https
            if not value.startswith(('http://', 'https://')):
                value = f"https://{value}"
            # Re-check with updated value
            if not re.match(url_regex, value):
                raise ValueError("Invalid URL format")
        self._url = value
        
    
    def _handle_response(self, response):
        """
        Handles the HTTP response, raising errors for bad responses.

        Args:
            response (requests.Response): The HTTP response.

        Raises:
            RuntimeError: If the response contains an HTTP error, timeout, or request exception.
        """
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            raise RuntimeError(f'HTTP error occurred: {http_err}')
        except Timeout as timeout_err:
            raise RuntimeError(f'Timeout error occurred: {timeout_err}')
        except RequestException as req_err:
            raise RuntimeError(f'Error occurred: {req_err}')

    def _handle_headers(self, response):
        """
        Isolates the headers from the response and creates a HeaderModel.

        Args:
            response (requests.Response): The HTTP response.

        Returns:
            HeaderModel: The model containing the response headers.
        """
        headers_dict = dict(response.headers)
        return HeaderModel(headers_dict)

    def run_request(self):
        """
        Executes the HTTP request and processes the response headers.

        Args:
            url (str): The URL to send the request to.

        Returns:
            HeaderModel: The model containing the response headers.

        Raises:
            RuntimeError: If an error occurs during the request.
        """
        config = self.config
        try:
            response = self.session.request(self.method, self.url, **config)
            self._handle_response(response)
            response_headers = self._handle_headers(response)
            return response_headers
        except RequestException as e:
            raise RuntimeError(f'An error occurred: {e}')



