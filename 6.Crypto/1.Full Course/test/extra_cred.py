c1 = 3348898614019888901908403254933640035246212844961838831090198209986980794381721549119817432681384755697410365192319104804164099565189541033745677177908430898159000425144231080271489963068735078029094600990872466478190741629812176
e1 = 927497329847987298271115
n = 4035789025935566763434217693291904203514985559759202218772232737779637242777118595044390460183072421339720558176591333566629680159420540355202801063004396853930869779589477542063791290354739283500845851153515283182096350655220153
c2 = 239640052909589767377717332389707447467040807634556900631678847178249840124011908871933438491107613018104449557989400002181849114477870950132116542696807901617211160049032412890334084433427701567750018959947232564370889351855337
e2 = 123132131231124141411111

#https://crypto.stackexchange.com/questions/1614/rsa-cracking-the-same-message-is-sent-to-two-different-people-problem

from Crypto.Util.number import GCD, inverse

#Euclidean Algorithm, compute  gcd(e1,e2)
b = GCD(e1, e2)
print("gcd of e1, e2 is:  ",b)

#Extended Euclidean Algorithm, compute a, b
#stolen from FindModInverse in https://inventwithpython.com/cracking/
#  e1 * a + e2 * b = gcd(e1, e2) = 1
u1, u2, u3 = 1, 0, e1
v1, v2, v3 = 0, 1, e2
while v3 != 0:
    q = u3 // v3
    v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    a, b = u1, u2
print("Bézout coefficients:")
print("a = ", a,"b = ", b, "gcd = ", u3)
print("test e1 * a + e2 * b = 1")
print(e1*a + e2*b)

print ("compute i = Inverse(c2) mod n or c2^-1")
i =inverse(c2, n)
print(i)

print("\nmessage = c1^a * c2^b mod n")
print("since b < 0, use c2^b = c2^-1^-b = i^-b")
print("so message = c1^a * i^-b mod n\n")
message = pow(c1, a, n) * pow(i, -b, n) % n
print("The message integer is:")
print(message)
print("\nThe decoded message is:")
q = message
flag = []
while q > 0:
    qmod = q % 100
    if qmod < 30:
        flag.insert(0,chr(q % 1000))
        q = q // 1000
    else:
        flag.insert(0,chr(qmod))
        q = q // 100
print(''.join(flag))
