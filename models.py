from enum import Enum
import random


class CardValues(Enum):
    TWO = 2, "2"
    THREE = 3, "3"
    FOUR = 4, "4"
    FIVE = 5, "5"
    SIX = 6, "6"
    SEVEN = 7, "7"
    EIGHT = 8, "8"
    NINE = 9, "9"
    TEN = 10, "10"
    JACK = 11, "J"
    QUEEN = 12, "Q"
    KING = 13, "K"
    ACE = 14, "A"


class CardSymbols(Enum):
    SPADES = 1, "♠️"
    HEARTS = 2, "♥️"
    CLUBS = 3, "♣️"
    DIAMONDS = 4, "♦️"


class Card:
    def __init__(self, value: CardValues = None, symbol: CardSymbols = None):
        self._value = value
        self._symbol = symbol

    @property
    def value(self) -> int:
        return self._value.value[1]

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __str__(self) -> str:
        return f"{self.value}{self._symbol.value[1]}"

    def __repr__(self) -> str:
        return f"{self.value}{self._symbol.value[1]}"


class Deck:
    def __init__(self):
        self._cards = []

        for value in CardValues:
            for symbol in CardSymbols:
                self._cards.append(Card(value, symbol))

        random.shuffle(self._cards)

    def draw(self) -> Card:
        return self._cards.pop()


class Dealer:
    def __init__(self, no_players: int):
        self._deck = Deck()
        self._players = []

        for _ in range(no_players):
            self._players.append([self.deck.draw()])

        for player in self._players:
            player.append(self.deck.draw())

        import pudb

        pu.db

    @property
    def deck(self) -> Deck:
        return self._deck

    @property
    def players(self) -> list[tuple]:
        return self._players
