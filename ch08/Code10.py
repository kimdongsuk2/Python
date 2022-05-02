# ss = '   파     이    썬   '
# ss.strip()
# ss.rstrip()
# ss.lstrip()
#
# print(ss)
# print(ss.strip())
# print(ss.rstrip())
# print(ss.lstrip())

# ss = '----파---이---썬----'
# print(ss.strip('-'))
# ss = '<<<파<<이>>썬>>>'
# print(ss.strip('<>'))
ss = input("입력 문자열 ==> ")

print("출력 문자열 ==>", end='')
for i in  range(0,len(ss)):
    if ss[i] !='o' :
        print(ss[i],end='')
    else:
        print('$',end='')

