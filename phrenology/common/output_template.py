import json

from .output import OutputAbstract

"""
Contains all of the methods for processing and displaying output from phrenology lib
"""


class darkcolors:
    """
    sets colors to dark values
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class lightcolors:
    """
    sets colors to light values
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[95m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def colorize(string, alert, colors=None):
    bcolors = darkcolors
    if colors == "light":
        bcolors = lightcolors
    elif colors == "none":
        return string
    color = {
        "error": bcolors.FAIL + string + bcolors.ENDC,
        "warning": bcolors.WARNING + string + bcolors.ENDC,
        "success": bcolors.OKGREEN + string + bcolors.ENDC,
        "info": bcolors.OKBLUE + string + bcolors.ENDC,
        "deprecated": string,  # No color for deprecated headers or not-an-issue ones
    }
    return color[alert] if alert in color else string


def colorize_exclamation_and_key(key, alert):
    exclamation_point = colorize("!", "error")  # Adjust color as needed
    colored_key = colorize(key, alert)
    return f"[!] Missing security header: {exclamation_point} {colored_key}"


class Template(OutputAbstract):
    def __init__(self):
        self.name = ""

    def _render_banner(self, url=None, name=None, result=None, data=None):
        """
        Renders the Banner

        Args:
            none
        """
        print("           __                          __                 ")
        print("    ____  / /_  ________  ____  ____  / /___  ____ ___  __")
        print("   / __ \\/ __ \\/ ___/ _ \\/ __ \\/ __ \\/ / __ \\/ __ `/ / / /")
        print("  / /_/ / / / / /  /  __/ / / / /_/ / / /_/ / /_/ / /_/ / ")
        print(" / .___/_/ /_/_/   \\___/_/ /_/\\____/_/\\____/\\__, /\\__, /  ")
        print("/_/                                        /____//____/   ")
        print("      A simple tool for checking security HEADers         ")
        print("           SecurityShrimp/DataMinion 2024                 ")
        print("\n\n")

    def render_output(self, output_type, name=None, url=None, result=None, data=None):
        """
        Renders the output based on its type.

        Args:
            output_type (str): The type of the output.
            data (dict): The data to render.
        """
        method_name = f"_render_{output_type}"
        method = getattr(self, method_name, None)
        if callable(method):
            method(name, url, result, data)
        else:
            raise AttributeError(f"No render method found for type '{output_type}'")

    def _render_counts(self, name, url, result, data):
        """
        Renders the counts output.

        Args:
            data (dict): The data to render.
        """
        # print("************************************")
        # print(f"**          {name}: Counts Example        **\n")
        for key, value in data.items():
            if key == "expected":
                alert = result[0]
            elif key == "missing":
                alert = result[1]
            else:
                alert = "info"

            # print(colorize(f"\t{key}: {value}",alert))

    def _render_list(self, name, url, result, data):
        """
        Renders the list output.

        Args:
            data (dict): The data to render.
        """

        domain = url
        colorbang = colorize("!", "error")
        colorsplat = colorize("*", "info")

        found_alert = result[0] if result else "success"
        missing_alert = result[1] if result and len(result) > 1 else "error"
        owasp = data.get("owasp", {})

        if missing_alert != "error" and not data["expected"]:
            print(f"[{colorsplat}] No {colorize(name.lower(), 'success')} found on {colorize(domain, 'info')}")
            return

        print(f"[*] Analyzing {colorize(name, 'info')} of {colorize(domain, 'info')}")

        for key, value in data["expected"].items():
            print(
                f"[{colorize('!', found_alert) if found_alert == 'warn' else colorsplat}] Header {colorize(key, found_alert)} is present! (Value: {colorize(value, 'info')})"
            )
            if key in owasp:
                entry = owasp[key]
                print(f"    OWASP Recommended: {colorize(entry['recommended'], 'info')}")
                print(f"    Guidance: {entry['guidance']}")
        if missing_alert == "error":
            for key, value in data["missing"].items():
                print(f"[{colorbang}] Missing security header: {colorize(key, 'error')}")
                if key in owasp:
                    entry = owasp[key]
                    print(f"    OWASP Recommended: {colorize(entry['recommended'], 'info')}")
                    print(f"    Guidance: {entry['guidance']}")
        for key, value in data["present"].items():
            print(
                f"[{colorsplat}] {colorize(key, 'info')}: {value}"
            )

    def _render_read(self, name, url, result, data):
        """
        Renders the read output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print(f"**          {name}: Read Example          **\n\n")
        for key, value in data.items():
            print(f"\t{key}: {value}")

    def _render_error(self, name, url, result, data):
        """
        Renders the error output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print(f"**          {name}: Error Occurred        **\n\n")
        print(f"\t{data['message']}")


class JsonTemplate(OutputAbstract):
    """
    Collects header analysis results and outputs them as JSON.
    """

    def __init__(self):
        self.results = {}

    def render_output(self, output_type, name=None, url=None, result=None, data=None):
        method_name = f"_render_{output_type}"
        method = getattr(self, method_name, None)
        if callable(method):
            method(name, url, result, data)
        else:
            raise AttributeError(f"No render method found for type '{output_type}'")

    def _render_banner(self, name=None, url=None, result=None, data=None):
        pass

    def _render_counts(self, name, url, result, data):
        if url not in self.results:
            self.results[url] = {}
        if name not in self.results[url]:
            self.results[url][name] = {}
        missing_alert = result[1] if result and len(result) > 1 else "error"
        counts = {"expected": data["expected"]}
        if missing_alert == "error":
            counts["missing"] = data["missing"]
        self.results[url][name]["counts"] = counts

    def _render_list(self, name, url, result, data):
        if url not in self.results:
            self.results[url] = {}
        if name not in self.results[url]:
            self.results[url][name] = {}
        missing_alert = result[1] if result and len(result) > 1 else "error"
        present = data.get("present", {})
        if present:
            self.results[url][name]["present"] = present
        if missing_alert == "error":
            self.results[url][name]["missing"] = list(data.get("missing", {}).keys())
        self.results[url][name]["expected"] = data.get("expected", {})

    def _render_read(self, name, url, result, data):
        if url not in self.results:
            self.results[url] = {}
        if name not in self.results[url]:
            self.results[url][name] = {}
        self.results[url][name]["details"] = data

    def _render_error(self, name, url, result, data):
        if url not in self.results:
            self.results[url] = {}
        self.results[url]["error"] = data.get("message", str(data))

    def dump(self):
        """Prints the collected results as JSON."""
        print(json.dumps(self.results, indent=2))
