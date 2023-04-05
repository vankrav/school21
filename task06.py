import re

str = input().lower()
str = re.sub(r'[.,"\'-?:!;]', '', str).split()

str = set(str)
str = sorted(list(str))
print(", ".join(str))