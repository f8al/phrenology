# phrenology - a tool to read security HEADers



## Check security headers on a target website

This tool was created out of a need to be able to audit which security headers were present on websites and which ones were not.

Found a couple other projects out there that do this, but of the ones I tried, most of them either didnt completely work, or were so poorly written that there was a ton of room for improvement on the concept.

## How to run:

### From source
```bash
git clone https://github.com/f8al/phrenology && cd phrenology
python3 phrenology.py https://google.com
```

## Usage
```
Usage: python3 phrenology.py [options] <target>

Options:
  -h, --help            show this help message and exit
  -p PORT, --port=PORT  Set a custom port to connect to
  -c COOKIE_STRING, --cookie=COOKIE_STRING
                        Set cookies for the request
  -a HEADER_STRING, --add-header=HEADER_STRING
                        Add headers for the request e.g. 'Header: value'
  -d, --disable-ssl-check
                        Disable SSL/TLS certificate validation
  -g, --use-get-method  Use GET method instead HEAD method
  -j, --json-output     Print the output in JSON format
  -i, --information     Display information headers
  -x, --caching         Display caching headers
  -k, --deprecated      Display deprecated headers
  --proxy=PROXY_URL     Set a proxy (Ex: http://127.0.0.1:8080)
  --hfile=PATH_TO_FILE  Load a list of hosts from a text file
  --colors=COLORS     Set up a colour profile [dark/light/none]
```
