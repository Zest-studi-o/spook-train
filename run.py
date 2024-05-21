# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



no_seats_on_train_available = 5
no_seats_on_train_sold = 0

while no_seats_on_train_sold < no_seats_on_train_available:
    print("\n******Welcome to Buntys SpookTrain******")
    print("Train Capacity:",no_seats_on_train_available)
    print("Remaining Tickets:",(no_seats_on_train_available-no_seats_on_train_sold))
    print("Process the next patron request.\n")
    patron_age = int(input("Enter age: "))

    if patron_age <= 12:
        print("Sorry, but minors (12 years of age or under) cannot ride SpookTrain.")
    elif patron_age > 12 and patron_age <= 17:
        patron_ID = input("Has the patron presented a valid school ID card? Enter Y or N: ")
        if patron_ID not in ("Y", "y"):
            print("As a valid school ID card has not been presented, a ticket cannot be sold.")
        else:
           patron_no_of_previous_rides = int(input("Enter the number of previous rides on SpookTrain: "))
   
           if patron_no_of_previous_rides >= 3:
               print("Sorry, but you cannot ride SpookTrain more than 3 times.")
           elif patron_no_of_previous_rides == 2:
               print("OK, you can ride SpookTrain, but as this is your third ride, you could be sick!")
               no_seats_on_train_sold += 1
           else:
               print("We have stamped your ticket and you can take your seat on the SpookTrain! It leaves soon!")
               no_seats_on_train_sold += 1
    else:
        print("Take your seat on the SpookTrain! It leaves soon!")
        no_seats_on_train_sold += 1

print("\nSpookTrain is now full and will depart in approximately 10 minutes. Fasten your seatbelts!")
