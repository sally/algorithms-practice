"""
  Implement a method to perform basic string compression using
  the counts of repeated characters. For example, the string aabcccccaaa
  would become a2b1c5a3. If the "compressed" string would not become
  smaller than the original string, your method should return the original string.
"""

# questions off the bat: What should it return for empty string? Just empty string, I suppose

# since we have to know how long the return string is vs the original string, we must keep track of both lengths 

# we will iterate through the original string, set first letter as "previous letter"

# we also institute a "current count" of how many times the character occurs, so in this case we would increment "current letter" count from 0 to 1

# we will then move on: the next letter is scrutinized.
  # if it is equal to "previous letter", then we increment the current count by 1 and move on
  # if it is not equal to the "previous letter", then we
    # 1. concatenate the "previous letter" to the return string
    # 2. concatenate the "current count" converted to a string to the return string 
    # 3. increment the "return string length" variable by 2
    # 4. reset the "current count" to 1
    # 5. set the current letter as "previous letter"
  
# repeat step above ^ (until string is done)

# now compare lengths (that we have been keeping track of) of the return string and the original string, and return the shorter one

"""
Big O Analysis:
  Space: the worst case is that the string could have all unique letters (like abc) which would end up making our return string have length 2N (a1b1c1) -- so it's O(N)
  Time: we must iterate through the given string at least once, so it's O(N)
"""
