import utils.stringutils as stringutils

def name_and_partial_surname(user_data, with_separator=''):
    name = user_data[0]
    surname = user_data[-1]
    for prefix_length in range(1,len(surname)):
        yield ''.join([name, with_separator, stringutils.prefix(surname, prefix_length)])