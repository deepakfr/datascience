#!/usr/bin/env python
# coding: utf-8

# # Python Exercises
# Epita 2023 - Camille Duquesne

# **Important informations**
# * All the exercices are going to be graded automatically. 
# * Remember to fill in your name correctly.
# * If you delete cells that are commented as `#Do not delete` the automatic grading will directly award no points for that exercise.
# * Don't forget to remove `raise NotImplementedError()` if you code a solution for a function.
# * The name of the file should not be changed, otherwise the automatic grading will not see your sumbission and award 0.
# * Automatic plagiarism will also be run on your notebook.
# * As in any academic context, you should cite your sources and collaborators.

# In[ ]:


Name = '' 
Collaborators = ''


# ## Exercice 1 - 4 points
# Write a function called reverse that, given a non-negative integer (entered as argument), returns the digits of this number within an array in reverse order. For example with input 35231 reverse should give [1,3,2,5,3] and for input 0 reverse should give [0]. 

# In[ ]:


#Do not delete
def reverse(number):
    """Transform a non-negative integer into a list of its digits, 
    in reverse order.
    
    #######
    input: number (integer)
    output: reversed_numbers (list)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(reverse(123456))


# In[ ]:


#If this cell runs without any errors then it means your function works perfectly :) 
#Do not delete
assert reverse(35231) == [1,3,2,5,3]
assert reverse(0) == [0]
assert reverse(12345678910) == [0,1,9,8,7,6,5,4,3,2,1]
assert reverse(3333) == [3,3,3,3]
assert reverse(90) == [0,9]
assert reverse(7692537291635382) == [2,8,3,5,3,6,1,9,2,7,3,5,2,9,6,7]


# ## Exercice 2 - 4 points
# Write a function called pretty_word, that given a string, reverses the string and omits and non-alphabetic characters. For example, for input `'krishan'` `pretty_word('krishan')` should give `'nahsirk'` and for input `'ultr53o?n'` `pretty_word('ultr53o?n')` should give `'nortlu'`.

# In[ ]:


#Do not delete
def pretty_word(word):
    """Remove all non-letter characters from a string and reverse its character order.
    
    #######
    input: word (string)
    output: cleaned_word (string)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(pretty_word("ultr53o?n"))


# In[ ]:


#Do not delete
assert pretty_word("krishan") == "nahsirk"
assert pretty_word("ultr53o?n") == "nortlu"
assert pretty_word("") == ""
assert pretty_word("!*)[!&@)$*") == ""
assert pretty_word("uh(tucz§0") == "zcuthu"
assert pretty_word("Kl98i$*Poi") == "ioPilK"


# ## Exercice 3 - 6 points
# Write a function called `even_sorting` that, given an array of numbers, will sort the even numbers in ascending order while leaving the odd numbers at their original positions. 
# Examples:
# 
# [7, 1] => [7, 1]
# 
# [5, 8, 6, 3, 4] => [5, 4, 6, 3, 8]
# 
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] => [9, 0, 7, 2, 5, 4, 3, 6, 1, 8]

# In[ ]:


#Do not delete
def even_sorting(number_list):
    """Sort the even number of a list while leaving the odd numbers at the same position.
    
    #######
    input: number_list (list)
    output: sorted_list (list)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(even_sorting([1, 4, 5, 2, 8, 9, 2, 6]))


# In[ ]:


#Do not delete
assert even_sorting([7, 1]) == [7, 1]
assert even_sorting([5, 8, 6, 3, 4]) == [5, 4, 6, 3, 8]
assert even_sorting([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) ==  [9, 0, 7, 2, 5, 4, 3, 6, 1, 8]
assert even_sorting([5, 3, 1, 8, 0]) == [5, 3, 1, 0, 8]
assert even_sorting([]) == []
assert even_sorting([5, 3, 2, 8, 1, 4]) == [5, 3, 2, 4, 1, 8]


# ## Exercise 4 - 5 points
# Write a function named `cropped` that takes as input a list and an element and returns the list cropped after the second occurence of the given element.  
# Examples:    
# [1,2,3,4,5] and 2 => [1,2,3,4,5]     
# [1,2,5,2,5] and 2 => [1,2,5,2]   
# [1,5,5,4,5] and 5 => [1,5,5]    
# ['b', 'b', 'c'] and 'b' => ['b', 'b']  
# ['a', 'b', 'c'] and 8 => ['a', 'b', 'c']

# In[ ]:


#Do not delete
def cropped(list_to_crop, specific_element):
    """Crop a list based on a given element, after its second occurrence.
    
    #######
    input: list_to_crop (list)
           specific_element
    output: cropped_list (list)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(cropped([0, 3, 2, 0, 5, 0, 5], 0))
