arr= [0,0,0,0,0]
for i in range(5):
    arr[i] = int(input())
arr = sorted(arr, reverse=True)
for i in arr:
  print(i)
