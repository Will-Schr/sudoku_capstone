# pylint: skip-file
tester = [[1,2,3,4,5,6],[1,2],[4,5,6],[1,2],[3,5,9,2]]

nav_lst = list(range(5))
while (nav_lst):
    first_lst = tester[nav_lst[0]]
    nav_lst.pop(0)
    if (nav_lst == False):
        continue
    for x in nav_lst:
        if (tester[x] == first_lst):
            for j in range(5):
                if tester[j] != first_lst:
                    tester[j] = [g for g in tester[j] if g not in first_lst]
            nav_lst.remove(x)
print(tester)
