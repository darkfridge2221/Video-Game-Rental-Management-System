"""
F320951 8/12/2023
Holds a function which carries out the necessary jobs
"""
import subscriptionManager as SM
import database
import csv
from datetime import datetime

GAME_INFO = "Game_Info.txt"
RENTAL = "Rental.txt"

def rent_game(customer_id, game_id):
    """
    Carries out many validation checks and edits database if it passes these checks
    Uses the given parameters to check for their presence in the databases
    """
    if len(customer_id) == 4 or customer_id.islower(): #checks if customer id is in correct format
        if SM.check_subscription(customer_id, SM.load_subscriptions("Subscription_Info.txt")): #checks if subscription is in date
            subscription_dictionary = SM.load_subscriptions("Subscription_Info.txt") #load subscription list of dictionaries

            rental_dictionary = [] #load rental list of dictionaries
            with open(RENTAL, 'r') as csvfile:
                reader = list(csv.DictReader(csvfile))
                for rental in reader:
                    rental_dictionary.append(rental)

            try:
                if len(database.read_rental_info(customer_id)) >= SM.get_rental_limit(subscription_dictionary[customer_id]['SubscriptionType']): #check if rental limit is hit
                    return( f"ERROR: Cannot rent more than your limit of {SM.get_rental_limit(subscription_dictionary[customer_id]['SubscriptionType'])} games") 
                else:
                    game_exists = False
                    with open(GAME_INFO, 'r') as csvfile:
                        reader = list(csv.DictReader(csvfile))
                        for entry in reader:
                            if entry['id'] == game_id: #checks if game id exists in game info database
                                game_exists = True
                                break

                    if not game_exists: #if game is not in database
                        return( f"ERROR: Game with ID {game_id} does not exist") 

                    else:
                        rental_dictionary.append({'id': game_id, 'rentaldate': datetime.now().strftime('%d/%m/%Y'), 'returndate': '', 'customerid': customer_id}) #adds entry

                    with open(RENTAL, 'r') as csvfile:
                        reader = list(csv.DictReader(csvfile))
                        for entry in reader:
                            if entry['id'] == game_id and entry['returndate'] == "": #checks if an entry exists that has no return date
                                return("ERROR: This game is already rented out") 
                    
                    with open(RENTAL, 'w', newline='') as file: #update the rental file with the new entries
                        fieldnames = ['id', 'rentaldate', 'returndate', 'customerid']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rental_dictionary)
                    return(f"You successfully rented {game_id} on {datetime.now().strftime('%d/%m/%Y')}") 

            except Exception as e:
                return(f"ERROR: {e}.") #Handle any error at all
        else:
            return("ERROR: Subscription expired or Customer ID not present in database. Cannot rent a game.")
    
        
