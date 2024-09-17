# app.py


"""
This module is used to run the URL test tool.
"""


import argparse_module                                      # pylint: disable=import-error
import utility_module                                       # pylint: disable=import-error
import get_url_module                                       # pylint: disable=import-error



if __name__ == '__main__':
    args = argparse_module.parser.parse_args()

    if args.file:
        # read URLs from file
        url_list = utility_module.read_url_from_file(args.file)
    else:
        url_list = args.url


    if args.threading is True or args.no_stdout is True:
        THREADING = True
        # result_list structure
        # list[ list[tuple(str, str, str, str, str, str), ...] ]
        # (domain: str, url: str, status:str, content:str, timestamp:str, elapsed_time_ms:str)
        result_list = get_url_module.run_multi_threading(
            url_list, args.interval, args.count, THREADING, args.suppress)

        utility_module.write_to_file_threading(result_list)


    else:
        for url in url_list:
            get_url_module.run(url, args.interval, args.count, args.threading, args.suppress)
