def make_rows(tags, cnt=4):
	rows = [[]]
	counter = 0
	for t in tags:
		if counter == cnt:
			counter = 0
			rows.append([])

		counter += 1
		rows[-1].append(t)
	return rows