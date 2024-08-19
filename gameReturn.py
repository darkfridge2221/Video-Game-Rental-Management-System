"""
9/12/2023 F320951
Has a function called return game which checks mainly the return date and acts off this information
"""
import feedbackManager as FM
import database
import csv
from datetime import datetime

GAME_INFO = "Game_Info.txt"
RENTAL = "Rental.txt"

def return_game(game_id, rating, comments = ""):
    """
    Uses the information passed by the user, and writes to the feedback file
    And updates a record in the rental file
    Returns the message to be printed to the menu
    """
    try:
        rental_dictionary = []
        with open(RENTAL, 'r') as csvfile: #load list of dictionaries of rental data
            reader = list(csv.DictReader(csvfile))
            for rental in reader:
                rental_dictionary.append(rental)

        game_exists = False
        with open(GAME_INFO, 'r') as csvfile:
            reader = list(csv.DictReader(csvfile))
            for entry in reader:
                if entry['id'] == game_id: #checks if game exists in the game info database
                    game_exists = True
                    break
                
        if not game_exists:
            return("ERROR: The game does not exist or invalid ID")
        
        for entry in rental_dictionary:
            if entry['id'] == game_id:
                if entry['returndate'] == "" and entry['rentaldate'] != "": #checks if the game id matches and has not been returned
                    entry['returndate'] = datetime.now().strftime('%d/%m/%Y')
                    FM.add_feedback(game_id, rating, comments, "Game_Feedback.txt") #updates the feedback database
                    with open(RENTAL, 'w', newline='') as file: #write the new data into the database
                        fieldnames = ['id', 'rentaldate', 'returndate', 'customerid']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader() 
                        writer.writerows(rental_dictionary) 
                    return("You successfully returned the game") 
                
        return("ERROR: Game hasn't been rented out") #if game hasn't been rented out then return this message
    except Exception as e:
        return(f"ERROR: {e}") #if any other unwanted errors occur
