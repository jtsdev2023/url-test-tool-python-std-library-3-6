# app.py


"""
This module is used to run the URL test tool.
"""


import utility_module
import argparse_module


def main():
    """Docstring"""
    args = argparse_module.parser.parse_args()
    
    for url in args.url:
        url = str( utility_module.validate_url_format(url) )

        response_data = utility_module.request_url(url)
        if response_data is not None:
            print(response_data)
        else:
            print(f"Error: No data returned from {url}")


if __name__ == '__main__':
    main()
