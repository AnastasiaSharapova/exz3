word = input('Введите слово :')
def c_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        print(word, '- Является полиндромом')
    else:
        print(word, '-Не вляется полиндромом')

print(c_palindrome(word))


