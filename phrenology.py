#!/bin/env python3
import argparse
import time
from phrenology.main import Main



class darkcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class lightcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(string, alert, options):
    bcolors = darkcolors
    if options.colors == "light":
        bcolors = lightcolors
    elif options.colors == "none":
        return string
    color = {
        'error':    bcolors.FAIL + string + bcolors.ENDC,
        'warning':  bcolors.WARNING + string + bcolors.ENDC,
        'ok':       bcolors.OKGREEN + string + bcolors.ENDC,
        'info':     bcolors.OKBLUE + string + bcolors.ENDC,
        'deprecated': string # No color for deprecated headers or not-an-issue ones
    }
    return color[alert] if alert in color else string

class Template:

    @staticmethod
    def _render_banner(data):
        print('           __                          __                 ')
        print('    ____  / /_  ________  ____  ____  / /___  ____ ___  __')
        print('   / __ \/ __ \/ ___/ _ \/ __ \/ __ \/ / __ \/ __ `/ / / /')
        print('  / /_/ / / / / /  /  __/ / / / /_/ / / /_/ / /_/ / /_/ / ')
        print(' / .___/_/ /_/_/   \___/_/ /_/\____/_/\____/\__, /\__, /  ')
        print('/_/                                        /____//____/   ')
        print('      A simple tool for checking security HEADers         ')
        print('                   SecurityShrimp 2024                    ')

    @staticmethod
    def render_output(output_type, data):
        """
        Renders the output based on its type.

        Args:
            output_type (str): The type of the output.
            data (dict): The data to render.
        """
        method_name = f"_render_{output_type}"
        method = getattr(Template, method_name, None)
        if callable(method):
            method(data)
        else:
            raise AttributeError(f"No render method found for type '{output_type}'")

    @staticmethod
    def _render_counts(data):
        """
        Renders the counts output.

        Args:
            data (dict): The data to render.
        """
        print("************************************")
        print("**        Counts Example        **\n")
        for key, value in data["counts"].items():
            print(f"\t{key}: {value}")

    @staticmethod
    def _render_list(data):
        """
        Renders the list output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print("**        Analysis Example        **\n")
        print("\n\tDoes Exist:\n")
        for key, value in data["does_exist"].items():
            print(f"\t{key}: {value}")

        print("\n\tDoes Not Exist:\n")
        for key, value in data["not_exist"].items():
            print(f"\t{key}: {value}")

        print("\n\tMore Exist:\n")
        for key, value in data["more_exist"].items():
            print(f"\t{key}: {value}")

    @staticmethod
    def _render_read(data):
        """
        Renders the read output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print("**          Read Example          **\n\n")
        for key, value in data.items():
            print(f"\t{key}: {value}")

    @staticmethod
    def _render_error(data):
        """
        Renders the error output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print("**          Error Occurred        **\n\n")
        print(f"\t{data['message']}")

def main():
    parser = argparse.ArgumentParser(description='Hatmaker CLI')
    parser.add_argument('url', type=str, help='URL to check headers')
    args = parser.parse_args()

    Template.render_output("banner", {})
    main_obj = Main()
    main_obj.engage(args.url)

    previous_output = None

    while True:
        if main_obj.output != previous_output:
            previous_output = main_obj.output
            if previous_output:
                Template.render_output(previous_output['type'], previous_output['payload'])
        time.sleep(1)  # Sleep to prevent tight loop, adjust as needed

if __name__ == "__main__":
    main()
