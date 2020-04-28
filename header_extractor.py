import requests
import argparse
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

print('''

  _   _                _
 | | | | ___  __ _  __| | ___ _ __
 | |_| |/ _ \/ _` |/ _` |/ _ \ '__|
 |  _  |  __/ (_| | (_| |  __/ |
 |_|_|_|\___|\__,_|\__,_|\___|_| _
  | ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __
  |  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
  | |___ >  <| |_| | | (_| | (__| || (_) | |
  |_____/_/\_\\__|_|  \__,_|\___|\__\___/|_|

A Simple Tool Using Requests To Extract
Headers From a List of Hosts'''
)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Select File of Targets")

args = parser.parse_args()
file = args.file

if args.file:
    f = open(file, "r")
    for line in f:
        requests.packages.urllib3.disable_warnings()
        try:
            line = line.rstrip("\n")
            http = "http://" + line
            https = "https://" + line
            r1 = requests.get(http, timeout=2)
            r2 = requests.get(https, verify=False, timeout=2)
            r1h = dict(r1.headers)
            r2h = dict(r2.headers)
            dict1 = json.dumps(r1h, indent=4)
            dict2 = json.dumps(r2h, indent=4)
            print("\n")
            print("-" * 50)
            print("\n")
            print("[*] IP: " + line)
            print("[*] HTTP Response Headers")
            print("\n")
            print(highlight(dict1, JsonLexer(), TerminalFormatter()))
            print("\n")
            print("[*] HTTPS Response Headers")
            print("\n")
            print(highlight(dict2, JsonLexer(), TerminalFormatter()))
            print("\n\n")
        except requests.exceptions.Timeout:
            print("[!] Request Timed Out")
            pass
else:
    print("[!] Error! Must Input File Parameter")
