while True:
 print("1. Register \n 2. Login \n 3. Exit")
 choice = input("Select one from the above options: ")
 choice = int(choice)

 if choice == 1 :
  username = input("Enter your Username: ")
  password = input("Enter your password make sure it should have 4 digits in it: ")
  print(" THANKYOU; for entering your detail ")

  with open("user.txt","a")as file:
     file.write("\n"+ username +" : " + password)
 elif choice == 2:
  username = input("Enter your Username: ")
  password = input("Enter your password: ")


  with open("user.txt","r")as file:
     login=file.readlines()
     login_info = username + " : " + password
  if login_info in login :
    print(" LOGIN SUCESSFULL")
  else:
    print("You entered a wrong username or password !")
 elif choice == 3:
  print("Thankyou, for choosing us have a great day")  
  break
 else:
  print("you choose an invalid option")




