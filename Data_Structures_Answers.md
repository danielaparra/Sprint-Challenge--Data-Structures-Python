Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    The time complexity is 0(n) since we traverse n number of nodes once.

2. What is the space complexity of your `depth_first_for_each` function?
    The space complexity is 0(h) where h is the height of the bst because the function recursively calls the branches of the tree and has to store it's place as it traverses depth first. 

3. What is the runtime complexity of your `breadth_first_for_each` method?
    The time complexity is 0(n) since we traverse n number of nodes once.

4. What is the space complexity of your `breadth_first_for_each` method?
    The space complexity is O(n/2) because that is the max number of items that will be in the given queue for the last row of a complete bst (worst case scenario). We can simplify that down O(n).

5. What is the runtime complexity of the provided code in `names.py`?
    It is a time complexity of O(n^2) assuming both names list are equal we can set them to n.

6. What is the space complexity of the provided code in `names.py`?
    It is a space complexity of O(2n + m) where m is the number of duplicates. But we can simplify that to O(2n) assuming the duplicates will be much smaller than the total number of names. And then we can simplify that to simply O(n)

7. What is the runtime complexity of your optimized code in `names.py`?
    It is a time complexity of 0(2n) or big O of 0(n).

8. What is the space complexity of your optimized code in `names.py`?
    It is a space complexity of 0(3n + m) where m is the no. of duplicates. Since m will be smaller than n, we can reduce that to O(3n). And then simplify that to 0(n)
