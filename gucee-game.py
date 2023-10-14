n = 18
number_of_gucess= 1
while number_of_gucess <= 9:
               gucess_number = int(input("Gucess the number: \n"))
               if gucess_number < 18:
                       print("You are enter less number please input greater number.\n")
               elif gucess_number > 18:
                           print("You are enter greater number please input smaller number.\n")  
               else:
                       print("you won!")
                       print(f"{number_of_gucess} no of gucess he took finish.")
                       break
               print(f"{number_of_gucess} no. of gucess left")
               number_of_gucess += 1

if number_of_gucess > 9:
        print("Game Over")


