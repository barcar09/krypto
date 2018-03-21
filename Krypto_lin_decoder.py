from functools import reduce

def linear_congruential_generator(a, c, count_of_elements, first_el):   #   Function generationg pseudorandom number
    list_of_generator = []
    lcg_mod = 2 ** 31
    for el in range(count_of_elements):
        lcg_next = first_el * a + c;
        list_of_generator.append(lcg_next % lcg_mod)
        first_el = lcg_next
    return (list_of_generator)

def xgcd(b, n):     # Extended euclidan alghoritm  needed for modulo inversion
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def mulinv(b, n):   # Multi modulo inversion function
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n
def GCD(a,b):   # Great common dividor function
	while a != 0:
			a,b = b % a, a
	return b
def m_returner(list_of_el):     # Function returning m in (a*x +c) % m function 
    t = 0
    empty_sum_list = [s1 - s0 for s0, s1 in zip(list_of_el, list_of_el[1:])]
    u_list = [t2*t0 - t1*t1 for t0, t1, t2 in zip(empty_sum_list, empty_sum_list[1:], empty_sum_list[2:])]
    soln =  abs(reduce(GCD,u_list))
    return soln
def a_returner(list_of_el, modulus):     # Function returning a in (a*x +c) % m function 
    multiplier = (list_of_el[2] - list_of_el[1]) * mulinv(list_of_el[1] - list_of_el[0], modulus) % modulus
    # we use multi inverse a*x % m = 1,
    return multiplier
def c_returner(list_of_el,modulus,multiplier):   # Function returning c in (a*x +c) % m function 
     increment = (list_of_el[1] - list_of_el[0]*multiplier) % modulus
     return(increment)
for el in range(100):   # Simple test's
    list_of_el = linear_congruential_generator(67225,7382843,10,4324234)
    est=m_returner(list_of_el)
    a_ret = a_returner(list_of_el,est)
print(list_of_el)
print(est)
print(a_ret)
print(c_returner(list_of_el,est,a_ret))

# the gcd of two random multiples of m will 
# be m with probability 6/π2 = 0.61; and if you take the gcd of k of them, 
# this probability gets very close to 1 (exponentially fast in k)
# This decription code  working only for m = multiplicative of 2. 