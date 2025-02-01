def akhJoon(lst):
    flat_lst = [day for sublist in lst for day in sublist]
    missing_days = set(days) - set(flat_lst)
    return len(missing_days)

days = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]

lst = []
for i in range(3): 
    nums = int(input())
    day = input().split()
    lst.append(day)
print(akhJoon(lst))
