"""
F320951 7/12/2023
This program contains one function to handle searching the database
It searches the platforms, genres, and titles for similarity
"""
import database

def game_search(search_term):
    """
    This passes the term given by the user and searches each row's genre, title, and platform
    If there is similarity, it will return this record
    For example, the title is "Minecraft" and the user inputs "mi", it should return this record
    Similarly, "Play" for "Playstation", or for the Genre
    """
    try:
        updated_list = []
        data = database.read_game_info(search_term) #passes the search term to the database module to search
        for i, item1 in enumerate(data[0]): 
            item1['Availability'] = data[1][i] #makes dictionary
            updated_list.append(item1) #makes a new list, adding the availability as another dictionary
        return(updated_list)
    except Exception as e: #handles any errors 
        print(f"ERROR: {e}")
