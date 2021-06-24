
def partition(low, high, list):
    i = low -1 
    pivot = list[high]

    for j in range (low,high):
        if list[j] <= pivot:
            i = i+1
            list[i],list[j] = list[j],list[i]

    list[i+1],list[high] = list[high],list[i+1] 
    return (i+1) 


def quickSort(low,high,list): 
	if low < high: 

		part = partition(list,low,high) 

		quickSort(list, low, part-1) 
		quickSort(list, part+1, high) 
