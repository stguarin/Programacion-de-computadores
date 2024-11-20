frase = input('digite la frase a combprobar (los espacios seran reconocidos como caracteres especiales) ')

if frase.isalpha() == True:
    print('es una frase solo con caracteres unicamente alfabeticos')
else:
    print('la frase tiene mas que caracteres alfabeticos')