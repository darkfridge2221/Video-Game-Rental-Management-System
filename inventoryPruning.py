"""
11/12/2023 F320951
Holds 3 functions which are used togther to return a graph
And also recommends which games to prune
"""
import database
import csv
#import feedbackManager as FM
import matplotlib.pyplot as plt

FEEDBACK = "Game_Feedback.txt" #define the file path

def inventory_pruning():
    """
    No parameters needed because doesn't need user input
    It gets the game ratings and calculates averages and returns a string with the "worst" games
    """
    data = load_feedback() #load feedback using own module because given one didn't work

    average_ratings = {} #dictionary to store cumulative rating
    count_ratings = {} #dictionary to store count for each game

    for entry in data: #calculate rating and counts for each game
        game_id = entry['id']
        rating = int(entry['rating'])

        if game_id in average_ratings: #update rating and counts for exisiting games
            average_ratings[game_id] += rating
            count_ratings[game_id] +=1
        else: #initialise rating and counts for new games
            average_ratings[game_id] = rating
            count_ratings[game_id] = 1

    for game_id in average_ratings: #calculate average for each game
        average_ratings[game_id] /= count_ratings[game_id]

    plot_ratings(average_ratings) #plot bar chart
    sorted_games = sorted(average_ratings.items(), key=lambda x: x[1]) #sorting games by average rating

    bad_games = "You should prune:\n" #generate string to list the two worst rated games
    for game_id, average in sorted_games[:2]:
        bad_games += (f"{game_id} with average rating {average}\n")
    return(bad_games) #return string containing worst games

def plot_ratings(average_ratings): 
    """
    Uses matplotlib to plot the averages for visualisation
    """
    plt.bar(average_ratings.keys(), average_ratings.values())
    plt.xlabel('Game ID')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings of Games')
    plt.xticks(rotation=45)
    plt.show()

def load_feedback():
    """
    Made this function because the FM function was giving error:
    "ValueError: not enough values to unpack (expected 3, got 0)"
    """
    data = []
    with open(FEEDBACK, 'r') as csvfile: #open feedback file in read mode
        reader = csv.DictReader(csvfile) #use DictReader to parse CSV file into a dictionary
        for row in reader:
            data.append(row)
    return(data) #return list of dictionaries
