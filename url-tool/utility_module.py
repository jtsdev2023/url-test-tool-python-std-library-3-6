# utility_module.py


"""
This module contains utility functions for the main program.
"""


import re
import urllib.request as request
import urllib.error


# cli -u/--url parser
# not going to do an excessive amount of validation here
# will let urllib3 etc. error out if the URL is not valid
def validate_url_format(input_url):
    """Validate URL format"""
    # regex pattern for URL
    url_pattern_http = re.compile(r'^http://[\w\W]+')
    url_pattern_https = re.compile(r'^https://')

    # does this add any security from remote code execution?
    _url = input_url.to_string().strip()

    if url_pattern_http.match(_url) or url_pattern_https.match(_url):
        return _url


# get IANA/ICANN TLD list
class IANATopLevelDomain:
    """Class to handle ICANN/IANA top level domain (TLD) list tasks"""
    def __init__(self):
        self._url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
        self._tld_list = []
        self._tld_list_file = 'tld_list.txt'

    def retrieve_tld_list(self):
        """Retrieve TLD list"""
        try:
            with request.urlopen(self._url) as response:
                self._tld_list = response.read().decode('utf-8').splitlines()
        except Exception as e:
            print(f"Error: {e}")
        else:
            return self._tld_list

    def write_tld_list(self):
        """Write TLD list to file"""
        with open(self._tld_list_file, 'w', encoding='utf-8') as file:
            for line in self._tld_list:
                file.write(f"{line}\n")
        return self._tld_list_file
