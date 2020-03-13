"""
print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

or

print("".join(map(str.swapcase, input())))

or 

print(input().swapcase())
"""
def swap_case(s):
    o = ""
    for i in range(len(s)):
        if s[i].islower():
            o += s[i].upper()
        elif s[i].isupper():
            o += s[i].lower()
        else:
            o += s[i]

    return o

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)