from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(HealCapability, base).heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(HealCapability, evolved).heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    base_cap = cast(TransformCapability, base)
    print(base_cap.transform())
    print(base.attack())
    print(base_cap.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    evolved_cap = cast(TransformCapability, evolved)
    print(evolved_cap.transform())
    print(evolved.attack())
    print(evolved_cap.revert())


def main() -> None:
    try:
        test_healing(HealingCreatureFactory())
        print()
        test_transform(TransformCreatureFactory())
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
