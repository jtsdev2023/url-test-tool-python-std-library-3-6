# app.py


"""
This module is used to run the URL test tool.
"""


import time
import utility_module                                       # pylint: disable=import-error
import argparse_module                                      # pylint: disable=import-error
from concurrent.futures import ThreadPoolExecutor


def main():
    """Docstring"""
    args = argparse_module.parser.parse_args()

    if args.threading is False:
        for url in args.url:

            loop_counter = 0
            while loop_counter < args.count:
                loop_counter += 1
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

                start_time_ns = time.perf_counter_ns()
                url_response = utility_module.request_url(url)
                end_time_ns = time.perf_counter_ns()
                elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)
                print(f"URL: {scheme}://{domain}\nElapsed time: {elapsed_time_ms:.3f} seconds")

                # output_filename = utility_module.create_file_name(domain)
                output_filename = domain.replace('.', '_')

                with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f"HTTP Status Code: {url_response[0]}\n")
                    f.write(f"Content:\n\n{url_response[1]}\n\n")

                time.sleep(args.interval)

        # if isinstance(url_response[1], Exception):
        #     print(f"ERROR: {url_response[1]}")
        # else:
        #     print(url_response[0], url_response[1])


if __name__ == '__main__':
    main()
