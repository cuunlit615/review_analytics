data = []
count = 0
good = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print(len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print(sum_len/len(data))
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))