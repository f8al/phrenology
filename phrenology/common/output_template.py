from .output import OutputAbstract

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

class Template(OutputAbstract):
    def __init__(self):
        self.name =''

    def _render_banner(self, data=None):
        print('           __                          __                 ')
        print('    ____  / /_  ________  ____  ____  / /___  ____ ___  __')
        print('   / __ \\/ __ \\/ ___/ _ \\/ __ \\/ __ \\/ / __ \\/ __ `/ / / /')
        print('  / /_/ / / / / /  /  __/ / / / /_/ / / /_/ / /_/ / /_/ / ')
        print(' / .___/_/ /_/_/   \\___/_/ /_/\\____/_/\\____/\\__, /\\__, /  ')
        print('/_/                                        /____//____/   ')
        print('      A simple tool for checking security HEADers         ')
        print('                   SecurityShrimp 2024                    ')

    def render_output(self, output_type, data = None):
        """
        Renders the output based on its type.

        Args:
            output_type (str): The type of the output.
            data (dict): The data to render.
        """
        method_name = f"_render_{output_type}"
        method = getattr(self, method_name, None)
        if callable(method):
            method(data)
        else:
            raise AttributeError(f"No render method found for type '{output_type}'")

    def _render_counts(self, data):
        """
        Renders the counts output.

        Args:
            data (dict): The data to render.
        """
        print("************************************")
        print("**        Counts Example        **\n")
        for key, value in data.items():
            print(f"\t{key}: {value}")

    def _render_list(self, data):
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

    def _render_read(self, data):
        """
        Renders the read output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print("**          Read Example          **\n\n")
        for key, value in data.items():
            print(f"\t{key}: {value}")

    def _render_error(self, data):
        """
        Renders the error output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print("**          Error Occurred        **\n\n")
        print(f"\t{data['message']}")