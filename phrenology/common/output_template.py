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

def colorize(string, alert, colors=None):
    bcolors = darkcolors
    if colors == "light":
        bcolors = lightcolors
    elif colors == "none":
        return string
    color = {
        'error':    bcolors.FAIL + string + bcolors.ENDC,
        'warning':  bcolors.WARNING + string + bcolors.ENDC,
        'success':       bcolors.OKGREEN + string + bcolors.ENDC,
        'info':     bcolors.OKBLUE + string + bcolors.ENDC,
        'deprecated': string # No color for deprecated headers or not-an-issue ones
    }
    return color[alert] if alert in color else string

def colorize_exclamation_and_key(key, alert):
  exclamation_point = colorize("!", "error")  # Adjust color as needed
  colored_key = colorize(key, alert)
  return f"[!] Missing security header: {exclamation_point} {colored_key}"


class Template(OutputAbstract):
    def __init__(self):
        self.name =''

    def _render_banner(self, name=None, result=None, data=None):
        print('           __                          __                 ')
        print('    ____  / /_  ________  ____  ____  / /___  ____ ___  __')
        print('   / __ \\/ __ \\/ ___/ _ \\/ __ \\/ __ \\/ / __ \\/ __ `/ / / /')
        print('  / /_/ / / / / /  /  __/ / / / /_/ / / /_/ / /_/ / /_/ / ')
        print(' / .___/_/ /_/_/   \\___/_/ /_/\\____/_/\\____/\\__, /\\__, /  ')
        print('/_/                                        /____//____/   ')
        print('      A simple tool for checking security HEADers         ')
        print('           SecurityShrimp/DataMinion 2024                 ')
        print('\n\n')

    def render_output(self, output_type, name=None,result=None, data = None):
        """
        Renders the output based on its type.

        Args:
            output_type (str): The type of the output.
            data (dict): The data to render.
        """
        method_name = f"_render_{output_type}"
        method = getattr(self, method_name, None)
        if callable(method):
            method(name, result, data)
        else:
            raise AttributeError(f"No render method found for type '{output_type}'")

    def _render_counts(self, name, result, data):
        """
        Renders the counts output.

        Args:
            data (dict): The data to render.
        """
        #print("************************************")
        #print(f"**          {name}: Counts Example        **\n")
        for key, value in data.items():
            if (key == "expected"):
                alert = result[0]
            elif (key == "missing"):
                alert = result[1]
            else:
                alert = "info"
            
            #print(colorize(f"\t{key}: {value}",alert))
           
    def _render_list(self, name, result, data):
        """
        Renders the list output.

        Args:
            data (dict): The data to render.
        """
        
        domain = data['present']['Location']
        colorbang = colorize("!", "error")
        colorsplat = colorize("*", "info")

        print(f"[*] Analyzing {colorize(name, 'info')} of {colorize(domain, 'info')}")
        #for key, value in data["expected"].items():
        #    print(f'[{colorsplat}] Security headers expected for analysis: {key}')
        for key, value in data["present"].items():
            print(f"[{colorsplat}] Header {colorize(key, 'success')} is present! (Value: {colorize(value, 'info')})")
        for key, value in data["missing"].items():
            print(f"[{colorbang}] Missing security header: {colorize(key, 'error')}")

    def _render_read(self, name, result, data):
        """
        Renders the read output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print(f"**          {name}: Read Example          **\n\n")
        for key, value in data.items():
            print(f"\t{key}: {value}")

    def _render_error(self, name, result, data):
        """
        Renders the error output.

        Args:
            data (dict): The data to render.
        """
        print("\n************************************")
        print(f"**          {name}: Error Occurred        **\n\n")
        print(f"\t{data['message']}")