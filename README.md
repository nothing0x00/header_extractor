# Header Extractor

A Simple Tool Using Requests To Extract Headers From a List of Hosts

## Use

The header_extractor.py script is a simple Python3 script that leverages Requests to extract the headers from a list of target IPs or URLs. The script will iterate through the list specified in the command line options, make requests to both port 80 and 443, then parse the response headers, and print them in prettified, colorized JSON output for ease of use.  The goal of this script is to allow a user, either a systems administrator or pentester, to check headers on a large group of possible targets for information leakage or other header related vulnerabilities.

To install dependencies run the following:

`pip3 install -r requirements.txt`

Then, to run the script, do the following:

`python3 header_extractor.py -f [targets file]`

The result will be a color coded JSON output of the headers for services on ports 80 and 443 for hosts in the target list.
