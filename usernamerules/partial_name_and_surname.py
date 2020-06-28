import utils.stringutils as stringutils

def partial_name_and_surname(user_data, with_separator=''):
    name = user_data[0]
    surname = user_data[-1]
    for prefix_length in range(1,len(name)):
        yield ''.join([stringutils.prefix(name, prefix_length), surname])