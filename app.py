from models import Dealer, Engine, PokerHands

NO_ITERATIONS = 1000
NO_PLAYERS = 8


def main() -> None:
    engine = Engine()

    results = engine.run_simulation(NO_ITERATIONS, NO_PLAYERS)

    print(f"Results for {NO_ITERATIONS} iterations and {NO_PLAYERS} players:")
    for poker_hand in PokerHands:
        print(f"{poker_hand}: {results[poker_hand]}")


if __name__ == "__main__":
    main()
