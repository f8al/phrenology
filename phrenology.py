#!/bin/env python3
import argparse
from phrenology.main import Main
from phrenology.common.output_template import Template
def main(output):
    parser = argparse.ArgumentParser(description='Hatmaker CLI')
    parser.add_argument('url', type=str, help='URL to check headers')
    args = parser.parse_args()
    output.render_output("banner")
    main_obj = Main(output , {
            "method": "GET",
            "allow_redirects": False
        })
    main_obj.engage(args.url)

if __name__ == "__main__":
    main(Template())
