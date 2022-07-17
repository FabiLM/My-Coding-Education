import re
fname = input('Enter file name:')
fh = open(fname)
logdata = fh.read()
def logs() :

    host = re.findall('[\d]+\.[\d]+\.[\d]+\.[\d]+', logdata)
    user_name = re.findall('([a-z-]\S*)(\[)', logdata)
    time = re.findall('\[[\d].+[\d]\]',logdata)
    request = re.findall('["].+["]', logdata)

    pattern = '''
    (?P<host>[\d]*\.[\d]*\.[\d]*\.[\d]*)
    (\ -\ )
    (?P<user_name>[\w-]*)
    (\[)
    (?P<time>\w*/\w*/.*)
    (\]\ \")
    (?P<request>.*)
    (")
    '''

    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())

    return result


logs()
