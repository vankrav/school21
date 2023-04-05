
import re

str = input()
str = re.sub(r'[.,"\'-?:!;]', '', str).split()
pod_str = input()

for i in str:
    if pod_str in i:
        print(i)