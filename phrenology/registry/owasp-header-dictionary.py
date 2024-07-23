#!/bin/env python3

# pylint: disable=line-too-long
expected_security_responses = {
    'X-Frame-Options':'DENY', # no longer best practice. Use Content Security Policy (CSP) frame-ancestors directive if possible.
    'X-Content-Type-Options':'nosniff', # Set the Content-Type header correctly throughout the site. nosniff blocks MIME type sniffing
    'Referrer-Policy':'strict-origin-when-cross-origin', # Referrer policy has been supported by browsers since 2014. Today, the default behavior in modern browsers is to no longer send all referrer information (origin, path, and query string) to the same site but to only send the origin to other sites. However, since not all users may be using the latest browsers we suggest forcing this behavior by sending this header on all responses.
    'Content-Type':'text/html; charset=UTF-8', #The Content-Type representation header is used to indicate the original media type of the resource (before any content encoding is applied for sending). If not set correctly, the resource (e.g. an image) may be interpreted as HTML, making XSS vulnerabilities possible. charset attribute is necessary to prevent XSS in HTML pages
    'Set-Cookie':'Secure, HttpOnly, SameSite', # The Set-Cookie HTTP response header is used to send a cookie from the server to the user agent, so the user agent can send it back to the server later. To send multiple cookies, multiple Set-Cookie headers should be sent in the same response.
    'Strict-Transport-Security':'max-age=63072000; includeSubDomains; preload', # The HTTP Strict-Transport-Security response header (often abbreviated as HSTS) lets a website tell browsers that it should only be accessed using HTTPS, instead of using HTTP.
    'Access-Control-Allow-Origin':'https://yoursite.com', # The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin.
    'Cross-Origin-Opener-Policy':'same-origin', # Isolates the browsing context exclusively to same-origin documents.
    'Cross-Origin-Embedder-Policy':'require-corp', # A document can only load resources from the same origin, or resources explicitly marked as loadable from another origin.
    'Cross-Origin-Resource-Policy': 'same-site', # Limit current resource loading to the site and sub-domains only.
    'Permissions-Policy':'geolocation=(), camera=(), microphone=()', # Set it and disable all the features that your site does not need or allow them only to the authorized domains
    'Permissions-Policy': 'interest-cohort=()', # related to FLoC, A site can declare that it does not want to be included in the user's list of sites for cohort calculation by sending this HTTP header.
    'X-DNS-Prefetch-Control': 'off', #The default behavior of browsers is to perform DNS caching which is good for most websites. If you do not control links on your website, you might want to set off as a value to disable DNS prefetch to avoid leaking information to those domains. Do not rely in this functionality for anything production sensitive: it is not standard or fully supported and implementation may vary among browsers.
    '':'', #
}

bad_security_headers = {
    'Expect-CT':'report-uri="<uri>", enforce, max-age=<age>', # The Expect-CT header lets sites opt in to reporting and/or enforcement of Certificate Transparency requirements. Certificate Transparency (CT) aims to prevent the use of misissued certificates for that site from going unnoticed.
    'X-XSS-PROTECTION':'0', # no longer used, Use a Content Security Policy (CSP) that disables the use of inline JavaScript instead
    'X-Powered-By':'*', # OWASP recommends Remove all X-Powered-By headers.
    'X-AspNet-Version':'*', # Provides information on the .NET version, OWASP recommends disabling this header
    'X-AspNetMvc-Version':'*', # Provides information on the .NET version, OWASP recommends disabling this header
    'Public-Key-Pins':'' # deprecated and should no longer be used
    }

potentially_interesting_headers = {
    'Server':'webserver' # Remove this header or set non-informative values.
    }
# pylint: enable=line-too-long
