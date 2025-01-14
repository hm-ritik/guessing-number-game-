import random
choice=int(input("guess the random number between 1 to 100: "))
num=random.randint(1,100)
max_attemp=7
attemp=0


while attemp<=max_attemp: 
   if num==choice:
      print("Congratulation You are right")
      break
   elif choice>num:
      print("Too High")
      choice=int(input("guess the random number between 1 to 100: ")) 
      attemp+=1  
   elif choice<num:
    print("Too low")
    choice=int(input("guess the random number between 1 to 100: "))
    attemp+=1
   else:
    print("Invalid","Game stopped") 
    break
   

   if attemp<max_attemp:
     print(f"your chances {attemp}/{max_attemp}")
   else:
     print("sorry you lost the number is : ",num)  

