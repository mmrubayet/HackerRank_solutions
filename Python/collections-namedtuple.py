from collections import namedtuple
(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
print(f'{sum([float(Grade._make(input().split()).MARKS) for _ in range(n)])/n:.2f}')
