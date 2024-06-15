from array import *
print("Step  1")
#Create an array and travesse
arrays = array('i', [1,2,3,4,5,6,7,8,9,10])
def traverse(arrays):
  for i in range(len(arrays)):
    print(arrays[i])
traverse(arrays)    
#accesing the element
print("step2")
print(arrays[2])
#appending the element
print("step3")
arrays.append(11)
print(arrays)
#inserting the elements
print("step4")
arrays.insert(11,12)
print(arrays)
#extend property
print("step5")
arrays2 = array('i',[13,14,15])
arrays.extend(arrays2)
print(arrays)
print("step6")
#Adding elements from list into arrays using fromlist() function
temp = [16,17,18,19]
arrays.fromlist(temp)
print(arrays)
print("step 7")
#removing elements from an array
arrays.remove(19)
print(arrays)
print("step 8")
#removing elements using pop function
arrays.pop()
print(arrays)
print("step 9")
#fetching the index of the element
print(arrays.index(14))
print("step 10")
#reversing an element
arrays.reverse()
print(arrays)
print("step 11")
#using buffer info() method
print(arrays.buffer_info())
print("step 12")
#counting the elements
arrays.append(1)
print(arrays.count(1))
print("step 13")
#converting values into tolist method
print(arrays.tolist())
#using slicing method
print("step 14")
print(arrays[1:4])
print(arrays[4:])
print(arrays[:4])
print(arrays[:])





