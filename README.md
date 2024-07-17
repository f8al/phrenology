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
Usage: python3 phrenology.py domain
```
