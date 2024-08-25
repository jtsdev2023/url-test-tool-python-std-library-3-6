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
    url_pattern_http = re.compile(r'^http://[\w\W]+\.[\w\W]+/?[\w\W]*')
    url_pattern_https = re.compile(r'^https://[\w\W]+\.[\w\W]+/?[\w\W]*')
    url_pattern = re.compile(r'^https?://[\w\W]+\.[\w\W]+/?[\w\W]*')

    scheme_pattern = re.compile(r'^https?://')
    domain_pattern = re.compile(r'[\w\W]+\.[\w\W]+/?')

    url_split_pattern = re.compile(r'/{1,2}')

    # does this add any security from remote code execution?
    _url = str( input_url ).strip()

    # at the moment, i don't think i want to process http and https separately
    # subject to change
    # if url_pattern_http.match(_url):
    #     pass
    # elif url_pattern_https.match(_url):
    #     pass
    if url_pattern.match(_url):
        # _scheme = scheme_pattern.match(_url).group()
        # _domain = domain_pattern.search(_url).group()
        _scheme, _domain = url_split_pattern.split(_url)[0:2]
        return _url, _scheme.strip(':'), _domain
    else:
        print(f"Error: URL {_url} is not in the correct format.")
        return None, None, None


# get ICANN/IANA TLD list
class IANATopLevelDomain:
    """Class to handle ICANN/IANA top level domain (TLD) list tasks"""
    def __init__(self):
        self._url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
        self._url_data = None
        self._tld_list = []
        self._tld_list_file = 'tld_list.txt'

    def retrieve_tld_list(self):
        """Retrieve TLD list"""
        try:
            with request.urlopen(self._url) as response:
                self._url_data = response.read().decode('utf-8')
                self._tld_list = response.read().decode('utf-8').splitlines()
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e}")
        except urllib.error.URLError as e:
            print(f"URL Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        else:
            return self._tld_list

    def write_tld_list(self):
        """Write TLD list to file"""
        if self._url_data is not None:
            with open(self._tld_list_file, 'w', encoding='utf-8') as file:
                for line in self._tld_list:
                    file.write(f"{line}\n")
            return self._tld_list_file
        if self._url_data is None:
            print("Error: No IANA Top Level Domain (TLD) data to write to file.")


# get URL
def request_url(input_url):
    """Request URL"""
    try:
        with request.urlopen(input_url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
