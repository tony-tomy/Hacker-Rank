# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    k, m = map(int,input().split())
    l = []
    for i in range(int(k)):
        line = input().split()
        line = map(int, line)
        line.sort()
        l.append(line[-1]**2)
    print(l)
