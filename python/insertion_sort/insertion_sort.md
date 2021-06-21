```
( takes in an array of integers )
InsertionSort(int[] arr)
    ( For i in range(1, len(arr)) )
    FOR i = 1 to arr.length
        ( j = i -1 )
        int j <-- i - 1
        ( temp = arr[i] )
        int temp <-- arr[i]
        WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1
        arr[j + 1] <-- temp
```

## Algorithm:

- take in an list of integers

- for 1 to list length
    -assign j to i - 1
    -assign temp variable to list[i]
    -while j >= 0 **OR** temp is less than list[j]
        -arr[j] = arr[j+1]
        -j = j-1
    -temp = list[j+1]

### Round 1

- list = [8,4,23,42,16,15]

- for i in range(1, len(list)):
    -this equates to:
        -for i in range(1,6)

- feed the array into the function
- the for loop goes through the length of the array

- this makes i start at index 1, so i = 1

### Round 1.1

- make a temp variable equal to list[i]

- make a j variable equal to i-1

- in this round, temp = list[1]

### Round 1.2

- WHILE LOOP TIME

- while j >= 0 **and** temp is < list[j]
    -list[j+1] is equal to list[j]

