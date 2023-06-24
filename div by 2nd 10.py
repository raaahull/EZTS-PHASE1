L2=[a for a in range(100,151)]
result = list(filter(lambda x: (x % 2 == 0), L2))
print("Numbers divisible by 2 are",result)
result = list(filter(lambda x: (x % 10 == 0), num_list))
print("Numbers divisible by 10 are",result)
