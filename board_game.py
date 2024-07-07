import random
import json
from collections import Counter

NUM_PLAYERS = 3
NUM_DECKS = 4
CARDS_PER_PLAYER = 5

def load_card_data(filename='Board_Game/cards.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: {filename} is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: Missing key in JSON file - {e}")
    return None

def create_deck(num_decks, card_data):
    single_deck = [{'suit': suit, 'value': card['value'], 'points': card['points']} for suit in card_data['suits'] for card in card_data['cards']]
    return single_deck * num_decks

def shuffle_deck(deck):
    random.shuffle(deck)

def get_player_name(player_number):
    while True:
        player_name = input(f"Enter name for Player {player_number}: ").strip()
        if player_name and len(player_name) <= 15 and player_name.isalpha():
            return player_name
        else:
            print("Invalid name. Please enter a valid name (only letters and spaces, max 15 characters).")


def deal_cards_to_player(deck, cards_per_player):
    return [deck.pop() for _ in range(cards_per_player)]

def deal_cards(deck, num_players, cards_per_player):
    players = {}
    for i in range(num_players):
        player_name = get_player_name(i + 1)
        player_cards = deal_cards_to_player(deck, cards_per_player)
        players[player_name] = player_cards
    return players

def display_cards(cards):
    return ', '.join([f"{card['value']}{card['suit']}" for card in cards])

def calculate_score(cards):
    return sum(card['points'] for card in cards)

def calculate_score_by_suit(cards):
    suit_counts = Counter(card['suit'] for card in cards)
    most_common_suit_count = suit_counts.most_common(1)[0][1]
    return most_common_suit_count

def calculate_score_by_value(cards):
    value_counts = Counter(card['value'] for card in cards)
    most_common_value_count = value_counts.most_common(1)[0][1]
    return most_common_value_count

def remove_loser(players):
    scoreboard_by_score = []
    scoreboard_by_suit = []
    scoreboard_by_value = []
    for player, cards in players.items():
        scoreboard_by_score.append((player, calculate_score(cards)))
        scoreboard_by_suit.append((player, calculate_score_by_suit(cards)))
        scoreboard_by_value.append((player, calculate_score_by_value(cards)))
    scoreboard_by_score = sorted(scoreboard_by_score, key=lambda x: x[1])
    scoreboard_by_suit = sorted(scoreboard_by_suit, key=lambda x: x[1])
    scoreboard_by_value = sorted(scoreboard_by_value, key=lambda x: x[1])
    if scoreboard_by_score[0][1] != scoreboard_by_score[1][1]:
        return scoreboard_by_score[0][0]
    elif scoreboard_by_suit[0][1] != scoreboard_by_suit[0][1]:
        return scoreboard_by_suit[0][0]
    elif scoreboard_by_value[0][1] != scoreboard_by_value[0][1]:
        return scoreboard_by_value[0][0]

def deal_new_round(deck, players):
    shuffle_deck(deck)
    remaining_cards = len(deck)
    for player in players:
        if remaining_cards >= CARDS_PER_PLAYER:
            players[player] = deal_cards_to_player(deck, CARDS_PER_PLAYER)
            remaining_cards -= CARDS_PER_PLAYER
        else:
            print("Not enough cards remaining in the deck.")
            break
    return deck, players

def change_card(deck, players):
    for player, cards in players.items():
        while True:
            decision = input(f'{player} do you want to change card? (y/n): ')
            if decision.lower() == "n":
                break
            elif decision.lower() == "y":
                while True:
                    try:
                        card_index = int(input("Which one (index 0-4): "))
                        if card_index < 0 or card_index >= CARDS_PER_PLAYER:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 4.")
                new_card = deck.pop()
                players[player][card_index] = new_card
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
            
def find_winner(player_hands):
    players = list(player_hands)
    scores = {player: calculate_score(player_hands[player]) for player in players}
    max_score = max(scores.values())
    candidates = [player for player, score in scores.items() if score == max_score] 
    
    if len(candidates) == 1:
        return candidates[0]
    
    suit_counts = {player: calculate_score_by_suit(player_hands[player]) for player in candidates}
    max_suit_count = max(suit_counts.values())
    candidates = [player for player, count in suit_counts.items() if count == max_suit_count]
    
    if len(candidates) == 1:
        return candidates[0]
    
    value_counts = {player: calculate_score_by_value(player_hands[player]) for player in candidates}
    max_value_count = max(value_counts.values())
    candidates = [player for player, count in value_counts.items() if count == max_value_count]
    
    if len(candidates) == 1:
        return candidates[0]
    
def main():
    card_data = load_card_data("Board_Game/cards.json")
    if not card_data:
        print("Error loading card data. Exiting program.")
        return

    deck = create_deck(NUM_DECKS, card_data)
    shuffle_deck(deck)
    players = deal_cards(deck, NUM_PLAYERS, CARDS_PER_PLAYER)

    while len(players) > 1:
        print("\nInitial Cards:")
        for player, cards in players.items():
            print(f"{player}: {display_cards(cards)}")

        change_card(deck, players)
        print("\nAfter Cards Change:")
        for player, cards in players.items():
            print(f"{player}: {display_cards(cards)}")

        player_who_lost = remove_loser(players)
        if player_who_lost:
            print(f"{player_who_lost} loses this round.")
            players.pop(player_who_lost)

        if len(players) > 1:
            deck, players = deal_new_round(deck, players)

    winner = find_winner(players)
    if winner:
        print(f"\nCongrats {winner}!, you won!")
    else:
        print(f"\nIt is a draw!")
            

if __name__ == "__main__":
    main()
    
