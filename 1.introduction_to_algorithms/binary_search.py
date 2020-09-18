class BinarySearch():

	# 简单二分搜索
	def search_iterative(self, list, item):
		# track the list by low and high
		low = 0
		high = len(list) - 1

		# when you haven't narrowed it , down to the next
		while low <= high:
			mid = (low + high) // 2
			guess = list[mid]  # num found
			# compare
			if guess == item:
				return  mid
			if guess > item:
				high = mid - 1
			else:
				low = mid + 1

		# 不存在item
		return None

	# 自我迭代
	def search_recruise(self, list, low, high, item):
		if high > low:
			mid = (high + low) // 2
			guess = list[mid]

			if guess == item:
				return mid
			elif guess > item:
				return self.search_recruise(list, low, mid-1, item)
			else:
				return  self.search_recruise( list, mid, high, item)

		else:
			return None


	# initial
if __name__ == "__main__":
	bs = BinarySearch()
	my_list = [1, 3, 5, 7,9]

	print(bs.search_iterative(my_list, 3))  # =>结果应该为1
	print(bs.search_recruise(my_list, 0, 4,-1))	# =>结果应该为None