import timeit
# #Big O notes
# #(Big O asymtotic analysis)

# #What is good code?
# #1. Readable
# #2. Scalable - Speed & Memory

# #Linear Time
# #Example
# nemo = ['nemo']


# def find_nemo(x):
#     start = timeit.default_timer()
#     for string in x:
#         if string == 'nemo':
#             print("Found NEMO!")
#             stop = timeit.default_timer()
#             break  #Stops running, saves time/memory
#     print("Time: ", stop - start)


# find_nemo(nemo)

# #Run time with just nemo as an argument is very quick
# #If list was much larger, run time would be larger:
# large = nemo * 10000


# def find_nemo2(x):
#     #start = timeit.default_timer()
#     for string in x:
#         if string == 'nemo':
#             print("Found NEMO!")
#         #stop = timeit.default_timer()
#     #print("Time: ", stop - start)


# find_nemo2(large)

# #Run time is longer
# #Run time is relative to cpu
# #Big O is absolute
# #Big O for above is O(n) --> linear time

# #__________Constant__Time_______________________________

# #Example 1
# box_count = ["box", "box", "box"]


# def first_box(boxes):
#     print(boxes[0])


# #O(1) --> Constant Time


# #Example 2
# def two_boxes(boxes):
#     print(boxes[0])  #O(1)
#     print(boxes[1])  #O(1)


# #O(2)


# #Example 3
# def example_3(input):
#     a = 10  #O(1)
#     a = 50 + 3  #O(1)

#     for i in len(input):  #O(n)
#         # anotherFunction() #O(n)
#         stranger = True  #O(n)
#     return i  #O(1)


# # =O(3+3n) --> O(n)

# #______Rules_____
# #1. Worst Case
# #2. Remove Constants - Slope doesn't matter. Just the type of relation
# #3. Different terms for inputs - O(n) vs O(n+m), nested loops are O(n*m*...*count of nested loops) <-- Quadratic Time
# #4. Drop Non Dominants

# #_______________________________________________


# # Excercise 1: reverse a string
# def reverse(myStr):
#     result = " "
#     myStr = split(myStr)
#     reverse_string = []
#     str_length = len(myStr)
#     for i in range(str_length - 1, -1, -1):
#         reverse_string.append(myStr[i])

#     result = "".join(reverse_string)
#     return result


# def split(word):
#     return [char for char in word]


# print(reverse("hello"))

# #Excerise 2: combine 2 lists of ints and sort them


# def list_sort(list1, list2):
#     combined_list = list1 + list2
#     return sorted(combined_list)


# print(list_sort([1, 2, 3, 3], [2, 4, 5, 6, 2, 1, 7, 8]))


# #Excercise 3: print longest word in a sentence. Ignore non alpha characters
# def LongestWord(sen):
#     temp = "".join(x for x in sen if x.isalpha() or x == " ")
#     sen_split = temp.lower().split()
#     temp_longest = ""

#     for i in range(0, len(sen_split)):
#         if len(sen_split[i]) > len(temp_longest):
#             temp_longest = sen_split[i]
#     return temp_longest


# print(LongestWord(input()))

#_______________________________________________
#Array pros and cons:
#pros: fast lookup, fast push/pop, ordered
#cons: slow insert and delete


#_________________________________________
# Hash Tables Key Value pairs (Dictionary)
#O(1) for value insert, lookup, delete & search
#Collision slows lookup down by O(n) actually by O(n/k)

 
#Excercise 1: Given an array, return first recurring chracter

#You can brute force with nested for loops O(a*b)

#Or use temp values (comes to my mind first) only works if repeating numbers are consecutive
def temp_value_recur(array):
  temp_num = None
  for i in range(0, len(array)):
    if array[i] == temp_num:
      return(array[i])
    temp_num = array[i]
  return("none")
print(temp_value_recur([1,2,3,4,5,6,7,8]))

#Or use hash tables
def dict_recur(array):
  recur_dict = {}

  for i in array:
    if i in recur_dict:
      return i
    else:
      recur_dict[i] = array[i]
  return None
print(dict_recur([1,2,2,3]))

# The two above only work when in a certain order, you need clarification about what they want returned (first that appears vs first that repeats)

#Hash tables pros and cons:
#+Fast lookups (good collision resolution needed)
#+Fast inserts
#+flexible keys
#-unordered
#slow key iteration


#_______________________________________________
#Linked 
