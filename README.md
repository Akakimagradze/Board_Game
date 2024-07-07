# Brief Overview:
    The program is about a board game. The game is played from a deck of 4 cards.
    Three players participate in the game. Players are dealt 5 cards each and then
    change or keep their cards at various stages of the game. The ultimate goal of the game is to get the highest score.
    The winner is determined by the highest score.
    At the end of each round, the player with the lowest score is eliminated and
    this continues until there is only one winner left.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# About the game and rules of the game:
    1. program will get the names of three players.
    Then the program should randomly generate 5-5 cards for each player.
    Cards are drawn from a deck of 4 cards.

    2. Card suits and values will be:
        Suits:
            S - Spade
            H - Heart
            D - Diamond
            C - Club
        Values:
            A - Ace (20 Points)
            K - King (13 Points)
            Q - Queen (12 Points)
            J - Jack (11 Points)
            10 - Ten (10 Points)
            9 - Nine (9 Points)
            8 - Eight (8 Points)
            7 - Seven (7 Points)
            6 - Six (6 Points)
            5 - Five (5 Points)
            4 - Four (4 Points)
            3 - Three (3 Points)
            2 - Two (2 Points)

    3. If the points are equal, then the player with more cards of the same suit wins.
    For example, 4 clubs and 1 spade beats 3 hearts and 2 bricks because the number of cards of the same suit is 4 to 3.

    4. If the number of points is equal and the card suit does not reveal a winner, then
    the player with the most cards of the same value wins. 
    For example, 5 - 10s beats 2 - jacks. 2 - 10s beats 1 - 10. If the winner is not determined again, then it's a tie.

    5. After the cards are revealed, each player has the right to change or not change 1 card from his five cards.

    6. Program will kick out the player who has the least points in his hands.
    If it's a tie then no one leaves the game. After each round, the program deals new cards from the beginning.
    This continues until there is only one winner left.








