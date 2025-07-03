while True:
 print("\n1. Register \n 2. Login \n 3. Exit")
 choice = input("Select one from the above options: ")
 choice = int(choice)

 if choice == 1 :
  username = input("Enter your Username: ")
  password = input("Enter your password make sure it should have 4 digits in it: ")
  if len(password) != 4:
    print("\nYou entered a wrong password it must be of 4 digits or should contain numbers only")
  else:
   print("THANKYOU! Successfully Registered")

 elif choice == 2:
  username = input("Enter your Username: ")
  password = input("Enter your password: ")


  with open("user.txt","r")as file:
     login=file.readlines()
     login_info = username + " : " + password
  if login_info in login :
    print(" \nLOGIN SUCESSFULL")
  else:
    print("\nYou entered a wrong username or password !")
 elif choice == 3:
  print("\nThankyou, for choosing us have a great day")  
  break
 else:
  print("\nyou choose an invalid option")




