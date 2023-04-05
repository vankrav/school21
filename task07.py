import re
a =[]
k = 0
str = input().lower()
str = re.sub(r'[.,"\'-?:!;]', '', str).split()

b = {}
for i in str:
    for j in str:
        if i == j:
            k+=1
    a.append(k)
    k = 0
for i in range(len(str)):
    b[str[i]] = a[i]
b = sorted(b.items(), reverse=True, key=lambda item: item[1])

for i in range(3):
  print(b[i][0], ": ", b[i][1])

