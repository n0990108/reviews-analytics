data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)	
print('每筆留言的平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100') 
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料包含"good"')
print(good[0])

good = [d for d in data if 'good' in d ]
bad = ['bad' in d for d in data]


# 文字計數
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] >= 500:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	elif word in wc:
		print(word, '出現過的次數為', wc[word], '次')
	else:
		print('這個字沒有出現過哦!')
print('感謝使用本查詢功能')
	








