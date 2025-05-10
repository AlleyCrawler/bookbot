def book_wc(text):
        book_split = text.split()
        split_count = len(book_split)
        return split_count

def book_char(text):
	book_lc=text.lower()
	count = {}
	for char in book_lc:
		if char in count:
			count[char] +=1
		else:
			count[char] =1
	return count

def char_sort(char_count):
	char_list = []

	for char,count in char_count.items():
		char_dict={"char":char,"num":count}
		char_list.append(char_dict)

	def sort_on(dict):
		return dict["num"]

	char_list.sort(reverse=True,key=sort_on)
	return char_list
