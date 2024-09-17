# utility_module.py


"""
This module contains utility functions for the main program.
"""


import sys
import re
import urllib.request as request
import urllib.error


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
        with request.urlopen(input_url) as response:
            return response.url, response.status, response.read().decode('utf-8')
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
def write_to_file_text(output_filename, url, status, content):
    """Write to text file"""
    with open(f'{output_filename}.txt', 'a', encoding='utf-8') as txt_f:
        txt_f.write("\n****************************************\n")
        txt_f.write(f"URL: {url}\n")
        txt_f.write(f"HTTP Status Code: {status}\n")
        txt_f.write(f"Content:\n\n{content}\n\n")
        txt_f.write("\n****************************************\n")


# write to csv file
def write_to_file_csv(output_filename, url_domain, timestamp, elapsed_time_ms):
    """Write to CSV file"""
    with open(f'{output_filename}.csv', 'a', encoding='utf-8') as csv_f:
        csv_f.write(f"{url_domain},{timestamp},{elapsed_time_ms}\n")


# write to stdout
def write_to_stdout(url, http_status, elapsed_time_ms):
    """Write to stdout"""
    print(
        f"\nURL: {url}\n"
        f"HTTP Status Code: {http_status}\n"
        f"Elapsed time: {elapsed_time_ms:.3f} seconds\n"
    )



if __name__ == '__main__':
    pass
