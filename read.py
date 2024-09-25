data = []
count = 0
good = []

print('loading...')

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 1000 == 0:
		# 	print(len(data))
print(len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(sum_len/len(data))

while True:
	look_for = input('word_include\n"-q" to quit\n')
	if look_for == '-q':
		break
	for d in data:
		if look_for == '-q':
			break
		elif look_for in d:
			good.append(d)
	print(len(good))

print('loading...')

wc = {}
for d in data:
	info = d.split()
	for word in info:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

times = input('show up over ___ times.\n"-q" to pass\n')
for word in wc:
	if times == '-q':
		break
	elif wc[word] > int(times):
		print(word, wc[word])

while True:
	word = input('input\ninput"-q" to quite\n')
	if word == '-q':
		break
	elif word in wc:
		print(word, 'show', wc[word], 'times')
	else:
		print('re-input\n')
