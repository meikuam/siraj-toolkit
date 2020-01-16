import sys
import argparse
sys.path.append('.')
sys.path.append('..')

from src.pandoc_cli import Converter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="path to text file containing text", type=str, default=None)
    args = parser.parse_args()
    if args.file is not None:

        path = args.file

        converter = Converter()
        converter.open(path)
        converter.save()
