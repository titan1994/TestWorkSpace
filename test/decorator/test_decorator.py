
try:
    import matplotlib
except:
    from os import system
    system('pip install matplotlib')


def makebold(fn):
    """
    Args:
        fn:
    """
    def my_super_name():
        return "<b>" + fn() + "</b>"

    return my_super_name


def makeitalic(fn):
    """
    Args:
        fn:
    """
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())  ## РІС‹РІРµРґРµС‚ <b><i>hello habr</i></b>


def shout(word="РґР°"):
    """
    Args:
        word:
    """
    return word.capitalize() + "!"


print (shout())
# РІС‹РІРµРґРµС‚: 'Р”Р°!'

# РўР°Рє РєР°Рє С„СѓРЅРєС†РёСЏ - СЌС‚Рѕ РѕР±СЉРµРєС‚, РІС‹ СЃРІСЏР·Р°С‚СЊ РµС‘ СЃ РїРµСЂРµРјРµРЅРЅРЅРѕР№,
# РєР°Рє Рё Р»СЋР±РѕР№ РґСЂСѓРіРѕР№ РѕР±СЉРµРєС‚
scream = shout

# Р—Р°РјРµС‚СЊС‚Рµ, С‡С‚Рѕ РјС‹ РЅРµ РёСЃРїРѕР»СЊР·СѓРµРј СЃРєРѕР±РѕРє: РјС‹ РќР• РІС‹Р·С‹РІР°РµРј С„СѓРЅРєС†РёСЋ "shout",
# РјС‹ СЃРІСЏР·С‹РІР°РµРј РµС‘ СЃ РїРµСЂРµРјРµРЅРЅРѕР№ "scream". Р­С‚Рѕ РѕР·РЅР°С‡Р°РµС‚, С‡С‚Рѕ С‚РµРїРµСЂСЊ РјС‹
# РјРѕР¶РµРј РІС‹Р·С‹РІР°С‚СЊ "shout" С‡РµСЂРµР· "scream":

print (scream())
# РІС‹РІРµРґРµС‚: 'Р”Р°!'

# Р‘РѕР»РµРµ С‚РѕРіРѕ, СЌС‚Рѕ Р·РЅР°С‡РёС‚, С‡С‚Рѕ РјС‹ РјРѕР¶РµРј СѓРґР°Р»РёС‚СЊ "shout", Рё С„СѓРЅРєС†РёСЏ РІСЃС‘ РµС‰С‘
# Р±СѓРґРµС‚ РґРѕСЃС‚СѓРїРЅР° С‡РµСЂРµР· РїРµСЂРµРјРµРЅРЅСѓСЋ "scream"

del shout
try:
    print(shout())
except NameError as e:
    print(e)
    # РІС‹РІРµРґРµС‚: "name 'shout' is not defined"

print (scream())
# РІС‹РІРµРґРµС‚: 'Р”Р°!'


def talk():
    # Р’РЅСѓС‚СЂРё РѕРїСЂРµРґРµР»РµРЅРёСЏ С„СѓРЅРєС†РёРё "talk" РјС‹ РјРѕР¶РµРј РѕРїСЂРµРґРµР»РёС‚СЊ РґСЂСѓРіСѓСЋ...
    def whisper(word="РґР°"):
        return word.lower() + "...";

    # ... Рё СЃСЂР°Р·Сѓ Р¶Рµ РµС‘ РёСЃРїРѕР»СЊР·РѕРІР°С‚СЊ!
    print(whisper())
    return whisper


# РўРµРїРµСЂСЊ, РљРђР–Р”Р«Р™ Р РђР— РїСЂРё РІС‹Р·РѕРІРµ "talk", РІРЅСѓС‚СЂРё РЅРµС‘ РѕРїСЂРµРґРµР»СЏРµС‚СЃСЏ Р° Р·Р°С‚РµРј
# Рё РІС‹Р·С‹РІР°РµС‚СЃСЏ С„СѓРЅРєС†РёСЏ "whisper".
talk()
# РІС‹РІРµРґРµС‚: "РґР°..."

# РќРѕ РІРЅРµ С„СѓРЅРєС†РёРё "talk" РќР• СЃСѓС‰РµСЃС‚РІСѓРµС‚ РЅРёРєР°РєРѕР№ С„СѓРЅРєС†РёРё "whisper":
try:
    print
    whisper()
except NameError as e:
    print(e)
    # РІС‹РІРµРґРµС‚ : "name 'whisper' is not defined"


def doSomethingBefore(func):
    """
    Args:
        func:
    """
    print ("РЇ РґРµР»Р°СЋ С‡С‚Рѕ-С‚Рѕ РµС‰С‘, РїРµСЂРµРґ С‚РµРј РєР°Рє РІС‹Р·РІР°С‚СЊ С„СѓРЅРєС†РёСЋ, РєРѕС‚РѕСЂСѓСЋ С‚С‹ РјРЅРµ РїРµСЂРµРґР°Р»")
    print (func())

doSomethingBefore(scream)


