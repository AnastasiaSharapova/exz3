def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

card = (input('Введите номер карты : '))
print(card_hide(card))