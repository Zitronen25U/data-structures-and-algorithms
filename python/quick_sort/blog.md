# Python Sort, What is it?

- is a sorting algorithm that follows a "divide and conquer" method of sorting by selecting a pivot point. 

## How its done

- select a pivot point

You can select a pivot point based on the following. You can choose any of these as a pivot point:

- We can select the first element of the list as a pivot.
- We can select the last element of the list as a pivot.
- We can select some random element of the list as a pivot.
- Finally, we can select the median of the elements of the list as a pivot.

1. We will select a pivot point within a list

2. Using a partition, we will arrange all the items in the list so that all the values less than the pivot point, are on the left, and all of the values greater than the pivot are on the right

3. From there, the list gets split into two halves, that before the pivot, and that after

4. Using recursion, we will repeat step 2 through both halves of the list. 

The list should now be in order!

- 