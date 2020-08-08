#!/usr/bin/python3

import logging
import os

import usernamerules
import utils.argparsers as argparsers


DEFAULT_RULE_NAMES = ['simple', 'surname', 'name', 'partial_name_and_surname', 'name_and_partial_surname']


def __apply(rule_names, with_user_data, with_separator):
    usernames = set()
    for rule_name in rule_names:
        rule = getattr(usernamerules, rule_name)
        usernames.update(rule(with_user_data, with_separator))
    return usernames


def __produce_usernames_without_changes(for_users, rule_names, separator=''):
    no_changes_usernames = set()
    for user in for_users:
        user_data = user.split()
        no_changes_usernames.update(__apply(rule_names, user_data, separator))
    return no_changes_usernames


def __try_produce_usernames_reversed(for_users, rule_names, reverse, separator=''):
    reversed_usernames = set()
    if reverse:
        for user in for_users:
            user_data = user.split()
            user_data.reverse()
            reversed_usernames.update(__apply(rule_names, user_data, separator))
    return reversed_usernames


def __try_produce_rule_lowercase(usernames, lowercase):
    lowercase_usernames = set()
    if lowercase:
        lowercase_usernames = set([username.lower() for username in usernames])
    return lowercase_usernames


def __try_produce_rule_uppercase(usernames, uppercase):
    uppercase_usernames = set()
    if uppercase:
        uppercase_usernames = set([username.upper() for username in usernames])
    return uppercase_usernames


def __produce_without_separators(for_users, rule_names, reverse):
    usernames = set()

    no_changes_usernames = __produce_usernames_without_changes(for_users, rule_names)
    reversed_usernames = __try_produce_usernames_reversed(for_users, rule_names, reverse)
    usernames.update(no_changes_usernames)
    usernames.update(reversed_usernames)

    return usernames


def __produce_with_separators(for_users, rule_names, reverse, separators):
    usernames = set()

    for separator in separators:
        no_changes_usernames = __produce_usernames_without_changes(for_users, rule_names, separator)
        reversed_usernames = __try_produce_usernames_reversed(for_users, rule_names, reverse, separator)
        usernames.update(no_changes_usernames)
        usernames.update(reversed_usernames)

    return usernames


def get_users(from_file):
    users = []
    if not os.path.isfile(from_file):
        logging.error("File path {} does not exist.".format(from_file))
    else:
        with open(from_file, "r") as f:
            users = f.readlines()
    users = [user.strip() for user in users]
    return users


def produce_usernames(for_users, separators, rule_names=DEFAULT_RULE_NAMES, reverse=False,
                      lowercase=False, uppercase=False):
    base_usernames = set()
    base_usernames.update(__produce_without_separators(for_users, rule_names, reverse))
    base_usernames.update(__produce_with_separators(for_users, rule_names, reverse, separators))

    lowercase_usernames = __try_produce_rule_lowercase(base_usernames, lowercase)
    uppercase_usernames = __try_produce_rule_uppercase(base_usernames, uppercase)

    usernames = set()
    if lowercase:
        usernames.update(lowercase_usernames)
    elif uppercase:
        usernames.update(uppercase_usernames)
    else:
        usernames.update(base_usernames)

    return usernames


def main():
    logging.basicConfig(level=logging.INFO)

    arg_parser = argparsers.create_args_parser()
    script_args = arg_parser.parse_args()
    logging.log(level=logging.DEBUG, msg=str(script_args))

    users = get_users(script_args.i)
    usernames = produce_usernames(users, separators=script_args.s, reverse=script_args.r,
                                  lowercase=script_args.l, uppercase=script_args.u)

    for username in usernames:
        print(username)


if __name__ == "__main__":
    main()
