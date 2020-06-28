#!/usr/bin/python3

import logging
import os

import usernamerules
import utils.argparsers as argparsers

def __apply__(rule_names, with_user_data):
    usernames = set()
    for rule_name in rule_names:
            rule = getattr(usernamerules, rule_name)
            usernames.update(rule(with_user_data))
    return usernames

def __try_apply_rule_reverse__(rule_names, with_user_data, reverse):
    usernames = set()
    if reverse:
        with_user_data.reverse()
        usernames = __apply__(rule_names, with_user_data)
    return usernames

def __try_apply_rule_lowercase__(usernames, lowercase):
    lowercase_usernames = set()
    if lowercase:       
        lowercase_usernames = set([username.lower() for username in usernames])
    return lowercase_usernames

def __try_apply_rule_uppercase__(usernames, uppercase):
    uppercase_usernames = set()
    if uppercase:       
        uppercase_usernames = set([username.upper() for username in usernames])
    return uppercase_usernames

def get_users(from_file):
    users = []
    if not os.path.isfile(from_file):
       logging.error("File path {} does not exist.".format(from_file))
    else:
        with open(from_file, "r") as f:
            users = f.readlines()
    users = [user.strip() for user in users]
    return users

def default_rule_names():
    return ['simple', 'surname', 'name', 'partial_name_and_surname', 'name_and_partial_surname']

def produce_usernames(for_users, rule_names=default_rule_names(), reverse=True, lowercase=True, uppercase=True):
    usernames = set()
    for user in for_users:
        user_data = user.split()
        usernames.update(__apply__(rule_names, user_data))
        usernames.update(__try_apply_rule_reverse__(rule_names, user_data, reverse))
    
    lowercase_usernames = __try_apply_rule_lowercase__(usernames, lowercase)
    uppercase_usernames = __try_apply_rule_uppercase__(usernames, uppercase)

    usernames.update(lowercase_usernames)
    usernames.update(uppercase_usernames)

    return usernames

def main():
    logging.basicConfig(level=logging.INFO)
    
    arg_parser = argparsers.create_args_parser()
    script_args = arg_parser.parse_args()
    logging.log(level=logging.DEBUG, msg=str(script_args))

    users = get_users(script_args.i)
    usernames = produce_usernames(users)
    
    for username in usernames:
        print(username)

if __name__ == "__main__":
    main()