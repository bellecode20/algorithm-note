stack = ['a', 'b', 'c', 'd', 'e']
m = 3

del stack[-m:]
print(stack)  # ['a', 'b']


lst = [1, 2, 3, 4, 5, 6]

del lst[1:4]   # 인덱스 1~3 삭제
print(lst)     # [1, 5, 6]

del lst[:2]    # 앞에서 2개 삭제
del lst[-2:]   # 뒤에서 2개 삭제