import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt','r') as f:
 	for line in f:
 		data.append(line)
 		count += 1 #count =  count + 1
 		bar.update(count)
print('檔案讀取完了，總共有',len(data),'筆資料')

print(data[0]) 

#文字計數
start_time = time.time() #紀錄系統時間，單位是秒
wc = {} #word_count
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, '秒')

print(len(wc))


while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in words:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('沒有出現過喔')

print('感謝使用本查詢功能')

# a = 0
# for d in data:
# 	a = a + len(d)
# 	b = a / len(data) 
# print(b)
# print('留言的平均長度為', b)
# new = []
# for e in data:
# 	if len(e) < 100:
# 		new.append(e)
# print('一共有', len(new) , '筆留言長度小於100')
# print(new[0])

#good= []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆提到good')

