# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# Examples:
# pale, ple -> true
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false 

"""
Note that two strings cannot possibly be one edit distance away if they differ more than one in length.

Hence, we first check whether their lengths differ by 0 or 1.

If they are, then we begin iterating through each string at the same time, using pointers (say p1 and p2 for str1 and str2 respectively), counting the errors between the strings.

If there is an "error" encountered, then there are three ways to proceed:

If str1 is longer, then advance p1 by 1 and continue.
If str2 is longer, than advance p2 by 1 and continue.
If str1's length and str2's length are the same, then just continue iterating normally
"""

def one_away(str1, str2):
  str1_length = len(str1)
  str2_length = len(str2)
  length_difference = abs(str1_length - str2_length)
  
  if length_difference in [0,1]:
    errors = 0
    p1 = 0
    p2 = 0
    
    for _ in range(min(str1_length, str2_length)):
      if str1[p1] == str2[p2]:
        p1 += 1 
        p2 += 1 
      else:
        errors += 1
        if errors > 1:
          return False 
        if str1_length > str2_length:
          p1 += 1
        elif str2_length < str1_length:
          p2 += 1
        else:
          p1 += 1 
          p2 += 1
    return True
  else:
    return False
    
 """
 Time complexity: O(N)
   Counting string lengths is ~N, iterating through both strings is ~N
 Space complexity: O(1)
   We only keep track of at most ~5 variables whose sizes are independent of str1 and str2's lengths
 """
