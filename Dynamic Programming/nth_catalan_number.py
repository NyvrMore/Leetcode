def catalanNumbers(n, d):
	if n == 0 or n == 1:
		d[n] = 1
	if n not in d:
		s = 0
		for i in range(n):
			s += catalanNumbers(i, d) * catalanNumbers(n - i - 1, d)
		d[n] = s
		
	return d[n]

	discord.gg/968syvf