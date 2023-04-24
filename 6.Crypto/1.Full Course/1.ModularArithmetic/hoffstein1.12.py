from Crypto.Util.number import GCD
def gcdprob(a, b):
    u = 1
    g = a
    x = 0
    y = b
    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x
        u = x
        g = y
        x = s
        y = t
    v = (g - a * u) // b
    return (g, u, v)

a = 3892394
b = 239847
g, u, v = gcdprob(a, b)
print(g, u, v)
print (GCD(a, b))

print(str(a) + ' * ' + str(u) + '  ' + str(b) + ' * ' + str(v))
print(a*u+v*b)
