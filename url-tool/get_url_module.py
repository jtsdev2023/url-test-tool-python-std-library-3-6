# get_url_module.py


"""
This module runs the urllib requests functions from the utility_module.py.
"""


import time
from concurrent.futures import ThreadPoolExecutor
import utility_module                                      # pylint: disable=import-error


# functions
def run(url, interval, count, threading, suppress):
    """Run serial mode. Print to stdout and write to text and csv files"""

    thread_results = []

    scheme, domain = utility_module.dissect_url(url)
    # filename_domain = utility_module.transform_url_domain(domain)

    while count > 0:

        if utility_module.validate_url_format(url) is False:
            print(url)
            print("URL validation failed.")
            url = None
            break

        # scheme, domain = utility_module.dissect_url(url)

        timestamp = time.strftime('%H:%M:%S')
        start_time_ns = time.perf_counter_ns()

        status, content = utility_module.request_url(url)

        end_time_ns = time.perf_counter_ns()
        elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3 )

        if threading is False:
            utility_module.write_to_stdout(url, status, elapsed_time_ms)

        # filename_domain = utility_module.transform_url_domain(domain)

        if suppress is False and threading is False:
            utility_module.write_to_file_text(domain, url, status, content)
            utility_module.write_to_file_csv(domain, timestamp, elapsed_time_ms)

        elif threading is True:
            thread_results.append(
                domain, url, status, content, timestamp, elapsed_time_ms)

        count -= 1

        time.sleep(interval)

    if len(thread_results) > 0:
        return thread_results


def run_multi_threading(url_list, interval, count):
    """Run threading mode"""
    start_time_ns = time.perf_counter_ns()

    with ThreadPoolExecutor() as executor:
        [executor.submit(run, url, interval, count) for url in url_list]

    end_time_ns = time.perf_counter_ns()
    elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)

    print(f"\n\nMultithreading Module Elapsed Run Time: {elapsed_time_ms:.3f} seconds.\n\n")


if __name__ == '__main__':
    pass
