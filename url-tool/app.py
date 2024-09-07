# app.py


"""
This module is used to run the URL test tool.
"""



import time
# from concurrent.futures import ThreadPoolExecutor
# import utility_module                                       # pylint: disable=import-error
import argparse_module                                      # pylint: disable=import-error
import get_url_module                                       # pylint: disable=import-error


def main():
    """Docstring"""
    args = argparse_module.parser.parse_args()

    # if args.threading is False:
    #     for url in args.url:

    #         loop_counter = 0

    #         while loop_counter < args.count:
    #             loop_counter += 1

    #             # url_result = utility_module.validate_url_format(url)
    #             # if isinstance(url_result, int) and url_result > 0:
    #             if utility_module.validate_url_format(url) is False:
    #                 print("URL validation failed.")
    #                 url = None
    #                 break

    #             elif utility_module.validate_url_format(url) is True:
    #                 scheme, domain = utility_module.dissect_url(url)

    #             timestamp = time.strftime('%H:%M:%S')
    #             start_time_ns = time.perf_counter_ns()

    #             url, status, content = utility_module.request_url(url)

    #             end_time_ns = time.perf_counter_ns()
    #             elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)

    #             # print(f"URL: {scheme}://{domain}\nElapsed time: {elapsed_time_ms:.3f} seconds")
    #             utility_module.write_to_stdout(url, status, elapsed_time_ms)

    #             transformed_domain = utility_module.transform_url_domain(domain)

    #             # with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
    #             #     f.write(f"URL: {url_response[0]}\n")
    #             #     f.write(f"HTTP Status Code: {url_response[1]}\n")
    #             #     f.write(f"Content:\n\n{url_response[2]}\n\n")

    #             utility_module.write_to_file_text(transformed_domain, url, status, content)
    #             utility_module.write_to_file_csv(
    #                 transformed_domain, domain, timestamp, elapsed_time_ms)

    #             time.sleep(args.interval)

    # if args.threading is True:
    #     print("Entering threading mode...")
    #     with ThreadPoolExecutor() as executor:
    #         thread_results = [
    #             executor.submit(utility_module.request_url, url) for url in args.url]

    #     for result in thread_results:
    #         # result.result() is a tuple (url, status, content)
    #         # this 'url' does not necessarily match the original user input URL
    #         # need to fix this
    #         url, status, content = result.result()

    #         scheme, domain = utility_module.dissect_url(url)
    #         transformed_domain = utility_module.transform_url_domain(domain)
    #         utility_module.write_to_file_text(transformed_domain, url, status, content)

    #         print(f"URL: {url}\nHTTP Status Code: {status}")


if __name__ == '__main__':
    args = argparse_module.parser.parse_args()

    run = get_url_module.RunGetURL(
        args.url, args.interval, args.count, args.threading, args.suppress)

    if args.threading is False:
        run.run_serial_get_url()

    elif args.threading is True:
        get_url_module.run_multi_threading(args.url, args.interval, args.count)

    # main()

    # args = argparse_module.parser.parse_args()

    # if args.threading is False:
    #     for url in args.url:

    #         loop_counter = 0

    #         while loop_counter < args.count:
    #             loop_counter += 1

    #             # url_result = utility_module.validate_url_format(url)
    #             print(f"URL: {url}")
    #             # if isinstance(url_result, int) and url_result > 0:
    #             if utility_module.validate_url_format(url) is False:
    #                 print("URL validation failed.")
    #                 url = None
    #                 break

    #             elif utility_module.validate_url_format(url) is True:
    #                 scheme, domain = utility_module.dissect_url(url)

    #             timestamp = time.strftime('%H:%M:%S')
    #             start_time_ns = time.perf_counter_ns()

    #             url, status, content = utility_module.request_url(url)

    #             end_time_ns = time.perf_counter_ns()
    #             elapsed_time_ms = round( (end_time_ns - start_time_ns) / 10e9, 3)

    #             # print(f"URL: {scheme}://{domain}\nElapsed time: {elapsed_time_ms:.3f} seconds")
    #             utility_module.write_to_stdout(url, status, elapsed_time_ms)

    #             transformed_domain = utility_module.transform_url_domain(domain)

    #             # with open(f'{output_filename}.txt', 'a', encoding='utf-8') as f:
    #             #     f.write(f"URL: {url_response[0]}\n")
    #             #     f.write(f"HTTP Status Code: {url_response[1]}\n")
    #             #     f.write(f"Content:\n\n{url_response[2]}\n\n")

    #             utility_module.write_to_file_text(transformed_domain, url, status, content)
    #             utility_module.write_to_file_csv(
    #                 transformed_domain, domain, timestamp, elapsed_time_ms)

    #             time.sleep(args.interval)

    # if args.threading is True:
    #     print("Entering threading mode...")
    #     with ThreadPoolExecutor() as executor:
    #         thread_results = [
    #             executor.submit(utility_module.request_url, url) for url in args.url]

    #     # for result in thread_results:
    #     #     # result.result() is a tuple (url, status, content)
    #     #     # this 'url' does not necessarily match the original user input URL
    #     #     # need to fix this
    #     #     url, status, content = result.result()

    #     #     scheme, domain = utility_module.dissect_url(url)
    #     #     transformed_domain = utility_module.transform_url_domain(domain)
    #     #     utility_module.write_to_file_text(transformed_domain, url, status, content)

    #     #     print(f"URL: {url}\nHTTP Status Code: {status}")
