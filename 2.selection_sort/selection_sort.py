# 选择排序
class selectSort():
	def findMin(self, Arr):
		minIdx = 0
		min = Arr[minIdx]

		for i in range(1, len(Arr)):
			if Arr[i] < min:
				min = Arr[i]
				minIdx = i

		return minIdx

	def selectionSort(self, Arr):0
		newArr = []
		for i in range(0, len(Arr)):
			minIndx = self.findMin(Arr)
			newArr.append(Arr.pop(minIndx))
		return newArr


if __name__ == "__main__":
	sS = selectSort()
	myArr = [1, 6, 2, 5]
	mySortedArr = sS.selectionSort(myArr)
	print(mySortedArr)


