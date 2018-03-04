#!/usr/bin/env python
"""
Script for simple conversion from HTML to MarkDown.
"""

import argparse

from converter import tools


if __name__ == "__main__":

    # create arguments for a script
    PARSER = argparse.ArgumentParser(description='HTML to MD converter')
    REQ_ARGS = PARSER.add_argument_group('required arguments')

    PARSER.add_argument(
        '-e', '--encoding', default='utf-8', help='Encoding of a HTML page')
    REQ_ARGS.add_argument(
        '-f', '--file', required=True, help='HTML page path')

    ARGS = PARSER.parse_args()

    print (
        "{delim}\n"
        "HTML file path: {file}\n"
        "Encoding: {encod}\n"
        "{delim}\n"
        "".format(
            delim="=" * 40,
            file=ARGS.file,
            encod=ARGS.encoding
        )
    )

    # read file
    READER = tools.FileReader(
        file_path=ARGS.file,
        encoding=ARGS.encoding
    )
    html_str = READER.read_file()  # pylint: disable=invalid-name

    # convert html to MD
    CONV = tools.HTMLToMD()
    CONV.feed(html_str)
    print CONV.out
