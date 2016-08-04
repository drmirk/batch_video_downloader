'''gets all the folder names in a list '''

def folder_names():
	save_source = driver.page_source
	links = []
	count = 1
	while(count > -1 ):
		count = save_source.find('<a href="/member/bin/view/')
		if(count != -1):
			ind = count + 9
			ind2 = save_source[ind:].find('"')
			ind2 = ind + ind2
			links.append(save_source[ind:ind2])
			save_source = save_source[ind2:]
	for index, item in enumerate(links):
		item = "http://www.videoblocks.com" + item
		links.remove(links[index])
		links.insert(index, item)
