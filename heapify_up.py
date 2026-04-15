def heapifyDown(self, arr, ind):
    n = len(arr)

    largest_Ind = ind
    
    leftChild_Ind = 2*ind + 1
    rightChild_Ind = 2*ind + 2

    if leftChild_Ind < n and arr[leftChild_Ind] > arr(largest_Ind):
        largest_Ind = leftChild_Ind
    if rightChild_Ind < n and arr[rightChild_Ind] > arr(largest_Ind):
        largest_Ind = rightChild_Ind
    if largest_Ind != ind:
        arr[ind], arr[largest_Ind] = arr[largest_Ind], arr[ind]
        self.heapifyDown(arr, largest_Ind)