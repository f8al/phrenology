EXPECTED_HEADERS = {
    "result": ["success", "error"],
    "items": [
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Permissions-Policy",
        "Content-Security-Policy",
        "Cross-Origin-Embedder-Policy",
        "Cross-Origin-Resource-Policy",
        "Cross-Origin-Opener-Policy",
        "Referrer-Policy",
        "X-Permitted-Cross-Domain-Policies",
        "X-DNS-Prefetch-Control",
        "Clear-Site-Data",
    ],
}

DEPRECATED_HEADERS = {
    "result": ["warn", "success"],
    "items": [
        "X-XSS-Protection",
        "Expect-CT",
        "Public-Key-Pins",
        "Feature-Policy",
        "Pragma",
    ],
}

INFORMATION_HEADERS = {
    "result": ["info", "info"],
    "items": [
        "X-Powered-By",
        "Server",
        "X-AspNet-Version",
        "X-AspNetMvc-Version",
        "X-Php-Version",
        "Powered-By",
        "X-CF-Powered-By",
        "X-Generator",
        "X-Redirect-By",
        "SourceMap",
        "X-SourceMap",
    ],
}

CACHE_HEADERS = {
    "result": ["info", "info"],
    "items": ["Cache-Control", "Pragma", "Last-Modified", "Expires", "ETag"],
}
