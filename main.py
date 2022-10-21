while True:
    try:
      pin = int(input("Введите пинкод \n"))
      if (pin > 999) and (pin < 1000000):
          break
      else:
          print("PIN-код должен состоять из не менее чем 4 и не более чем 6 цифр \n")
    except:
        print("Данные введены не коректно")
print("PIN-код сохранён")