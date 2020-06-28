import argparse

def create_args_parser():
    parser = argparse.ArgumentParser(description='Enterprise usernames wordlist generator')
    parser.add_argument('-i', nargs='?', help='input users file', required=True)
    parser.add_argument('-r', action='store_true', help='add reversed name and surname')
    parser.add_argument('-l', action='store_true', help='add lowercase')
    parser.add_argument('-u', action='store_true', help='add uppercase')
    parser.add_argument('-v', action='version', version='%(prog)s 1.0.0')
    return parser