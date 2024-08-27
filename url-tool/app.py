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

                url_result = utility_module.validate_url_format(url)

                if isinstance(url_result, int) and url_result > 0:
                    print("URL validation failed.")
                    break

                scheme, domain = url_result

                start_time_ns = time.perf_counter_ns()
                url_response = utility_module.request_url(url)
                end_time_ns = time.perf_counter_ns()
                elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)
                print(f"URL: {scheme}://{domain}\nElapsed time: {elapsed_time_ms:.3f} seconds")

                output_filename = domain.replace('.', '_')

                with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
                    f.write(f"URL: {url_response[0]}\n")
                    f.write(f"HTTP Status Code: {url_response[1]}\n")
                    f.write(f"Content:\n\n{url_response[2]}\n\n")

                time.sleep(args.interval)

    if args.threading is True:
        with ThreadPoolExecutor() as executor:
            thread_results = [
                executor.submit(utility_module.request_url, url) for url in args.url]

        for result in thread_results:
            # result.result() is a tuple (url, status, content)
            # this 'url' does not necessarily match the original user input URL
            # need to fix this
            url, status, content = result.result()

            url_result = utility_module.validate_url_format(url)
            scheme, domain = url_result
            output_filename = domain.replace('.', '_')

            with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"HTTP Status Code: {status}\n")
                f.write(f"Content:\n\n{content}\n\n")


if __name__ == '__main__':
    main()
