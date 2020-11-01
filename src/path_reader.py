import argparse


class PathReader:
    def __init__(self, log):
        self.log = log

    def read(self):
        self.log.info('Parsing the filepath.')

        parser = argparse.ArgumentParser(description='Parse args from console.')
        parser.add_argument('--filepath', type=str, required=True, help='Path to images.')
        args = parser.parse_args()
        return args.filepath
