import string
import random
message = input("enter message: ")
words = message.split(" ")
cd=input("enter 1 for code and 0 for decode: ")
cd = True if cd =="1" else False
if (cd):
  nmessage= []
  for word in words :
    if len(word) >= 3:
      r1=''.join(random.choices(string.ascii_letters , k=3 ))
      r2=''.join(random.choices(string.ascii_letters , k=3 ))
      code = r1+word[1:]+word[0]+r2
      nmessage.append(code)
      # print(nmessage)
    elif len(word) == 2:
      code = word[1]+word[0]
      nmessage.append(code)
    else:
      nmessage.append(word[0])
      # print(nmessage)
  print(" ".join(nmessage))
else:
  nmessage=[]
  for word in words:
    cd=True if len(word)>=3 else False
    if (cd):
      code=word[-4] + word[3:-4]
      nmessage.append(code)

    else :
      code=word[1]+word[0]
      nmessage.append(code)
    
  print (" ".join(nmessage))