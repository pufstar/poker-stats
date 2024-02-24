from models import Dealer, Engine, PokerHands
import click


@click.command()
@click.option("--iterations", "-i", default=0, help="Number of iterations")
@click.option("--players", "-p", default=1, help="Number of players")
@click.option(
    "--winners-only",
    "-w",
    is_flag=True,
    show_default=True,
    default=False,
    help="Count only the winning hand of each iteration",
)
def main(iterations, players, winners_only) -> None:
    engine = Engine()

    results = engine.run_simulation(iterations, players, winners_only)

    print(f"Results for {iterations} iterations and {players} players:")
    for poker_hand in PokerHands:
        print(f"{poker_hand}: {results[poker_hand]}")


if __name__ == "__main__":
    main()
