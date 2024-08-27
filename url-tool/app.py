# app.py


"""
This module is used to run the URL test tool.
"""


import urllib
import utility_module                                       # pylint: disable=import-error
import argparse_module                                      # pylint: disable=import-error
from concurrent.futures import ThreadPoolExecutor


def main():
    """Docstring"""
    args = argparse_module.parser.parse_args()

    if args.threading is False:
        for url in args.url:
            # url, _scheme, _domain = utility_module.validate_url_format(url)
            # print(f"scheme: {_scheme}")
            # print(f"domain: {_domain}")
            result = utility_module.validate_url_format(url)

            if isinstance(result, int) and result > 0:
                print("URL validation failed.")
                break

            scheme, domain = result
            # a, b, c = result
            # trying to add security by changing tye to str
            # does this really do anything?
            # a, b, c = [ str(x) for x in [a, b, c] ]
            # print(f"{a} {b} {c}")

            url_response = utility_module.request_url(url)

            # output_filename = utility_module.create_file_name(domain)
            output_filename = domain.replace('.', '_')

            with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
                f.write(f"HTTP Status Code: {url_response[0]}\n")
                f.write(f"Content:\n\n{url_response[1]}\n\n")

        # if isinstance(url_response[1], Exception):
        #     print(f"ERROR: {url_response[1]}")
        # else:
        #     print(url_response[0], url_response[1])


if __name__ == '__main__':
    main()
