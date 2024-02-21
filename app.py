from models import Dealer, Engine


def main() -> None:
    engine = Engine()

    results = engine.run_simulation(10, 4)

    print(results)


if __name__ == "__main__":
    main()
