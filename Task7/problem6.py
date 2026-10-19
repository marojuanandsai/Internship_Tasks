def pangrams(s):
  lettres=set(s.lower())
  alphabets=set("abcdefghijklmnopqrstuvwxyz")

  if alphabet.issubset(letters):
    return "pangram"
  else:
    return "not pangram"
    

s = input()
print(pangrams(s))  
    
