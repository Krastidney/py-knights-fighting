# Knight MORDRED
from app.knights.knight import Knight


class Mordred(Knight):
    def __init__(
        self,
        name: str,
        power: str,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict = None
    ) -> None:
        super().__init__(
            name, power, hp, armour, weapon, potion
        )
