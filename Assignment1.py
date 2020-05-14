input1 = "3141592653589793238462643383279502884197169399375105820974944592"
input2 = "2718281828459045235360287471352662497757247093699959574966967627"

# use karatsuba multiplication
n_2 = len(input1) / 2
n = 2 * n_2

a = int(input1[:n_2])
b = int(input1[n_2:])

c = int(input2[:n_2])
d = int(input2[n_2:])

ac = a*c
bd = b*d
ad = a*d
bc = b*c

res = 10**n * ac + 10**n_2 * (ad + bc) + bd
print(res)