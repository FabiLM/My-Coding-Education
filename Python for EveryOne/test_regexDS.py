import

def result():
    s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'

    result = []
    # complete the pattern below
    pattern = '''(\S)([A]{3})'''
    for item in re.finditer(pattern, s):
      # identify the group number below.
      result.append(item.group(1))

    return print(result)

result()
