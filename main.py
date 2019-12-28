import timeit
#Big O notes
#(Big O asymtotic analysis)

#What is good code?
#1. Readable
#2. Scalable - Speed & Memory

#Linear Time
#Example 
nemo = ['nemo']

def find_nemo(x):
  start = timeit.default_timer()
  for string in x:
    if string == 'nemo':
      print("Found NEMO!")
      stop = timeit.default_timer()
      break #Stops running, saves time/memory
  print("Time: ", stop - start)
find_nemo(nemo)

#Run time with just nemo as an argument is very quick
#If list was much larger, run time would be larger:
large = nemo * 10000
def find_nemo2(x):
  #start = timeit.default_timer()
  for string in x:
    if string == 'nemo':
      print("Found NEMO!")
     #stop = timeit.default_timer()
  #print("Time: ", stop - start)
find_nemo2(large)     

#Run time is longer
#Run time is relative to cpu
#Big O is absolute 
#Big O for above is O(n) --> linear time


#__________Constant__Time_______________________________


#Example 1
box_count = ["box","box","box"]
def first_box(boxes):
  print(boxes[0])
#O(1) --> Constant Time

#Example 2
def two_boxes(boxes):
  print(boxes[0]) #O(1)
  print(boxes[1]) #O(1)
#O(2)

#Example 3
def example_3(input):
  a=10 #O(1)
  a=50+3 #O(1)

  for i in len(input): #O(n)
    # anotherFunction() #O(n)
    stranger = True #O(n)
  return i #O(1)
# =O(3+3n) --> O(n)

#______Rules_____
#1. Worst Case
#2. Remove Constants - Slope doesn't matter. Just the type of relation 
#3. Different terms for inputs - O(n) vs O(n+m), nested loops are O(n*m*...*count of nested loops) <-- Quadratic Time
#4. Drop Non Dominants

#_______________________________________________

# Excercise 1: reverse a string
def reverse(myStr):
  result = " "
  myStr = split(myStr)
  reverse_string = []
  str_length = len(myStr)
  for i in range(str_length-1, -1, -1):
    reverse_string.append(myStr[i])
    
  result = "".join(reverse_string)
  return result

def split(word):
  return [char for char in word]

print(reverse("hello"))
