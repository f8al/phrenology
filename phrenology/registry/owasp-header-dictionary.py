#!/bin/env python3

expected_security_responses = {
    "X-Frame-Options": {
        "recommended": "deny",
        "guidance": "Prevents framing of the page. Superseded by CSP frame-ancestors directive but still recommended for backwards compatibility.",
    },
    "X-Content-Type-Options": {
        "recommended": "nosniff",
        "guidance": "Set the Content-Type header correctly throughout the site. nosniff blocks MIME type sniffing.",
    },
    "Referrer-Policy": {
        "recommended": "no-referrer",
        "guidance": "OWASP Secure Headers Project recommends no-referrer as the strictest option. Prevents sending any referrer information with requests. The OWASP Cheat Sheet suggests strict-origin-when-cross-origin as a less restrictive alternative.",
    },
    "Content-Type": {
        "recommended": "text/html; charset=UTF-8",
        "guidance": "The Content-Type representation header is used to indicate the original media type of the resource. If not set correctly, the resource (e.g. an image) may be interpreted as HTML, making XSS vulnerabilities possible. charset attribute is necessary to prevent XSS in HTML pages.",
    },
    "Set-Cookie": {
        "recommended": "Secure; HttpOnly; SameSite",
        "guidance": "The Set-Cookie HTTP response header is used to send a cookie from the server to the user agent. Always use the Secure, HttpOnly, and SameSite attributes. To send multiple cookies, multiple Set-Cookie headers should be sent in the same response.",
    },
    "Strict-Transport-Security": {
        "recommended": "max-age=63072000; includeSubDomains",
        "guidance": "The HTTP Strict-Transport-Security response header (HSTS) lets a website tell browsers that it should only be accessed using HTTPS. OWASP no longer recommends including the preload directive by default as premature preloading can cause operational problems.",
    },
    "Access-Control-Allow-Origin": {
        "recommended": "https://yoursite.com",
        "guidance": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin. Never use wildcard (*) for authenticated endpoints.",
    },
    "Cross-Origin-Opener-Policy": {
        "recommended": "same-origin",
        "guidance": "Isolates the browsing context exclusively to same-origin documents.",
    },
    "Cross-Origin-Embedder-Policy": {
        "recommended": "require-corp",
        "guidance": "A document can only load resources from the same origin, or resources explicitly marked as loadable from another origin.",
    },
    "Cross-Origin-Resource-Policy": {
        "recommended": "same-origin",
        "guidance": "Limits resource loading to the same origin only. OWASP tightened this from same-site to same-origin.",
    },
    "Content-Security-Policy": {
        "recommended": "default-src 'self'; form-action 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests",
        "guidance": "CSP is a powerful defense-in-depth mechanism against XSS. This is a restrictive baseline policy. Customize based on your application's needs.",
    },
    "Permissions-Policy": {
        "recommended": "accelerometer=(), autoplay=(), camera=(), cross-origin-isolated=(), display-capture=(), encrypted-media=(), fullscreen=(), geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(), midi=(), payment=(), picture-in-picture=(), publickey-credentials-get=(), screen-wake-lock=(), sync-xhr=(self), usb=(), web-share=(), xr-spatial-tracking=(), clipboard-read=(), clipboard-write=(), gamepad=(), hid=(), idle-detection=(), interest-cohort=(), serial=(), unload=()",
        "guidance": "Deny all browser features that your site does not need or allow them only to authorized domains. OWASP now recommends a comprehensive list of 29 features to explicitly deny.",
    },
    "X-DNS-Prefetch-Control": {
        "recommended": "off",
        "guidance": "The default behavior of browsers is to perform DNS caching which is good for most websites. If you do not control links on your website, you might want to set off as a value to disable DNS prefetch to avoid leaking information to those domains.",
    },
    "X-Permitted-Cross-Domain-Policies": {
        "recommended": "none",
        "guidance": "Prevents Adobe Flash and Acrobat from loading cross-domain data. OWASP classifies this as Active (not deprecated).",
    },
    "Cache-Control": {
        "recommended": "no-store, max-age=0",
        "guidance": "For pages containing sensitive information, set Cache-Control to prevent caching. This prevents sensitive data from being stored in browser or proxy caches.",
    },
    "Clear-Site-Data": {
        "recommended": '"cache","cookies","storage"',
        "guidance": "Instructs the browser to clear site data (cache, cookies, storage). Particularly useful on logout endpoints to ensure session data is fully cleared.",
    },
}

bad_security_headers = {
    "Expect-CT": {
        "recommended": "Remove this header",
        "guidance": "Deprecated. Certificate Transparency is now enforced by default in all major browsers. OWASP recommends removing this header entirely.",
    },
    "X-XSS-Protection": {
        "recommended": "0 or remove entirely",
        "guidance": "Deprecated. Can actually create XSS vulnerabilities in otherwise safe sites. Use Content-Security-Policy instead. If you must set it, use 0 to disable the XSS auditor.",
    },
    "X-Powered-By": {
        "recommended": "Remove this header",
        "guidance": "OWASP recommends removing all X-Powered-By headers as they leak server technology information.",
    },
    "X-AspNet-Version": {
        "recommended": "Remove this header",
        "guidance": "Provides information on the .NET version. OWASP recommends disabling this header.",
    },
    "X-AspNetMvc-Version": {
        "recommended": "Remove this header",
        "guidance": "Provides information on the .NET MVC version. OWASP recommends disabling this header.",
    },
    "Public-Key-Pins": {
        "recommended": "Remove this header",
        "guidance": "Deprecated and should no longer be used. HPKP was removed from modern browsers due to the risk of site lockout.",
    },
    "Feature-Policy": {
        "recommended": "Remove and replace with Permissions-Policy",
        "guidance": "Deprecated. Replaced by the Permissions-Policy header.",
    },
    "Pragma": {
        "recommended": "Remove this header",
        "guidance": "Deprecated. Use Cache-Control instead. Pragma is an HTTP/1.0 artifact and no longer needed.",
    },
}

potentially_interesting_headers = {
    "Server": {
        "recommended": "Remove or set non-informative value",
        "guidance": "Remove this header or set non-informative values to avoid leaking server technology information.",
    },
    "X-Php-Version": {
        "recommended": "Remove this header",
        "guidance": "Leaks PHP version information. Should be removed.",
    },
    "Powered-By": {
        "recommended": "Remove this header",
        "guidance": "Leaks technology stack information. Should be removed.",
    },
    "X-CF-Powered-By": {
        "recommended": "Remove this header",
        "guidance": "Leaks ColdFusion technology information. Should be removed.",
    },
    "X-Generator": {
        "recommended": "Remove this header",
        "guidance": "Leaks CMS/generator information. Should be removed.",
    },
    "X-Redirect-By": {
        "recommended": "Remove this header",
        "guidance": "Leaks information about the application handling redirects (e.g. WordPress). Should be removed.",
    },
    "SourceMap": {
        "recommended": "Remove in production",
        "guidance": "Source maps expose original source code. Remove in production environments.",
    },
    "X-SourceMap": {
        "recommended": "Remove in production",
        "guidance": "Source maps expose original source code. Remove in production environments.",
    },
}
