#LOOP AND THEIR PROBLEM SOLVING BY HITESH SIR
#1. numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count=0
# for num in numbers:
#     if num > 0:
#       positive_number_count+=1

#2. print("Final Count Of Positive Number: ",positive_number_count)
# n=10
# num=0
# for i in range(1,n+1):
#     if i%2==0:
#         num+=1
# print("the total even number is ",num)

#3. number=6
# for i in range(1,11):
#     if i==6:
#         continue
#     print(number,'X',i,'=',number*i)

# input="Python"
# reversed=""

# for char in input:
#     reversed=char + reversed
#     print(reversed)

# input="treecode"
# for char in input:
#     print(char)
#     if input.count(char)==1:
#       
#   print
# ("char is:",char)
#         break

# number=6
# factorial=1
# while number>0:
#  factorial=factorial*number
#  number=number-1
#  print("FACTORIAL ",factorial)

# while True:
#     number=int(input("Enter the number b/w 1 and 10:"))
#     if 1<=number<=10:
#         print("thanks")
#         break
#     else:
#         print("invalid number , try again")


# number = 29

# is_prime=True

# if number >1:
#     for i in range(2,number):
#         if(number%i)==0:
#             is_prime=False
#             break
# print(is_prime)


# items=["Mango","Banana","Apple","Orange","Apple"]

# unique_item=set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate ",item)
#         break
#     unique_item.add(item)


import time

wait_time=1
max_retries=5
attempts=0

while attempts<max_retries:
    print("ATTEMPTS",attempts+1,"- wait times",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1
























































# def word_pattern(pattern, s):
#     words = s.split()

#     if len(pattern) != len(words):
#         return False

#     char_to_word = {}
#     word_to_char = {}

#     for char, word in zip(pattern, words):
#         if char in char_to_word and char_to_word[char] != word:
#             return False
#         if word in word_to_char and word_to_char[word] != char:
#             return False

#         char_to_word[char] = word
#         word_to_char[word] = char

#     return True

# print(word_pattern("abba", "dog cat cat dog"))  
# print(word_pattern("abba", "dog cat cat fish")) 
# print(word_pattern("aaaa", "dog cat cat dog"))  


# def longest_palindrome(s):
#     count = {}

#     for char in s:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1

#     palindrome_length = 0

#     odd_found = False


#     for freq in count.values():
        
#         if freq % 2 == 0:
#             palindrome_length += freq
#         else:
            
#             palindrome_length += freq - 1
#             odd_found = True  

    
#     if odd_found:
#         palindrome_length += 1

#     return palindrome_length


# print(longest_palindrome("abccccdd"))  
# print(longest_palindrome("a"))        

