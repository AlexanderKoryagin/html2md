"""
Script for conversion from HTML to MarkDown.
"""

import argparse
from converter.converter import Converter

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='HTML to MD converter')
    required_args = parser.add_argument_group('required arguments')

    parser.add_argument(
        '-e', '--encoding', default='utf-8', help='Encoding of a HTML page')
    required_args.add_argument(
        '-f', '--file', required=True, help='HTML page path')

    args = parser.parse_args()

    print (
        "{delim}\n"
        "HTML file path: {file}\n"
        "Encoding: {encod}\n"
        "{delim}\n"
        "".format(
            delim="=" * 40,
            file=args.file,
            encod=args.encoding
        )
    )

    Conv = Converter(file_path=args.file, encoding=args.encoding)
    print Conv.to_md()

