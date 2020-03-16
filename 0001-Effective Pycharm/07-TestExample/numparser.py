def parse(txt):
    result = []

    for num in txt.split(','):
        if '-' in num:
            start, end = num.split('-')
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(num))

    return result
