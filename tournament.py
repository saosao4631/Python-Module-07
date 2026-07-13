from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)
from ex2.strategy import BattleStrategy


def fight(
    first: Tuple[CreatureFactory, BattleStrategy],
    second: Tuple[CreatureFactory, BattleStrategy],
) -> None:
    first_factory, first_strategy = first
    second_factory, second_strategy = second
    left = first_factory.create_base()
    right = second_factory.create_base()

    print()
    print("* Battle *")
    print(left.describe())
    print(" vs.")
    print(right.describe())
    print(" now fight!")
    first_strategy.act(left)
    second_strategy.act(right)


def battle(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                fight(opponents[i], opponents[j])
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
