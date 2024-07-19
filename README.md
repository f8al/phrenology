# phrenology - a tool to read security HEADers

# Why was this made
This project started out of a need from my leadership to have an extendable and scalable method for checking the security headers on all of the sites and pages in our external attack surface.  I found a couple tools already written, but most of them were either poorly written, all of the features they claimed to have didnt actually work, or the tool has been unmaintained for years.

The goal of phrenology was to be able to create an extendable well written tool that could easily be agmented to be used in a web GUI as well as being a CLI tool, with the ability to output its data in a number of useful ways.

This project is also being used as a way for me to better learn the concepts of Object-Oriented programming, the goal of which being to take myself from merely scripting tools and  releasing monolithic scripts, to being able to actually develop well written and documented tools to give back to the security community in a more meaningful way.

# How to run:

### From source
```bash
git clone https://github.com/f8al/phrenology && cd phrenology
python3 phrenology.py -u https://google.com
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
  -d, --deprecated      Show deprecated headers
  -f FILE, --file FILE  path to file containing a list of domains
  -i, --information     Show informational headers headers
  -g, --get             Use GET request method instead of HEAD
  -j, --json            Output results as a json object
```

## Screenshots
![](https://github.com/f8al/media/blob/main/phrenology.png?raw=true)

# About the name
If you're one of the people looking at this tool going "OMG PHRENOLOGY IS RACIST!!1one!" then please read on below.

## Acknowledging the Past:
The term "phrenology" historically refers to a now-debunked pseudoscience that claimed to determine personality traits and mental abilities based on the shape of the skull. We acknowledge the problematic and pseudo-scientific nature of phrenology and its misapplication in the past.

## Highlighting the Irony:
In choosing this name for our web security tool, we aim to draw a parallel to the often overlooked and underestimated importance of security headers in web development. Just as phrenology was taken seriously despite its lack of scientific basis, the security of web headers is frequently dismissed or neglected by some engineers.

## Our Purpose:
"Phrenology" is a tool designed to rigorously check the security headers of websites, ensuring they are robust against common vulnerabilities. It serves as a reminder that while we may laugh at the absurdity of past pseudo-sciences, the real absurdity lies in the modern-day neglect of essential security practices.

## A Call to Action:
Let’s take web security seriously. Just as the scientific community moved beyond phrenology to better understand the human mind, we must move beyond superficial security measures to protect our digital assets. Our tool aims to make it easier for engineers to uphold high security standards, ensuring a safer web for everyone.

# Contribution credit
This tool has been developed with extensive guidance and direction from [@DataMinion](https://github.com/DataMinion)
