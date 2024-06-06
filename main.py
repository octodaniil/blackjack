import random

# Определение констант
SUITS = ['♥️', '♦️', '♣️', '♠️']
RANKS = ['Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К']
VALUES = {'Т': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'В': 10, 'Д': 10, 'К': 10}

# Определение классов
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Т':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Функции игры
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def get_hand_value(hand):
    hand.adjust_for_ace()
    return hand.value

def bust(hand):
    return get_hand_value(hand) > 21

def determine_winner(player_hand, dealer_hand):
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)

    if bust(dealer_hand):
        return "Игрок"
    elif player_value > dealer_value:
        return "Игрок"
    elif player_value < dealer_value:
        return "Дилер"
    else:
        return "Ничья"

def play():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Раздача начальных карт
    for _ in range(2):
        hit(deck, player_hand)
        hit(deck, dealer_hand)

    # Вывод состояния игры
    print("Ваши карты:", ", ".join(map(str, player_hand.cards)))
    print("Карта дилера:", str(dealer_hand.cards[0]))

    # Ход игрока
    while True:
        choice = input("Хотите взять карту или остановиться? (в/о) ").lower()
        if choice == 'в':
            hit(deck, player_hand)
            print("Ваши карты:", ", ".join(map(str, player_hand.cards)))
            if bust(player_hand):
                print("Вы перебрали! Дилер выиграл.")
                return
        elif choice == 'о':
            break

    # Ход дилера
    while get_hand_value(dealer_hand) < 17:
        hit(deck, dealer_hand)

    # Вывод итогового результата
    print("Ваша итоговая рука:", ", ".join(map(str, player_hand.cards)), f"(значение: {get_hand_value(player_hand)})")
    print("Итоговая рука дилера:", ", ".join(map(str, dealer_hand.cards)), f"(значение: {get_hand_value(dealer_hand)})")

    winner = determine_winner(player_hand, dealer_hand)
    if winner == "Игрок":
        print("Вы выиграли!")
    elif winner == "Дилер":
        print("Дилер выиграл.")
    else:
        print("Ничья!")

# Начало игры
play()

