from random import randint


class Die:
    """РљР»Р°СЃСЃ, РїСЂРµРґСЃС‚Р°РІР»СЏСЋС‰РёР№ РѕРґРёРЅ РєСѓР±РёРє."""

    def __init__(self, num_sides=6):
        """РџРѕ СѓРјРѕР»С‡Р°РЅРёСЋ РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ
        С€РµСЃС‚РёРіСЂР°РЅРЅС‹Р№ РєСѓР±РёРє.

        Args:
            num_sides:
        """
        self.num_sides = num_sides

    def roll(self):
        """Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃР»СѓС‡Р°Р№РЅРѕРµ С‡РёСЃР»Рѕ РѕС‚ 1 РґРѕ
        С‡РёСЃР»Р° РіСЂР°РЅРµР№
        """
        return randint(1, self.num_sides)