print(cropped([0, 3, 2, 0, 5, 0, 5], 5))


# In[ ]:


#Do not delete
assert cropped([1,2,2,4,5], 2) == [1,2, 2]
assert cropped([1,2,3,4,5], 3) == [1,2,3,4,5]
assert cropped([1,2,5,4,5], 5) == [1,2,5,4,5]
assert cropped([], 5) == []
assert cropped([5,5], 5) == [5,5]
assert cropped(['a','b','c','b','e','b','g','h'], 'b') == ['a','b','c','b']
assert cropped([1,2,3,4,5,6,7,8], 0) == [1,2,3,4,5,6,7,8]
assert cropped([1,8,3,14,2,0,36,14,301,38, 34], 14) == [1,8,3,14,2,0,36,14]
assert cropped(["apple", "apple", "banana", "orange", "grapes","melon"], "apple") == ["apple", "apple"]
assert cropped(["4", "4", "5", "4", "5"], 4) == ["4", "4", "5", "4", "5"]


# ## Exercice 5 - 4 points
# Write a function called `special_sum` that sums a list, but ignores
# any duplicate items in the list.
# 
# For instance, for the list [3, 4, 3, 6] , the function should return 10.    
# For the list [3, 4, 3, 3, 1] , the function should return 5.

# In[ ]:


#Do not delete
def special_sum(numbers_list):
    """
    Takes as argument numbers_list, a list of numbers, and sums each number that
    appears only once. Returns an integer.
    #######
    input: numbers_list (list)
    output: sum (integer)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(special_sum([3,4,3,6]))


# In[ ]:


#Do not delete
assert special_sum([3,4,3,6]) == 10
assert special_sum([3,4,3,3,1]) == 5
assert special_sum([1,1,3,3,2]) == 2
assert special_sum([6, 9, 5, 8, 0, 8, 7, 8, 9, 6, 9, 4, 2, 10, 10]) == 18
assert special_sum([2, 0, 8, 1, 9, 9, 6, 4, 3, 6, 6, 10, 4]) == 24
assert special_sum([]) == 0
assert special_sum([1, 9, 9, 5, 7, 7, 6, 1, 5, 6]) == 0
assert special_sum([0, 1, 4, 4, 0, 4, 2, 5, 9, 0, 10, 9, 0, 1, 2]) == 15
assert special_sum([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1]) == 21
assert special_sum([4, 7, 3, 7, 9, 0, 6, 1, 8, 5, 7, 8]) == 28


# ### Exercice 6 - 4 points
# Write a function called `square_digits` that squares every digit of a number and concatenates them.
# For example, if we run 9119 through the function, 811181 will come out, because 9 squared 2 is 81 and 1 squared 2 is 1.
# The function accepts an integer and returns an integer

# In[ ]:


#Do not delete
def square_digits(num):
    """
    Takes as argument num, an integer, squares each digit of the
    number and returns that number as an integer. 
    #######
    input: num (integer)
    output: num_squared_digits (integer)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(square_digits(9119))


# In[ ]:


#Do not delete
assert square_digits(9119) == 811181
assert square_digits( 2112 ) == 4114
assert square_digits( 0 ) == 0
assert square_digits( 6423 ) == 361649
assert square_digits( 5458 ) == 25162564
assert square_digits( 5136 ) == 251936
assert square_digits( 4983 ) == 1681649
assert square_digits( 5188 ) == 2516464


# ## Exercice 6 - 6 points
# Write a function that is called `pascal()` that will create the classic Pascal's triangle.
# Your function will get as argument the depth of the triangle and your code has to return the corresponding Pascal's triangle up to that depth.
# 
# The triangle should be returned as a nested array. For example:
# 
# `pascal(5) -> [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]`
# To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together, except for the edges, which are all 1. e.g.:
# 
# ```
#       1
#     1   1
#   1   2   1
# 1   3   3   1
# ```

# In[ ]:


