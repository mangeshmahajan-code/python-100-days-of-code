import random
pointofx=0
pointofy=0
print("let's play rock,paper,scissors\n".center(50))
# words= ["choose : rock,paper,scissors"]
z={"rock":"paper","paper":"scissors","scissors":"rock"}
m=input("do you want to play with computer or friend?\nfor computer press 1\nfor friend press 2\nyour choise is:")
while m=="1":
 x=input("choose:rock,paper,scissors or quit?:")
 y=random.choice(["rock","paper" ,"scissors"])
 print(f"my choise is :{y}")
 point=0
 if x==z[y]: 
  print ("you win")
  point=point+1
  print("your point is",point)
 elif x==y:
  print("tie")
  point=point
  print("your point is",point)
 elif x!=z[y] :
  print("you lose")
  point=point-1
  print("your point is",point)
  
else:
   


  # while True:
# else :
  
  try:
    while m=="2":
      name1=input ("enter your name:")
      x=input("choose : rock,paper,scissors :")
      y=input("choose : rock,paper,scissors :")
      if y==z[x]:
        print ("x win")
        pointofx +=1
        print(f"point of {name1} is:",pointofx)
        print(f"point of {name2} is:",pointofy)
      elif x==z[y]:
        print ("y win")
        pointofy+=1
        print("point of x is",pointofx)
        print("point of y is",pointofy)
      elif x==y:
        print("tie")
        pointofx=pointofx
        pointofy=pointofy
        print("point of x is",pointofx)
        print("point of y is",pointofy)

  except Exception as e:
      print(f"{e},enter the correct code")
      m=input("do you want to play with computer or friend?\nfor computer press 1\nfor friend press 2\nyour choise is:")
