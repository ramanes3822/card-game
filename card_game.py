import random

cards_string = [f'{str(x)}' for x in range(2,10)]+["J", "Q", "K", "A"]
characters = ["@", "#", "^", "*"]
cards = [f"{x}{i}" for x in cards_string for i in characters]
print("before shuffle",cards)
print("")
random.shuffle(cards)
print("after shuffle",cards)
print("")

#four player
players = {1: [], 2: [], 3: [], 4: []}

#distribute cards
for i in range(len(cards)):
    players[i % 4+1].append(cards[i])
for player, cards in players.items():
    print(f"Player {player}: {', '.join(cards)}")

def evaluate_winner(players):
    card_ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                  'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    symbol_ranks = {'@': 1, '#': 2, '^': 3, '*': 4}

    player_scores = {}
    for player, cards in players.items():
        card_counts = {}
        for card in cards:
            value, symbol = card[:-1], card[-1]
            if value not in card_counts:
                card_counts[value] = []
            card_counts[value].append(symbol)

        max_count = max(len(symbols) for symbols in card_counts.values())
        top_cards = [value for value, symbols in card_counts.items() if len(symbols) == max_count]

        if len(top_cards) > 1:
            top_cards.sort(key=lambda x: card_ranks[x], reverse=True)

        top_value = top_cards[0]
        top_symbols = sorted(card_counts[top_value], key=lambda x: symbol_ranks[x], reverse=True)

        player_scores[player] = (max_count, card_ranks[top_value], symbol_ranks[top_symbols[0]])

    winner = max(player_scores, key=player_scores.get)
    return winner, player_scores[winner]

winner, score = evaluate_winner(players)

print(f"\nWinner: Player {winner} with {score[0]} cards of highest rank {list(players[winner])[0][:-1]}.")
