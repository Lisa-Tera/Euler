
num = '0123456789'
i = len(num)-2
while i >= 0:
    if num[i] < num[i+1]:
        t = sorted(num[i:])
        new_num = t.pop(t.index(num[i])+1)
        last_nums = ''.join(t)
        a =num[:i] + new_num + last_nums




'''
def get_next_permutation(string):
    i=len(string)-2
    while i >= 0:
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''.join(target)
            return string[:i] + new_num + last_nums
        i-=1
 
string='0123456789'
for i in range(1,1000000):    
    string = get_next_permutation(string)
print(string)






def lexico(s='', n=[str(i) for i in range(10)]):

    l = []
    for i in n:
        l += lexico(s + str(i), list(set(n) - {i}))

    if not len(n): return [s]

    return l

print(sorted(lexico())[999999])
'''