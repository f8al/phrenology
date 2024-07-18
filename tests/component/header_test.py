import unittest
from phrenology.component.header import HeaderService

class BaseTestHeaderService(unittest.TestCase):

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


class TestMethodProperty(BaseTestHeaderService):

    def test_when_I_set_the_method_to_POST(self):
        """
        When I set the method to POST,
        the method property should return POST.
        """
        self.service.method = 'POST'
        self.assertEqual(self.service.method, 'POST')


class TestProxyProperty(BaseTestHeaderService):

    def test_when_I_set_a_new_proxy(self):
        """
        When I set a new proxy,
        the proxy property should return the new proxy configuration.
        """
        new_proxy = {'http': 'http://new.proxy:3128'}
        self.service.proxy = new_proxy
        self.assertEqual(self.service.proxy, new_proxy)


class TestParamsProperty(BaseTestHeaderService):

    def test_when_I_set_new_params(self):
        """
        When I set new params,
        the params property should return the new parameters.
        """
        new_params = {'new_key': 'new_value'}
        self.service.params = new_params
        self.assertEqual(self.service.params, new_params)


class TestHeadersProperty(BaseTestHeaderService):

    def test_when_I_set_new_headers(self):
        """
        When I set new headers,
        the headers property should return the new headers.
        """
        new_headers = {'New-Header': 'HeaderValue'}
        self.service.headers = new_headers
        self.assertEqual(self.service.headers, new_headers)


class TestAuthProperty(BaseTestHeaderService):

    def test_when_I_set_new_auth_credentials(self):
        """
        When I set new auth credentials,
        the auth property should return the new credentials.
        """
        new_auth = ('new_user', 'new_pass')
        self.service.auth = new_auth
        self.assertEqual(self.service.auth, new_auth)


class TestTimeoutProperty(BaseTestHeaderService):

    def test_when_I_set_the_timeout_to_10(self):
        """
        When I set the timeout to 10,
        the timeout property should return 10.
        """
        new_timeout = 10
        self.service.timeout = new_timeout
        self.assertEqual(self.service.timeout, new_timeout)


class TestAllowRedirectsProperty(BaseTestHeaderService):

    def test_when_I_allow_redirects(self):
        """
        When I allow redirects,
        the allow_redirects property should return True.
        """
        self.service.allow_redirects = True
        self.assertTrue(self.service.allow_redirects)


class TestVerifyProperty(BaseTestHeaderService):

    def test_when_I_disable_ssl_verification(self):
        """
        When I disable SSL verification,
        the verify property should return False.
        """
        new_verify = False
        self.service.verify = new_verify
        self.assertEqual(self.service.verify, new_verify)


class TestCertProperty(BaseTestHeaderService):

    def test_when_I_set_a_new_cert_path(self):
        """
        When I set a new cert path,
        the cert property should return the new path.
        """
        new_cert = '/new/path/to/certfile'
        self.service.cert = new_cert
        self.assertEqual(self.service.cert, new_cert)


class TestUrlProperty(BaseTestHeaderService):
    """Group of tests for the URL property to check different URL formats."""

    def test_when_I_set_an_http_url(self):
        """
        When I set an HTTP URL,
        the url property should return the HTTP URL.
        """
        new_url = 'http://new-url.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

    def test_when_I_set_an_https_url(self):
        """
        When I set an HTTPS URL,
        the url property should return the HTTPS URL.
        """
        new_url = 'https://secure-url.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

    def test_when_I_set_an_ftp_url(self):
        """
        When I set an FTP URL,
        an exception should be thrown with the message:
        "Invalid URL input: FTP protocol does not return headers."
        """
        new_url = 'ftp://ftp-url.com'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: FTP protocol does not return headers.")

    def test_when_I_set_a_mailto_url(self):
        """
        When I set a mailto URL,
        an exception should be thrown with the message:
        "Invalid URL input: mailto protocol does not return headers."
        """
        new_url = 'mailto:someone@example.com'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: mailto protocol does not return headers.")

    def test_when_I_set_a_file_url(self):
        """
        When I set a file URL,
        an exception should be thrown with the message:
        "Invalid URL input: file protocol does not return headers."
        """
        new_url = 'file:///path/to/file'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: file protocol does not return headers.")

    def test_when_I_set_a_subdomain_url(self):
        """
        When I set a subdomain URL,
        the url property should return the subdomain URL.
        """
        new_url = 'http://subdomain.new-url.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

    def test_when_I_set_a_url_with_path(self):
        """
        When I set a URL with a path and query parameters,
        the url property should return the full URL.
        """
        new_url = 'http://new-url.com/path?query=param'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

if __name__ == '__main__':
    unittest.main()
