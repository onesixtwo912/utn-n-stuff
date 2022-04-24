for x in range (1,9):
	for y in range (9):
		for z in range (9):
			if x * 100 + y *10 + z == x**3 + y**3 + z**3:
				print(x * 100 + y *10 + z)

