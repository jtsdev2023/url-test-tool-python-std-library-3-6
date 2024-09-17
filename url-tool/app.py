# app.py


"""
This module is used to run the URL test tool.
"""


import argparse_module                                      # pylint: disable=import-error
import get_url_module                                       # pylint: disable=import-error



if __name__ == '__main__':
    args = argparse_module.parser.parse_args()

    if args.threading is True:
        r = get_url_module.run_multi_threading(
            args.url, args.interval, args.count, args.threading, args.suppress)

    else:
        for url in args.url:
            get_url_module.run(url, args.interval, args.count, args.threading, args.suppress)
