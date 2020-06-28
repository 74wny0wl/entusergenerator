import argparse

def create_args_parser():
    parser = argparse.ArgumentParser(description='Enterprise usernames wordlist generator')
    parser.add_argument('-i', nargs='?', help='input user file', required=True)
    parser.add_argument('-v', action='version', version='%(prog)s 1.0.0')
    return parser