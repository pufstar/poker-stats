from enum import Enum
import random
import itertools
from tqdm import tqdm


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

    def __str__(self) -> str:
        return self.value[1]

    def __repr__(self) -> str:
        return self.value[1]

    def __hash__(self) -> int:
        return self.value[0]

    def __eq__(self, other) -> bool:
        return self.value[0] == other.value[0]

    def __lt__(self, other) -> bool:
        return self.value[0] < other.value[0]

    def __gt__(self, other) -> bool:
        return self.value[0] > other.value[0]


class Card:
    def __init__(self, value: CardValues, symbol: CardSymbols = None):
        self._value = value
        self._symbol = symbol

    @property
    def value(self) -> int:
        return int(self._value.value[0])

    @property
    def value_verbose(self) -> str:
        return self._value.value[1]

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
        return f"{self.value_verbose}{self._symbol.value[1]}"

    def __repr__(self) -> str:
        return f"{self.value_verbose}{self._symbol.value[1]}"


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

        for _ in range(no_players):
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

    def _is_straight(self, cards: list[tuple]) -> bool:
        if cards[0] == Card(CardValues.ACE) and cards[1] == Card(CardValues.FIVE):
            for index in range(1, 4):
                if cards[index] - cards[index + 1] > 1:
                    return False

            return True

        for index in range(4):
            if cards[index] - cards[index + 1] > 1:
                return False

        return True

    def _is_same_symbol_combination(self, cards: list[tuple]) -> bool:
        for card in cards:
            if card.symbol != cards[0].symbol:
                return False

        return True

    def _get_duplicate_cards(self, cards: list[tuple]) -> dict:
        duplicates = {}

        for card in cards:
            if card.value not in duplicates:
                duplicates[card.value] = 0

            duplicates[card.value] += 1

        return duplicates

    def check_hand(self, hand: list[tuple]) -> PokerHands:
        cards = hand + self._table_cards
        cards.sort(reverse=True)

        best_combinations = []

        for combination in itertools.combinations(cards, 5):
            # TODO: move this into a method
            # we shouldn't check all the possible hands for each
            # combination(stop at the best one we've found for
            # a combination and the just compare the best from each)

            if self._is_straight(combination):
                best_combinations.append(PokerHands.STRAIGHT)

                if self._is_same_symbol_combination(combination):
                    if combination[-1] == Card(CardValues.TEN):
                        return PokerHands.ROYAL_FLUSH

                    best_combinations.append(PokerHands.STRAIGHT_FLUSH)

            if (
                list(combination).count(combination[0]) == 4
                or list(combination).count(combination[1]) == 4
            ):
                best_combinations.append(PokerHands.FOUR_OF_A_KIND)

            if self._is_same_symbol_combination(combination):
                best_combinations.append(PokerHands.FLUSH)

            duplicates = self._get_duplicate_cards(combination)

            if 2 in duplicates.values() and 3 in duplicates.values():
                best_combinations.append(PokerHands.FULL_HOUSE)
            elif 3 in duplicates.values():
                best_combinations.append(PokerHands.THREE_OF_A_KIND)
            elif list(duplicates.values()).count(2) == 2:
                best_combinations.append(PokerHands.TWO_PAIR)
            elif 2 in duplicates.values():
                best_combinations.append(PokerHands.PAIR)
            else:
                best_combinations.append(PokerHands.HIGH_CARD)

        return min(best_combinations)

    @property
    def deck(self) -> Deck:
        return self._deck

    @property
    def players(self) -> list[tuple]:
        return self._players

    @property
    def table_cards(self) -> list[tuple]:
        return self._table_cards


class Engine:
    def simulate_hand(self, no_players: int) -> dict:
        dealer = Dealer()

        dealer.shuffle_deck()

        players = dealer.deal_cards(no_players)

        dealer.deal_table_cards()

        return [dealer.check_hand(player) for player in players]

    def run_simulation(
        self, iterations: int, no_players: int, winners_only: bool = False
    ) -> dict:
        results = {poker_hand: 0 for poker_hand in PokerHands}
        for index in tqdm(range(iterations)):
            # iteration = index + 1

            result = self.simulate_hand(no_players)

            if winners_only:
                results[min(result)] += 1
            else:
                for poker_hand in result:
                    results[poker_hand] += 1

        return results
