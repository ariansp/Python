#read the position
a = "Hello, World!"
print(a[1])

#Loop the string position
for x in "banana":
  print(x)

#String length
b = "Hello, World!"
print(len(b))

#checking word in string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#checking word that not exist in a string
txt1 = "The best things in life are free!"
if "expensive" not in txt1:
  print("No, 'expensive' is NOT present.")

#get characters in certain position
b = "Hello, World!"
print(b[2:5])

#get character from start to certain position
b = "Hello, World!"
print(b[:5])

#get character from certain position to te end
b = "Hello, World!"
print(b[2:])

#lets assume [x:y]
#it's using negative, its mean to get from end to begin
#get character in x position to y position, but x will be (+1)
b = "Hello, World!"
print(b[-5:-2])