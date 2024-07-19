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
Usage: python3 phrenology.py -u fqdn

Optional Arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to check headers
  -C COOKIE, --cookie COOKIE
                        Custom cookie to send
  -c, --cache           Show cache headers
  -d, --deprecated      Show informational headers
  -f FILE, --file FILE  path to file containing a list of domains
  -i, --information     Show informational headers headers
  -g, --get             Use GET request method instead of HEAD
  -j, --json            Output results as a json object
```

## Why was this made
This project started out of a need from my leadership to have an extendable and scalable method for checking the security headers on all of the sites and pages in our external attack surface.  I found a couple tools already written, like shceck.py in Kali, but most of them were either poorly written, all of the features they claimed to have didnt actually work, or the tool has been unmaintained for years.

The goal of phrenology was to be able to create an extendable well written tool that could easily be agmented to be used in a web GUI as well as being a CLI tool, with the ability to output its data in a number of useful ways.

I am also using this project as a way to better learn the concepts of OO programming to be able to take myself from merely scripting tools and just releasing monolithic scripts, to being able to actually develop well written and documented tools to give back to the security community in a more meaningful way.

## Contribution credit
This tool has been developed with extensive guidance and direction from DataMinion
