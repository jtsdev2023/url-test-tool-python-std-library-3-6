# argparse-module.py


"""
This module is used to parse command-line arguments.
"""


import argparse


class URLMaxNargs(argparse.Action):
    """argparse action to limit the number of URLs"""
    def __call__(self, parser, namespace, input_values, option_string=None):
        if len(input_values) > 6:
            parser.error(f'{option_string} accepts a maximum of 6 URLs')
        setattr(namespace, self.dest, input_values)


parser = argparse.ArgumentParser(
    prog='url-tool',
    description=(
    'URL test tool using only the Python standard '
    'library and backwards compatible with Python 3.6'),
    epilog='Thank you for using the URL test tool!'
)

# group to exclude using inline URL list or URL list file at same time
exclude_group_url_inline_file = parser.add_mutually_exclusive_group(required=True)
# -u/--url is limited to 6 inline URLs
exclude_group_url_inline_file.add_argument(
    '-u', '--url', type=str, nargs='+', help='URLs to test', action=URLMaxNargs)
exclude_group_url_inline_file.add_argument(
    '-f', '--file', type=str, help='File containing URLs to test')

# normal arguments
parser.add_argument('-i', '--interval', type=int, help='Interval in seconds between tests')
parser.add_argument('-c', '--count', type=int, help='Number of times to HTTP GET the URLs')
parser.add_argument('-s', '--suppress', action='store_true', help='Suppress output')
parser.add_argument('-t', '--threading', action='store_true',
                    help='Use threading to GET URLs. Implies "-s/--suppress". '\
                        ' Default is serial mode.'
)
