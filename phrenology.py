#!/bin/env python3
import argparse
from phrenology import Main
from phrenology.common.output import Template
def main(output):
    parser = argparse.ArgumentParser(description='Phrenology CLI')
    parser.add_argument('-u', '--url', dest='url', type=str, help='URL to check headers', required=False)
    parser.add_argument('-C', '--cookie', dest='cookie', type=str, help='Custom cookie to send', required=False)
    parser.add_argument('-c', '--cache', dest='cache', action='store_true', help='Show cache headers', required=False)
    parser.add_argument('-d', '--deprecated', dest='deprecated', action='store_true', help='Show informational headers', required=False)
    parser.add_argument('-f', '--file', dest='file', type=str, help='path to file containing a list of domains', required=False )
    parser.add_argument('-i', '--information', dest='information', action='store_true', help='Show informational headers headers', required=False)
    parser.add_argument('-g', '--get', dest='get', action='store_true', help='Use GET request method instead of HEAD', required=False)
    parser.add_argument('-j', '--json', dest='json', action='store_true', help='Output results as a json object', required=False)
    

    args = parser.parse_args()
    output.render_output("banner")
    main_obj = Main(output , {
            "method": "HEAD",
            "allow_redirects": False,
            "verify": False
        })

    if args.file:
        with open(args.file, 'r') as f:
            urls = f.read().splitlines()
        for url in urls:
            main_obj.engage(url, args.cookie, args.cache, args.deprecated, args.information, args.get, args.json)
    elif args.url:
        main_obj.engage(args.url, args.cookie, args.cache, args.deprecated, args.information, args.get, args.json)
    else:
        # Handle error: No URL or file provided
        print("Error: Either -u/--url or -f/--file argument is required.")   
   # main_obj.engage(args.url, args.cookie, args.cache, args.deprecated, args.information, args.get, args.json)

if __name__ == "__main__":
    main(Template())
