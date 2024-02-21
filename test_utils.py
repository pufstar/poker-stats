from models import Card, CardValues, CardSymbols, Dealer, PokerHands


def test_royal_flush():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.TEN, CardSymbols.HEARTS),
        Card(CardValues.KING, CardSymbols.HEARTS),
        Card(CardValues.ACE, CardSymbols.HEARTS),
        Card(CardValues.JACK, CardSymbols.HEARTS),
        Card(CardValues.NINE, CardSymbols.CLUBS),
    ]

    hand = [
        Card(CardValues.QUEEN, CardValues.HEARTS),
        Card(CardValues.NINE, CardSymbols.HEARTS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.ROYAL_FLUSH


def test_straight_flush():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.TWO, CardSymbols.CLUBS),
        Card(CardValues.TEN, CardSymbols.DIAMONDS),
        Card(CardValues.KING, CardSymbols.DIAMONDS),
        Card(CardValues.QUEEN, CardSymbols.DIAMONDS),
        Card(CardValues.ACE, CardSymbols.SPADES),
    ]

    hand = [
        Card(CardValues.JACK, CardSymbols.DIAMONDS),
        Card(CardValues.NINE, CardSymbols.DIAMONDS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.STRAIGHT_FLUSH


def test_four_of_a_kind():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.SEVEN, CardSymbols.CLUBS),
        Card(CardValues.THREE, CardSymbols.CLUBS),
        Card(CardValues.TEN, CardSymbols.SPADES),
        Card(CardValues.TEN, CardSymbols.CLUBS),
        Card(CardValues.SEVEN, CardSymbols.HEARTS),
    ]

    hand = [
        Card(CardValues.SEVEN, CardSymbols.DIAMONDS),
        Card(CardValues.SEVEN, CardSymbols.SPADES),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.FOUR_OF_A_KIND


def test_full_house():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.TWO, CardSymbols.SPADES),
        Card(CardValues.ACE, CardSymbols.DIAMONDS),
        Card(CardValues.SEVEN, CardSymbols.CLUBS),
        Card(CardValues.FIVE, CardSymbols.SPADES),
        Card(CardValues.SEVEN, CardSymbols.SPADES),
    ]

    hand = [
        Card(CardValues.SEVEN, CardSymbols.HEARTS),
        Card(CardValues.TWO, CardSymbols.DIAMONDS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.FULL_HOUSE


def test_flush():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.THREE, CardSymbols.SPADES),
        Card(CardValues.SIX, CardSymbols.SPADES),
        Card(CardValues.QUEEN, CardSymbols.DIAMONDS),
        Card(CardValues.QUEEN, CardSymbols.CLUBS),
        Card(CardValues.FOUR, CardSymbols.SPADES),
    ]

    hand = [
        Card(CardValues.QUEEN, CardSymbols.SPADES),
        Card(CardValues.TEN, CardSymbols.SPADES),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.FLUSH


def test_straight():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.FIVE, CardSymbols.SPADES),
        Card(CardValues.SEVEN, CardSymbols.DIAMONDS),
        Card(CardValues.EIGHT, CardSymbols.HEARTS),
        Card(CardValues.TWO, CardSymbols.DIAMONDS),
        Card(CardValues.NINE, CardSymbols.SPADES),
    ]

    hand = [
        Card(CardValues.SIX, CardSymbols.SPADES),
        Card(CardValues.SIX, CardSymbols.CLUBS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.STRAIGHT


def test_three_of_a_kind():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.ACE, CardSymbols.CLUBS),
        Card(CardValues.EIGHT, CardSymbols.SPADES),
        Card(CardValues.FIVE, CardSymbols.DIAMONDS),
        Card(CardValues.KING, CardSymbols.SPADES),
        Card(CardValues.EIGHT, CardSymbols.HEARTS),
    ]

    hand = [
        Card(CardValues.EIGHT, CardSymbols.DIAMONDS),
        Card(CardValues.SIX, CardSymbols.HEARTS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.THREE_OF_A_KIND


def test_two_pair():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.FIVE, CardSymbols.SPADES),
        Card(CardValues.NINE, CardSymbols.DIAMONDS),
        Card(CardValues.NINE, CardSymbols.SPADES),
        Card(CardValues.TEN, CardSymbols.SPADES),
        Card(CardValues.FIVE, CardSymbols.CLUBS),
    ]

    hand = [
        Card(CardValues.ACE, CardSymbols.SPADES),
        Card(CardValues.ACE, CardSymbols.DIAMONDS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.TWO_PAIR


def test_pair():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.SIX, CardSymbols.CLUBS),
        Card(CardValues.NINE, CardSymbols.CLUBS),
        Card(CardValues.TWO, CardSymbols.DIAMONDS),
        Card(CardValues.KING, CardSymbols.SPADES),
        Card(CardValues.QUEEN, CardSymbols.HEARTS),
    ]

    hand = [
        Card(CardValues.SIX, CardSymbols.DIAMONDS),
        Card(CardValues.ACE, CardSymbols.HEARTS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.PAIR


def test_high_card():
    dealer = Dealer()

    table_cards = [
        Card(CardValues.SIX, CardSymbols.CLUBS),
        Card(CardValues.NINE, CardSymbols.CLUBS),
        Card(CardValues.TWO, CardSymbols.DIAMONDS),
        Card(CardValues.KING, CardSymbols.SPADES),
        Card(CardValues.QUEEN, CardSymbols.HEARTS),
    ]

    hand = [
        Card(CardValues.SEVEN, CardSymbols.DIAMONDS),
        Card(CardValues.ACE, CardSymbols.HEARTS),
    ]

    dealer._table_cards = table_cards

    assert dealer.check_hand(hand) == PokerHands.HIGH_CARD
