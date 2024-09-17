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
    loop_counter = 1

    while loop_counter <= count:
        loop_counter += 1

        if utility_module.validate_url_format(url) is False:
            print(url)
            print("URL validation failed.")
            url = None
            break
        else:
            scheme, domain = utility_module.dissect_url(url)

        timestamp = time.strftime('%H:%M:%S')
        start_time_ns = time.perf_counter_ns()

        url, status, content = utility_module.request_url(url)

        end_time_ns = time.perf_counter_ns()
        elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3 )

        if threading is False:
            utility_module.write_to_stdout(url, status, elapsed_time_ms)

        transformed_domain = utility_module.transform_url_domain(domain)


        if suppress is False:
            utility_module.write_to_file_text(transformed_domain, url, status, content)
            utility_module.write_to_file_csv(transformed_domain, domain, timestamp, elapsed_time_ms)

        time.sleep(interval)


# def run(url, count):
#     """Run get URL request"""
#     loop_counter = 0
#     while loop_counter <= count:
#         loop_counter += 1

#         if utility_module.validate_url_format(url) is False:
#             print("URL validation failed.")
#             url = None
#             break

#         elif utility_module.validate_url_format(url) is True:
#             scheme, domain = utility_module.dissect_url(url)

#         timestamp = time.strftime('%H:%M:%S')
#         start_time_ns = time.perf_counter_ns()

#         url, status, content = utility_module.request_url(url)

#         end_time_ns = time.perf_counter_ns()
#         elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)

#         return url, domain, status, timestamp, elapsed_time_ms, content


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
