Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    The time complexity is 0(n) since we traverse n number of nodes once.

2. What is the space complexity of your `depth_first_for_each` function?
    The space complexity was 0(n) because the cb function that was passed into the functions for testing. Otherwise it would be O(1).

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
    It is a time complexity of O(n^2) assuming both names list are equal we can set them to n.

6. What is the space complexity of the provided code in `names.py`?
    It is a space complexity of O(2n + m) where m is the number of duplicates. But we can simplify that to O(2n) assuming the duplicates will be much smaller than the total number of names.

7. What is the runtime complexity of your optimized code in `names.py`?
    It is a time complexity of 0(2n) or big O of 0(n).

8. What is the space complexity of your optimized code in `names.py`?
    It is a space complexity of 0(3n + m) where m is the no. of duplicates. Since m will be smaller than n, we can reduce that to O(3n).
