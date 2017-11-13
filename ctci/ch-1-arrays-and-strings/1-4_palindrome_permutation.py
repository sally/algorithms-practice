# Given a string, write a function to check if it is a permutation of palindrome. A palindrome is a word or phrase that is the same forwards as backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# Example:
# Input: "Tact Coa"
# Output: True (permutations: "taco cat", "atco cta", etc.)

"""
INITIAL NOTES:
It seems that spaces are not counted in 'being a palindrome', as well as capitalization.

Therefore, in whatever strategy we implement, we will first (1) downcase the input string and (2) resolve to ignore spaces in our solution.
"""

"""
PSEUDOCODE:

We note that a string is a palindrome if and only if it only has only one character that occurs an odd number of times.

Therefore, it suffices for us to iterate through the string and keep track of (1) the number of occurrences of each character and (2) the number of characters that occur an odd number of times.

If at the end, our (2) variable exceeds 1, then we return false. Else, we return true.
"""

from collections import defaultdict 

def is_palindrome_permutation(str):
  char_occurrences = defaultdict(lambda: 0)
  num_odd_occurrences = 0
  
  str = str.lower()
  
  for char in str:
    if char != " ":
      char_occurrences[char] += 1
      if char_occurrences[char] % 2 == 0 and num_odd_occurrences > 0:
        num_odd_occurrences -= 1
      else:
       num_odd_occurrences += 1
      
  if num_odd_occurrences > 1:
    return False
  else:
    return True
  
  """
  Time complexity: O(N)
    Iterating through the string once costs N operations
  Space complexity: O(N)
    Worse case, the string itself is made out of N different characters, which means that the histogram hash will have N key/value pairs in it
  """
