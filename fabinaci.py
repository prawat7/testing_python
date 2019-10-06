def fab(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

a=fab(9000)
print(a)
