import unittest
from phrenology.component.header import HeaderService

class TestHeaderService(unittest.TestCase):

    def setUp(self):
        self.config = {
            'method': 'GET',
            'proxy': {
                'http': 'http://10.10.1.10:3128',
                'https': 'http://10.10.1.10:1080'
            },
            'params': {'key1': 'value1', 'key2': 'value2'},
            'headers': {'User-Agent': 'my-app', 'Accept': 'application/json'},
            'auth': ('user', 'pass'),
            'timeout': 5,
            'allow_redirects': False,
            'verify': True,
            'cert': '/path/to/certfile'
        }
        self.service = HeaderService(config=self.config)
        self.service.url = 'http://example.com'

    def test_property_method(self):
        """
        When I set the method to POST,
        the method property should return POST.
        """
        def when_I_set_the_method_to_POST():
            self.service.method = 'POST'
            self.assertEqual(self.service.method, 'POST')

        when_I_set_the_method_to_POST()

    def test_property_proxy(self):
        """
        When I set a new proxy,
        the proxy property should return the new proxy configuration.
        """
        def when_I_set_a_new_proxy():
            new_proxy = {'http': 'http://new.proxy:3128'}
            self.service.proxy = new_proxy
            self.assertEqual(self.service.proxy, new_proxy)

        when_I_set_a_new_proxy()

    def test_property_params(self):
        """
        When I set new params,
        the params property should return the new parameters.
        """
        def when_I_set_new_params():
            new_params = {'new_key': 'new_value'}
            self.service.params = new_params
            self.assertEqual(self.service.params, new_params)

        when_I_set_new_params()

    def test_property_headers(self):
        """
        When I set new headers,
        the headers property should return the new headers.
        """
        def when_I_set_new_headers():
            new_headers = {'New-Header': 'HeaderValue'}
            self.service.headers = new_headers
            self.assertEqual(self.service.headers, new_headers)

        when_I_set_new_headers()

    def test_property_auth(self):
        """
        When I set new auth credentials,
        the auth property should return the new credentials.
        """
        def when_I_set_new_auth_credentials():
            new_auth = ('new_user', 'new_pass')
            self.service.auth = new_auth
            self.assertEqual(self.service.auth, new_auth)

        when_I_set_new_auth_credentials()

    def test_property_timeout(self):
        """
        When I set the timeout to 10,
        the timeout property should return 10.
        """
        def when_I_set_the_timeout_to_10():
            new_timeout = 10
            self.service.timeout = new_timeout
            self.assertEqual(self.service.timeout, new_timeout)

        when_I_set_the_timeout_to_10()

    def test_property_allow_redirects(self):
        """
        When I allow redirects,
        the allow_redirects property should return True.
        """
        def when_I_allow_redirects():
            self.service.allow_redirects = True
            self.assertTrue(self.service.allow_redirects)

        when_I_allow_redirects()

    def test_property_verify(self):
        """
        When I disable SSL verification,
        the verify property should return False.
        """
        def when_I_disable_ssl_verification():
            new_verify = False
            self.service.verify = new_verify
            self.assertEqual(self.service.verify, new_verify)

        when_I_disable_ssl_verification()

    def test_property_cert(self):
        """
        When I set a new cert path,
        the cert property should return the new path.
        """
        def when_I_set_a_new_cert_path():
            new_cert = '/new/path/to/certfile'
            self.service.cert = new_cert
            self.assertEqual(self.service.cert, new_cert)

        when_I_set_a_new_cert_path()

    def test_property_url(self):
        """Group of tests for the URL property to check different URL formats."""

        def when_I_set_an_http_url():
            """
            When I set an HTTP URL,
            the url property should return the HTTP URL.
            """
            new_url = 'http://new-url.com'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        def when_I_set_an_https_url():
            """
            When I set an HTTPS URL,
            the url property should return the HTTPS URL.
            """
            new_url = 'https://secure-url.com'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        def when_I_set_an_ftp_url():
            """
            When I set an FTP URL,
            an exception should be thrown with the message:
            "Invalid URL input: FTP protocol does not return headers."
            """
            new_url = 'ftp://ftp-url.com'
            with self.assertRaises(ValueError) as context:
                self.service.url = new_url
            self.assertEqual(str(context.exception), "Invalid URL input: FTP protocol does not return headers.")

        def when_I_set_a_mailto_url():
            """
            When I set a mailto URL,
            an exception should be thrown with the message:
            "Invalid URL input: mailto protocol does not return headers."
            """
            new_url = 'mailto:someone@example.com'
            with self.assertRaises(ValueError) as context:
                self.service.url = new_url
            self.assertEqual(str(context.exception), "Invalid URL input: mailto protocol does not return headers.")

        def when_I_set_a_file_url():
            """
            When I set a file URL,
            an exception should be thrown with the message:
            "Invalid URL input: file protocol does not return headers."
            """
            new_url = 'file:///path/to/file'
            with self.assertRaises(ValueError) as context:
                self.service.url = new_url
            self.assertEqual(str(context.exception), "Invalid URL input: file protocol does not return headers.")

        def when_I_set_a_subdomain_url():
            """
            When I set a subdomain URL,
            the url property should return the subdomain URL.
            """
            new_url = 'http://subdomain.new-url.com'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        def when_I_set_a_url_with_path():
            """
            When I set a URL with a path and query parameters,
            the url property should return the full URL.
            """
            new_url = 'http://new-url.com/path?query=param'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        # Run all the URL tests
        when_I_set_an_http_url()
        when_I_set_an_https_url()
        when_I_set_an_ftp_url()
        when_I_set_a_subdomain_url()
        when_I_set_a_url_with_path()

if __name__ == '__main__':
    unittest.main()
