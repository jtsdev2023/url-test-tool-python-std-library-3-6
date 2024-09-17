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

    # scheme unused at this time
    scheme, domain = utility_module.dissect_url(url)

    while count > 0:

        if utility_module.validate_url_format(url) is False:
            print(url)
            print("URL validation failed.")
            url = None
            break

        timestamp = time.strftime('%H:%M:%S')
        start_time_ns = time.perf_counter_ns()

        status, content = utility_module.request_url(url)

        end_time_ns = time.perf_counter_ns()
        elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3 )

        if threading is False:
            utility_module.write_to_stdout(url, status, elapsed_time_ms)

        if suppress is False and threading is False:
            utility_module.write_to_file_text(domain, url, status, content)
            utility_module.write_to_file_csv(domain, timestamp, elapsed_time_ms)

        elif threading is True:
            thread_results.append( (domain, url, status, content, timestamp, elapsed_time_ms) )

        count -= 1

        time.sleep(interval)

    if threading is True:
        return thread_results



def run_multi_threading(url_list, interval, count, threading, suppress):
    """Run threading mode"""

    start_time_ns = time.perf_counter_ns()

    with ThreadPoolExecutor() as executor:
        result = [
            executor.submit(run, url, interval, count, threading, suppress) for url in url_list]

    end_time_ns = time.perf_counter_ns()
    elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)

    print(f"\n\nMultithreading Module Elapsed Run Time: {elapsed_time_ms:.3f} seconds.\n\n")

    # is indexing the list comprehension pythonic? should use a for-loop instead?
    # without index 0, [r.result() for r in result][0], this returns a nested list...
    # [ [ (tuple), (tuple), ... ] ]
    result_list = [r.result() for r in result]

    return result_list



# handle threading results
def write_to_file_threading(result_list):
    """Write to text and csv files in threading"""

    # result structure
    # list[tuple(str, str, str, str, str, str), ...]
    # (domain: str, url: str, status:str, content:str, timestamp:str, elapsed_time_ms:str)
    for result in result_list:
        with ThreadPoolExecutor() as executor:
            for r in result:
                executor.submit(
                    utility_module.write_to_file_text, r[0], r[1], r[2], r[3] )

                executor.submit(
                    utility_module.write_to_file_csv, r[0], r[4], r[5] )



if __name__ == '__main__':
    pass
