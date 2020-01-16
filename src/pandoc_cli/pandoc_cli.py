import os
import subprocess
import pypandoc


class Converter:

    def __init__(self, inner_format='md'):
        self.inner_format = inner_format
        self.inner_path = None

        self.input_format = None
        self.input_path = None

        self.output_path = None

        self.dirname = None
        self.filename = None

    def open(self, path):
        self.input_path = path
        # print("input_path:", self.input_path)

        self.dirname = os.path.dirname(self.input_path)
        # print("dirname:", self.dirname)

        self.filename, self.input_format = os.path.splitext(os.path.basename(self.input_path))
        self.input_format = self.input_format[1:]
        # print("filename", self.filename, "input_format", self.input_format)

        self.inner_path = os.path.join(self.dirname, self.filename + '.' + self.inner_format)
        # print("inner_path", self.inner_path)

        output = pypandoc.convert_file(self.input_path, self.inner_format, outputfile=self.inner_path)
        assert output == '', print(output)

    def save(self, suffix="_mine"):
        self.output_path = os.path.join(self.dirname, self.filename + suffix + '.' + self.input_format)
        output = pypandoc.convert_file(self.inner_path, self.input_format, outputfile=self.output_path)
        assert output == '', print(output)
