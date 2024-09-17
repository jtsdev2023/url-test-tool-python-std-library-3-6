# utility_module.py


"""
This module contains utility functions for the main program.
"""


import re
import sys
import urllib.error
import urllib.request as request
from concurrent.futures import ThreadPoolExecutor


# break validate_url_format into two functions... loosen coupling
# validate
def validate_url_format(input_url):
    """Validate URL format"""
    # regex pattern for URL
    url_pattern = re.compile(r'^https?://[\w\W]+\.[\w\W]+/?[\w\W]*')

    _url = str( input_url ).strip()

    if url_pattern.match(_url):
        return True
    else:
        return False



# manipulate... assumes a good URL
def dissect_url(input_url):
    """Dissect URL into scheme and domain"""
    url_split_pattern = re.compile(r'/{1,2}')

    _url = str( input_url ).strip()

    _scheme, _domain = url_split_pattern.split(_url)[0:2]
    return _scheme.strip(':'), _domain



# get URL
def request_url(input_url):
    """Request URL"""
    try:
        with request.urlopen(input_url, timeout=5) as response:
            return response.status, response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        # print(f"HTTP Error: {e}")
        return 1, e
    except urllib.error.URLError as e:
        # print(f"URL Error: {e}")
        return 1, e
    except Exception as e:
        # print(f"Error: {e}")
        return 1, e


# transform URL domain... replace '.' with '_'
def transform_url_domain(url_domain):
    """Transform URL domain. Replace '.' with '_'"""
    # can URL domain contain more than one '.' or special characters ?
    return url_domain.replace('.', '_')



# write to text file
def write_to_file_text(url_domain, url, status, content):
    """Write to text file"""
    with open(f'{url_domain}.txt', 'a', encoding='utf-8') as txt_f:
        txt_f.write("\n****************************************\n")
        txt_f.write(f"URL: {url}\n")
        txt_f.write(f"HTTP Status Code: {status}\n")
        txt_f.write(f"Content:\n\n{content}\n\n")
        txt_f.write("\n****************************************\n")



# write to csv file
def write_to_file_csv(url_domain, timestamp, elapsed_time_ms):
    """Write to CSV file"""
    with open(f'{url_domain}.csv', 'a', encoding='utf-8') as csv_f:
        csv_f.write(f"{url_domain},{timestamp},{elapsed_time_ms}\n")



# write to stdout
def write_to_stdout(url, http_status, elapsed_time_ms):
    """Write to stdout"""
    print(
        f"\nURL: {url}\n"
        f"HTTP Status Code: {http_status}\n"
        f"Elapsed time: {elapsed_time_ms:.3f} seconds\n"
    )



# read url from file
def read_url_from_file(file_name):
    """Read URLs from a file"""
    with open(file_name, 'r', encoding='utf-8') as f:
        return [ line.strip() for line in f if line.strip() ]



def write_to_file_threading(result_list):
    """Write multithread results to text and csv files"""

    # result_list structure
    # list[ list[tuple(str, str, str, str, str, str), ...] ]
    # (domain: str, url: str, status:str, content:str, timestamp:str, elapsed_time_ms:str)
    for result in result_list:
        with ThreadPoolExecutor() as executor:
            for r in result:
                executor.submit(
                    write_to_file_text, r[0], r[1], r[2], r[3] )

                executor.submit(
                    write_to_file_csv, r[0], r[4], r[5] )



if __name__ == '__main__':
    pass
