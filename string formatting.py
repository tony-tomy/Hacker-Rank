"""
format symbols

s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation

"""


n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))