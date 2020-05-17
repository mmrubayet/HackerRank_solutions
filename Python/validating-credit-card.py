import re
for _ in range(int(input())):
  s = input()
  try:
    assert re.search(r'^[456]\d{3}(-?\d{4}){3}$',s)
    s = re.sub('-','',s)
    assert not re.search(r'(\d)\1{3,}',s)
  except:
    print("Invalid")
  else:
    print("Valid")
