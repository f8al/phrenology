import unittest
from phrenology.component import Header

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
        self.service = Header.Service(config=self.config)
        # self.service.url = 'http://example.com'


class TestMethodProperty(BaseTestHeaderService):

    def test_when_I_set_the_method_to_a_valid_HTTP_method(self):
        """
        When I set the method to a valid HTTP method,
        the method property should return the respective method.
        """
        valid_methods = ['GET', 'HEAD', 'OPTIONS','get', 'head', 'options']
        for method in valid_methods:
            with self.subTest(method=method):
                self.service.method = method
                self.assertEqual(self.service.method, method.upper())

    def test_when_I_set_the_method_to_a_valid_but_unsupported_HTTP_method(self):
        """
        When I set the method to a valid but unsupported HTTP method,
        the method property should return the respective method.
        """
        valid_methods = ['POST', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'CONNECT']
        for method in valid_methods:
            with self.subTest(method=method):
                with self.assertRaises(ValueError) as context:
                    self.service.method = method
                self.assertEqual(str(context.exception), "Invalid method input: your method is not currently supported please use GET HEAD or OPTIONS")

    def test_when_I_set_the_method_to_an_ivalid_HTTP_method(self):
        """
        When I set the method to a invalid HTTP method,
        the method property should return the respective method.
        """
        invalid_methods = ['bob', '123', 'stuff', 'none']
        for method in invalid_methods:
            with self.subTest(method=method):
                with self.assertRaises(ValueError) as context:
                    self.service.method = method
                self.assertEqual(str(context.exception), "Invalid method input: your method is invalid please use GET HEAD or OPTIONS")


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

    def test_when_I_try_to_set_headers_that_are_not_headers(self):
        """
        When I try to set headers that are not headers,
        the method property should throw the error:
        """
        invalid_headers = ['bob', '123', {'stuff':'13266', 'a':{'b':'c'}}, 'none']
        for headers in invalid_headers:
            with self.subTest(headers=headers):
                with self.assertRaises(ValueError) as context:
                    self.service.headers = headers
                self.assertEqual(str(context.exception), "Invalid headers input: input provided was malformed")


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
        test_values = [False, 'false', 'False', 'f', 'F', 0]
        for value in test_values:
            with self.subTest(value=value):
                self.service.verify = value
                self.assertEqual(self.service.verify, False)
                
    def test_when_I_set_invalid_ssl_verification(self):
        """
        When I set an invalid value for SSL verification,
        an exception should be raised.
        """
        invalid_values = ['invalid', 'yes', 'nope', 123, {}, []]
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as context:
                    self.service.verify = value
                self.assertEqual(str(context.exception), "Invalid value for SSL verification: must be a boolean or string/int representation of boolean.")

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
    
    def test_when_I_set_an_IP_url_badly(self):
        """
        When I set an IP URL badly,
        the url property should return the HTTP URL.
        """
        new_url = 'http://192.168'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: dude seriously?")


    def test_when_I_set_an_IP_url(self):
        """
        When I set an IP URL,
        the url property should return the HTTP URL.
        """
        new_url = 'http://192.168.1.1'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)
    
    def test_when_I_set_an_IP_url_with_a_port(self):
        """
        When I set an IP URL with a port,
        the url property should return the HTTP URL.
        """
        new_url = 'http://192.168.1.1:23656'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

    def test_when_I_set_an_http_url(self):
        """
        When I set an HTTP URL,
        the url property should return the HTTP URL.
        """
        new_url = 'http://new-url.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, new_url)

    def test_when_I_set_a_valid_http_url_with_numbers(self):
        """
        When I set a valid HTTP URL with numbers,
        the url property should return the HTTP URL.
        """
        wellformed_urls = [
            'https://192.com',
            'https://192.amazon.com',
            'https://192.168.1.1.com',
            'https://257.168.1.1.com',
            'http://192.com?query=param',
            'https://182.com/124/'
        ]
        for new_url in wellformed_urls:
            with self.subTest(new_url=new_url):
                self.service.url = new_url
                self.assertEqual(self.service.url, new_url)

    def test_when_I_set_an_http_url_badly_with_characters(self):
        """
        When I set an http URL badly,
        the url property should return the HTTP URL.
        """
        new_url = 'http://new-ur&l.com'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: character, dude seriously?")

    def test_when_I_set_an_http_url_badly_with_numbers(self):
        """
        When I set an http URL badly,
        the url property should return the HTTP URL.
        """
        new_url = 'http://new-url.192'
        with self.assertRaises(ValueError) as context:
            self.service.url = new_url
        self.assertEqual(str(context.exception), "Invalid URL input: numbers, dude seriously?")

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
        self.assertEqual(str(context.exception), "Invalid URL input: ftp:// protocol does not return headers.")

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
        self.assertEqual(str(context.exception), "Invalid URL input: file:// protocol does not return headers.")

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

    def test_when_I_set_a_fqdn(self):
        """
        When I set a valid FQDN without a protocol,
        the url property should return the URL with https:// prepended.
        """
        new_url = 'digitalminion.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, 'https://digitalminion.com')

    def test_when_I_set_a_fqdn_with_subdomain(self):
        """
        When I set a valid FQDN with subdomain(s) but without a protocol,
        the url property should return the URL with https:// prepended.
        """
        new_url = 'aws.cloud.digitalminion.com'
        self.service.url = new_url
        self.assertEqual(self.service.url, 'https://aws.cloud.digitalminion.com')
    
    def test_when_I_miss_position_a_dot_on_the_fqdn(self):
        """
        When I miss position a dot on the fqdn,
        an exception should be thrown with the message:
        Invalid URL input: your url is malformed please check it and try again.
        """
        malformed_urls = [
            'https://.digitalminion.com',
            'https://digitalminion.com.',
            'http://new-url.com.?query=param',
            'https://192.168.1.1.'
        ]
        for new_url in malformed_urls:
            with self.subTest(new_url=new_url):
                with self.assertRaises(ValueError) as context:
                    self.service.url = new_url
                self.assertEqual(str(context.exception), "Invalid URL input: your url is malformed please check it and try again.")

        def test_when_I_set_a_url_with_unicode_characters(self):
            """
            When I set a URL with Unicode characters,
            the url property should return the correctly formatted URL.
            """
            new_url = 'http://example.com/测试'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)
        
        def test_when_I_set_a_url_with_user_info(self):
            """
            When I set a URL with user info,
            the url property should return the URL with user info preserved.
            """
            new_url = 'http://user:pass@example.com'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)
        
        def test_when_I_set_a_url_with_fragment(self):
            """
            When I set a URL with a fragment,
            the url property should return the full URL including the fragment.
            """
            new_url = 'http://example.com/path#section'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        def test_when_I_set_a_url_with_port_and_path(self):
            """
            When I set a URL with a port and path,
            the url property should return the full URL including the port and path.
            """
            new_url = 'http://example.com:8080/path'
            self.service.url = new_url
            self.assertEqual(self.service.url, new_url)

        def test_when_I_set_a_url_with_only_path_and_query(self):
            """
            When I set a URL with only a path and query,
            the url property should return the full URL with https:// prepended.
            """
            new_url = 'example.com/path?query=param'
            self.service.url = new_url
            self.assertEqual(self.service.url, 'https://example.com/path?query=param')

        def test_when_I_set_an_IP_url_with_invalid_octet(self):
            """
            When I set an IP URL with an invalid octet,
            an exception should be thrown with the message:
            Invalid URL input: dude seriously?
            """
            new_url = 'http://256.256.256.256'
            with self.assertRaises(ValueError) as context:
                self.service.url = new_url
            self.assertEqual(str(context.exception), "Invalid URL input: dude seriously?")

if __name__ == '__main__':
    unittest.main()
