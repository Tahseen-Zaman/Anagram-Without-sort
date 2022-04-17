def anagram(s1,s2):
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()
  #Checking if both string have same number of characters
  if len(s1) != len(s2):
   return False
  # count the frequency of each letter in string
  count = {}
  for letter in s1: # for every letter  in string
    if letter in count :
      count[letter] += 1
    else:
      count[letter] = 1
  for letter in s1: # for every letter  in string
    if letter in count :
      count[letter] -= 1
    else:
      count[letter] = 1
      
  for k in count:
    if count[k] != 0:
      return False
  return True    
x= anagram("Clint Eastwood","old west action")
print(x)