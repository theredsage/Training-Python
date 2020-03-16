def parse(txt):
    '''
    Parse a string and convert it to a list of integers
    TODO - Add space support
    '''
    result = []

    for num in txt.split(','):
        if '-' in num:
            start, end = num.split('-')
            # fixme - support half open interval
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(num))

    return result
