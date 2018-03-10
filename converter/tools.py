"""
Tools
"""

import os.path
from HTMLParser import HTMLParser


HTML_TO_MD_MAP = {
    # 'html tag': ('MD open tag', 'MD close tag')
    'html': None,
    'head': None,
    'title': None,  # or maybe need to show title as H1
    'body': None,
    'h1': ('\n# ', '\n'),
    'p': ('\n', '\n'),
    'em': ('_', '_'),
    'strong': ('**', '**')
}


class HTMLToMD(HTMLParser):
    """Extract HTML and convert it to MD.

    Usage:
        Inst = HTMLToMD()
        Inst.feed(html_str)
        print Inst.out
    """
    supported_html_tags = HTML_TO_MD_MAP.keys()
    out = ''

    def check_html_tag(self, tag):
        """Check if HTML is supported"""
        if tag not in self.supported_html_tags:
            raise ValueError("Tag '%s' unsupported" % tag)

    def handle_starttag(self, tag, attrs):
        """Handle start tag"""
        self.check_html_tag(tag)
        md_tags = HTML_TO_MD_MAP[tag]
        if md_tags is not None:
            self.out += md_tags[0]

    def handle_data(self, data):
        """Handle data between start and end tag"""
        # check if there is a need to display this data
        if HTML_TO_MD_MAP[self.lasttag] is not None:
            self.out += data

    def handle_endtag(self, tag):
        """Handle end tag"""
        self.check_html_tag(tag)
        md_tags = HTML_TO_MD_MAP[tag]
        if md_tags is not None:
            self.out += md_tags[1]


class FileReader(object):
    """Read provided file"""

    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding

    def __check_file_exist(self):
        """Check if file with provided file path exists"""
        if not os.path.isfile(self.file_path):
            raise IOError(
                "File {path} not found".format(
                    path=self.file_path
                )
            )

    def read_file(self):
        """Read file.
        :return: (str) Stripped lines.
        """
        self.__check_file_exist()
        with open(self.file_path, 'r') as fileo:
            result = "".join([x.strip() for x in fileo.readlines()])
            result = result.decode(self.encoding)
            return result
