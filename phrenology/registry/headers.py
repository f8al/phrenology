EXPECTED_HEADERS = {
                        "result":["success","error"],
                        "items":[
                            "X-Frame-Options", 
                            "X-Content-Type-Options", 
                            "Strict-Transport-Security",
                            "Permissions-Policy", 
                            "X-Frame-Options", 
                            "Strict-Transport-Security",
                            "Content-Security-Policy", 
                            "Cross-Origin-Embedder-Policy", 
                            "Cross-Origin-Resource-Policy",
                            "Cross-Origin-Opener-Policy",
                            "Referrer-Policy"
                            ]
                    }

DEPRICATED_HEADERS = {
                        "result":["warn","success"],
                        "items":[
                            "X-XSS-Protection", 
                            "Expect-CT", 
                            "X-Permitted-Cross-Domain-Policies"
                            ]
                    }

INFORMATION_HEADERS = {
                            "result":["info","info"],
                            "items":[
                                "X-Powered-By", 
                                "Server", 
                                "x-AspNet-Version", 
                                "X-AspNetMvc-Version",
                                "CF-RAY"
                                ]
                        }
CACHE_HEADERS = {
                    "result":["info","info"],
                    "items":[
                        "Cache-Control", 
                        "Pragma", 
                        "Last-Modified", 
                        "Expires", 
                        "ETag"]
                }
          