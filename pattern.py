
""" code
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

input 

7 21

output

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

"""
n,m = map(int, raw_input().split())
pattern = [((".|.")*((2*i)+1)).center(m,"-") for i in range(n//2)]
print("\n".join(pattern))
print("welcome".center(m,"-"))
print("\n".join(pattern[::-1]))