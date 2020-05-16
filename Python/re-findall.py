import re
s = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(m or ['-1']))
