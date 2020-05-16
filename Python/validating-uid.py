import re
def valid(uid):
    if len(uid) != 10:
        return 'Invalid'
    else:
        if  not re.search(r'.*[A-Z].*[A-Z].*', uid):
            return 'Invalid'
        if not re.search(r'.*\d.*\d.*\d.*', uid):
            return 'Invalid'
        if not re.search(r'[a-zA-Z\d]{10}', uid):
            return 'Invalid'
        if re.search(r'(.).*\1', uid):
            return 'Invalid'
        return 'Valid'

for _ in range(int(input())):
    s = input()
    print(valid(s))
