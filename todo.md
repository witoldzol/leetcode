1) max-pair-sum-in-an-array
# https://leetcode.com/problems/max-pair-sum-in-an-array/solutions/3902240/using-map-detailed-approach-and-easy-to-understand-code/
- [X] solve using brute force
- [X] optimize using hash maps
2) max sum sub array 
- [X] find a problem on leet code or in wild
- [X] BRUTE FORCE
- [X] implement caching in brute force ( use i,j=i,k = i..j) https://www.youtube.com/watch?v=5WZl3MMT0Eg
- [X]implement sliding window solution ( with two pinters - start of positive , and current max sub ending)
- [X] add indexes of start and end of subarray 
[Issues encountered:
I thought that it was a n^2 problem, but really, it is n^3 ( with some adjustments because each following iteration is smaller ) 
Then I didn't realise that numbers have to be consequtive, so when defining ranges, make sure that the range closes in from both left
and right side, example 1,2,3,4 => i would select 1, and then check 2,3,4|| 3,4 || 4 => what I needed to do was to check 2,3,4| 2,3 | 2
which means narrowing the range from the "right"|end side of the array, not left]
- [x] add tests
[python modules cant have dashes in their names! use underscore !!! doh]
- [X] solve it using divide and conquer method
- [X] implement divide and conquer again, 
 - XX debug the split in middle by indexes
- [X] revise the O(n) soution - re do it from memory
- [X] get a popular stack question ( queue with two stacks / one stack - using recursion? ) 
https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
- solve the balanced parens question

