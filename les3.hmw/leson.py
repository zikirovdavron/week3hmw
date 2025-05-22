#task1
# def rememberlast():
#     b=None
#     def inner(a):
#         nonlocal b
#         print(f'last is {b}')
#         b=a
#         print(f'new is {b}')
#     return inner
# f=rememberlast()
# f(10)
# f(20)
#task2
# def limit(a):
#     cnt=0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         if cnt<=a:
#             print('Вызов выполнен')
#         else:
#             print('Лимит исчерпан')
#     return inner
# f=limit(2)
# f()
# f()
# f()
#task3
# def acum():
#     add=[]
#     def inner(a):
#         nonlocal add
#         add.append(a)
#         return add
#     return inner
# adlist = acum()
# print(adlist(5))   
# print(adlist(10))
#task4
# def stopwatch():
#     cnt=0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return f'{cnt} секунд прошло'
#     return inner
# timer=stopwatch()
# print(timer())
# print(timer())
# print(timer())
# print(timer())
# print(timer())
#task5
# def string_repeater(a):
#     def inner(b):
#         nonlocal a
#         return a*b
#     return inner
# repeat=string_repeater(1)
# print(repeat('hi'))
#task6
# def length_filter(a):
#     def inner(b):
#         if len(b)>a:
#             return True
#         else :
#             return False
#     return inner
# longer=length_filter(5)
# print(longer("Hello"))
# print(longer("Goodbye"))
#task7
# def personal_message(a):
#     def inner(b):
#         return f'{b}, {a}'
#     return inner
# say=personal_message('John')
# print(say('Welcome'))
#task8
# def pas(a,b):
#     def inner(c):
#         return f'{a}{c}{b}'
#     return inner
# password=pas('user_','_2025')
# print(password('secure'))
#task9
# def count(a):
#     def inner(b):
#         s=b-(b*a/100)
#         return s
#     return inner
# coun=count(10)
# print(coun(200))