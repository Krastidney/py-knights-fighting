from app.knights.knight_dict import KNIGHTS
from app.knights.arthur import Arthur
from app.knights.lancelot import Lancelot
from app.knights.red_knight import RedKnight
from app.knights.mordred import Mordred


def battle(knights: dict) -> None:
    arthur = Arthur(**knights["arthur"])
    lancelot = Lancelot(**knights["lancelot"])
    mordred = Mordred(**knights["mordred"])
    red_knight = RedKnight(**knights["red_knight"])

    # BATTLE:

    # 1 Lancelot vs Mordered:
    lancelot.hp -= mordred.powers() - lancelot.protections()
    mordred.hp -= lancelot.powers() - mordred.protections()

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.powers() - arthur.protections()
    red_knight.hp -= arthur.powers() - red_knight.protections()

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
