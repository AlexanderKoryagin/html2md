import os.path


class Converter(object):

    def __init__(self, file_path, encoding):
        self.file_path = file_path
        self.encoding = encoding
        self.html_str = self.read_file()
        print 1

    def check_file_exist(self):
        if not os.path.isfile(self.file_path):
            raise IOError(
                "File {path} not found".format(
                    path=self.file_path
                )
            )

    def read_file(self):
        self.check_file_exist()
        with open(self.file_path, 'r') as fileo:
            return fileo.read()

    def to_md(self):
        pass
