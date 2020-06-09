import math
EPSILON = 10 ** (-6)

def original_f(x):
	return (math.sqrt(1 + math.atan(16.7 * x + 0.1))) / (math.cos(7 * x + 0.3))


def compute_w(x):
	t = 7 * x + 0.3
	sum = 1
	cur = 1
	n = 1
	while 1:
		cur *= t**2 / (2 * n - 4*n**2)
		n = n+1
		sum += cur
		if abs(cur) < EPSILON / 9:
			return sum + cur * t**2 / (2 * n - 4*n**2)


def compute_u(x):
	t = 16.7 * x + 0.1
	sum = t
	n = 1
	cur = (1 - 2*n)*(t**2)*t / (2*n + 1)
	while 1:
		sum += cur
		n = n+1
		cur *= (1 - 2 * n) * (t ** 2) / (2 * n + 1)
		if abs(cur) < EPSILON / 3:
			return 1 + sum + cur


def compute_f(x):
	k = 1
	ustar = compute_u(x)
	wstar = compute_w(x)
	while abs(geron(k, ustar) - geron(k - 1, ustar)) / wstar >= EPSILON / 3:
		k = k + 1
	result = geron(k + 1, ustar) / wstar
	return result


def geron(k, ustar):
	s0 = 1
	if k == 0:
		return s0
	else:
		return 0.5 * (geron(k - 1, ustar) + ustar / geron(k - 1, ustar))


def ifless(x, y):
	return abs(x - y) < EPSILON


def factorial(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res


for y in range(10, 55, 5):
	print('____________________','\nx=', y / 1000, '\nmy f=',  compute_f(y / 1000), '|| original f=',  original_f(y / 1000), '\n', 'Difference:', compute_f(y / 1000)-original_f(y / 1000), '\nDifference < 10^6 ???', ifless( compute_f(y / 1000),original_f(y / 1000)),'\n____________________')
	