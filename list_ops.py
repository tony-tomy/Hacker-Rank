if __name__ == '__main__':
    N = int(input())
    out = []
    for _ in range(N):
        line = input().split()
        if line[0].lower() == 'insert':
            if len(out) <= int(line[1]):
                out.append(int(line[2]))
            else:
                out.insert(int(line[1]),int(line[2]))
        elif line[0].lower() == 'print':
            print(out)
        elif line[0].lower() == 'append':
            out.append(int(line[1]))
        elif line[0].lower() == 'sort':
            out.sort()
        elif line[0].lower() == 'pop':
            out.pop()
        elif line[0].lower() == 'reverse':
            out.reverse()
        elif line[0].lower() == 'remove':
            out.remove(int(line[1]))
        else:
            print("Wrong choice")
            
""" Sample code from discussion
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)
"""