import string
list1=[]
def abs_letter(word):
  for letter in word:
    list1.append(letter)
    list2=list(string.ascii_lowercase)
    numbers=["1","2","3","4","5","6","7","8","9","10"]
    list2.extend(numbers)
  for item in list2[:]:
    if item in list1:
      list2.remove(item)
  print("".join(list2))
  
abs_letter("congratulations132")
