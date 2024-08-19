"""
7/12/2023 F320951
Holds functions to interact with the txt files
"""
import subscriptionManager as SM
import feedbackManager as FM
import csv

GAME_INFO = "Game_Info.txt"
RENTAL = "Rental.txt"

def read_game_info(term):
    """
    Takes the search term and uses it to search both Game_Info and Rental.
    It then returns two lists to be handled.
    """
    try:
        with open(GAME_INFO, newline = "") as csvfile: 
            reader = csv.DictReader(csvfile)
            matching_entries = []
            availability = []
            
            for game in reader: #goes through entries and checks for matches
                if term.lower() in game["title"].lower() or term.lower() in game["genre"].lower() or term.lower() in game["platform"].lower():
                    matching_entries.append(game)
                    availability.append(check_availability(game["id"]))
            return(matching_entries, availability)
    except Exception as e: #to handle errors but mostly FileNotFoundError
        return(f"ERROR: {e}")

def check_availability(term):
    """
    Opens the rental file and checks for rows where no return date is present
    Takes in the game ID, which is used as a search term in the database
    """
    with open(RENTAL, newline = "") as csvfile: #opens rental database to check for return dates
        reader = csv.DictReader(csvfile)

        for rental in reader: #goes through entries and checks for matches
             if rental['id'] == term and rental['returndate'] == "": #if the current record in 
                return("Not Available")
             if rental['id'] == term and rental['returndate'] != "":
                return("Available")
             else:
                return("Available")


def read_rental_info(term):
    """
    Similar to read_game_info but purely to handle the rental file instead
    """
    try:
        with open(RENTAL, newline = "") as csvfile: 
            reader = csv.DictReader(csvfile)
            matching_entries = []

            for rental in reader: #goes through entries and checks for matches
                if term.lower() in rental["customerid"].lower() or term.lower() in rental["id"].lower():
                    matching_entries.append(rental)
            return(matching_entries)
    except Exception as e: #to handle errors but mostly FileNotFoundError
        return(f"ERROR: {e}")
            
