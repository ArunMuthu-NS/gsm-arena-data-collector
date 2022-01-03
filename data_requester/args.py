import argparse


def parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--data-path', dest='data_path', type=str, required=True)
    arg_parser.add_argument('--brand', dest='brand', type=str, required=True)
    arg_parser.add_argument('--sleep', dest='sleep', type=int, default=120)
    arg_parser.add_argument('--page-size', dest='page_size', type=int, default=None)
    return arg_parser
