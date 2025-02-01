def haftsang(lst, x):
  tol = len(lst)
  for i in range(len(lst)):
    if lst[i] == x:
      y = i
  if y == 0:
      return 6
  else:
      return (tol - y)

lst = list(map(int, input().split()))
x = int(input())
print(haftsang(lst, x))
print("salam")
print("test 222")