#Do not delete
def pascal(depth):
    """
    Takes as argument the depth of the triangle and returns the corresponding Pascal's triangle, as a nested array
    up to the given depth.
    #######
    input: depth (integer)
    output: pascal_triangle (array)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(pascal(5))


# In[ ]:


#Do not delete
assert pascal(0) == []
assert pascal(1) == [[1]]
assert pascal(2) == [[1], [1, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1]]
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


# ## Exercise 7 - 2 points
# Write a function called `to_sha256` that converts a given ASCII string to its hexadecimal SHA-256 hash.    
# What is SHA-256 ? See the following link: https://www.n-able.com/blog/sha-256-encryption      
# For example the text `'hello'` has the following sha 256 value : `'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'`

# In[ ]:


#Do not delete
def to_sha256(text):
    """
    Takes a string as argument and returns it's SHA-256 value
    #######
    input: text (string)
    output: encrypted (string)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(to_sha256("hello"))


# In[ ]:


#Do not delete
assert to_sha256("hello") == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
assert to_sha256("bye") == 'b49f425a7e1f9cff3856329ada223f2f9d368f15a00cf48df16ca95986137fe8'
assert to_sha256("python") == '11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1'
assert to_sha256("What the hell is this SHA 256 nonesense !?!?") == '4fca3af3580954db3156650e5569af09cd71c54c6be82d0fd312fa34bc39938b'


# ## Exercice 8 - 2 points
# Write a function called `est_subsets` that, given a list of elements, where any element may occur more than once, returns the number of distinct subsets that do not contain a repeated element.
# For example ` est_subsets([1, 2, 3, 4])` should return `15` as the following possible distinct subsets are:
# `{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}}`

# In[ ]:


#Do not delete
def est_subsets(array):
    """
    Estimates the numbers of distinct subsets of a given list.
    #######
    input: array (list)
    output: num_subsets (int)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


est_subsets([1, 2, 3, 4])


# In[ ]:


#Do not delete
assert est_subsets([1, 2, 3, 4]) == 15 
assert est_subsets([1, 2, 3, 4, 3, 2]) == 15 
assert est_subsets(["a", "b", "c", "d"]) == 15 
assert est_subsets(["a", "b", "c", "d", "e"]) == 31 
assert est_subsets([11, 562, 12, 214, 2, 281, 2, 873, 93, 11]) == 255 
assert est_subsets([True, False, True, True, False]) == 3 
assert est_subsets([1]) == 1 
assert est_subsets([]) == 0 


# ## Exercice 9 - 4 points
# Write a function called `pairs` that splits a string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# 
# For example: `pairs('abc')` should return `['ab', 'c_']` and `pairs('abcdef')` should return `['ab', 'cd', 'ef']`

# In[ ]:


#Do not delete
def pairs(text):
    """
    Splits a string into pairs of two characters.  If the string has 
    an odd number of chracters the last pair will be completed with an
    underscore '_'.
    #######
    input: text (string)
    output: pairs_list (list)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(pairs('abc'))


# In[ ]:


#Do not delete
assert pairs('abc') == ['ab', 'c_']
assert pairs('abcdef') == ['ab', 'cd', 'ef']
assert pairs('hello') == ['he', 'll', 'o_']
assert pairs('good morning') == ['go', 'od', ' m', 'or', 'ni', 'ng']
assert pairs('testing diverse texts !') == ['te', 'st', 'in', 'g ', 'di', 've', 'rs', 'e ', 'te', 'xt', 's ', '!_']


# ## Exercice 10 - 3 points
# 
# Write a function called `modify_multiply` that will have the following behavior:
# 
# 1. The function takes a string as its first parameter. This string will be a string of words.
# 
# 2. You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the given string. The first word would be represented by 0.
# 
# 3. Once you have the located string you are finally going to multiply by it the third provided parameter, which will also be an integer. You are additionally required to add a hyphen in between each word.
# 
# So for example `modify_multiply("This is a string",3 ,5)` will return `"string-string-string-string-string"`
# 

# In[ ]:


# Do not delete
def modify_multiply(text, index, repetiton):
    """
    Retuns a formatted string with hyphens of the repetition of a word at a given index from 
    a text passed as argument.
    #######
    input: text (string)
           index (int)
           repetiton (int)
    output: word_rep (string)
    #######
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


print(modify_multiply("This is a string", 3, 5))


# In[ ]:


assert modify_multiply("This is a string", 3, 5) == "string-string-string-string-string"
assert modify_multiply("Welcome to this game", 2, 4) == "this-this-this-this"
assert modify_multiply("What a beautiful day", 1, 3) == "a-a-a"


# In[ ]:




