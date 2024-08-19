# Video-Game-Rental-Management-System

Test cases: 

Search Game:
call (Searches for part of game Call Of Duty, searching by title)
god of war (Searches for the entire title, searching by title)
spo (searches for part of the genre Sports, searching by genre)
shooter (searches fully for the entire genre, searching by genre)
play (searches for part of the platform, searching by genre)
xbox (searches fully for the platform, searching by platform)

Rent Game:
coai cod01 (Optimal test case. Creates an entry in Rental.txt, which is their second game)
ABCD lol12 (Customer ID is in wrong format and therefore doesn't exist)
ijkl lol11 (Subscription is expired)
abcd hah02 (Game doesn't exist, you can input anything as game ID, in fact)
abcd minecraft23 (minecraft23 is already rented out)
mnop cyber14 (Cannot rent more than their limit of 2 games)

Return Game:
acr03, 5, very good game (Optimal test case. The game is rented out and can be returned)
cod01, 4, nice (Testing for returning when game hasn't been rented out yet)
minecraft25, 1, boring (Testing a game ID that doesn't exist)

Inventory Pruning:
I decided my criterion for a bad game to be their average rating. I then tell them to prune the two lowest ranked games on average.
