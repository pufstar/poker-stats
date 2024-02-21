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


class PokerHands(Enum):
    ROYAL_FLUSH = 1, "Royal flush"
    STRAIGHT_FLUSH = 2, "Straight flush"
    FOUR_OF_A_KIND = 3, "Four of a kind"
    FULL_HOUSE = 4, "Full house"
    FLUSH = (
        5,
        "Flush",
    )
    STRAIGHT = (
        6,
        "Straight",
    )
    THREE_OF_A_KIND = 7, "Three of a kind"
    TWO_PAIR = 8, "Two pair"
    PAIR = 9, "Pair"
    HIGH_CARD = 10, "High card"


class Card:
    def __init__(self, value: CardValues = None, symbol: CardSymbols = None):
        self._value = value
        self._symbol = symbol

    @property
    def value(self) -> int:
        return int(self._value.value[1])

    @property
    def symbol(self) -> CardSymbols:
        return self._symbol

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __add__(self, other) -> int:
        return self.value + other.value

    def __sub__(self, other) -> int:
        return self.value - other.value

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
    def __init__(self):
        self._deck = None
        self._table_cards = []

    def deal_cards(self, no_players: int) -> list[tuple]:
        players = []

        for _ in range(self._no_players):
            players.append([self.deck.draw()])

        for player in players:
            player.append(self.deck.draw())

        return players

    def deal_table_cards(self) -> None:
        self.deck.draw()

        for _ in range(3):
            self._table_cards.append(self.deck.draw())

        self.deck.draw()

        self._table_cards.append(self.deck.draw())

        self.deck.draw()

        self._table_cards.append(self.deck.draw())

    def shuffle_deck(self) -> None:
        self._deck = Deck()

    def check_hand(self, hand: list[tuple]) -> PokerHands:
        pass

    @property
    def table(self) -> dict:
        return {"players": self.players, "table": self._table_cards}

    @property
    def deck(self) -> Deck:
        return self._deck

    @property
    def players(self) -> list[tuple]:
        return self._players


class Engine:
    def simulate_hand(self, no_players: int) -> dict:
        dealer = Dealer()

        dealer.shuffle_deck()

        players = dealer.deal_cards(no_players)

        dealer.deal_table_cards()

        result = {player: dealer.check_hand(player) for player in players}

        result.update({"table": dealer.table})

        return result

    def run_simulation(self, iterations: int, no_players: int) -> None:
        results = []
        for index in range(iterations):
            sim_no = index + 1

            results.append(self.simulate_hand(no_players))

        return results
