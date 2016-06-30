myFile = open('F:\\python\\videoblocks\\test.txt', 'r', encoding = 'utf8')
lines = myFile.read()
links = []

count = 1

while(count > -1 ):
	count = lines.find('<a href="/member/bin/view/')
	if(count != -1):
		ind = count + 9
		ind2 = lines[ind:].find('"')
		ind2 = ind + ind2
		links.append(lines[ind:ind2])
		lines = lines[ind2:]

for index, item in enumerate(links):
	item = "http://www.videoblocks.com" + item
	links.remove(links[index])
	links.insert(index, item)


for i in links:
	print(i)
