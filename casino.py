import random
from colorama import Fore, Back, Style, init
import time

init()

money = 10000
print(Fore.MAGENTA + Style.BRIGHT + r"""
                            .__               
  ______ ____ _____    _____|__| ____   ____  
 /  ___// ___\\__  \  /  ___/  |/    \ /  _ \ 
 \___ \\  \___ / __ \_\___ \|  |   |  (  <_> )
/____  >\___  >____  /____  >__|___|  /\____/ 
     \/     \/     \/     \/        \/        
""" + Style.RESET_ALL)
print(Fore.MAGENTA + Style.BRIGHT + "> Author: raccoon888")
time.sleep(2)
print(Fore.WHITE + "> Добро пожаловать в Simple Casino!")
while True:
    bet_money = input(f"> Какую сумму вы хотите поставить? (у вас имеется {money} рублей): ")
    bet_money = int(bet_money)
    if bet_money > money:
        print(f"> Вы не можете поставить больше {money} рублей!")
        continue
    if bet_money < 0:
        print("> Вы не можете поставить отрицательное кол-во рублей")
        continue
    print(f"> Вы поставили {bet_money} рублей.")
    print("> Выберите режим: ")
    print("1 | Автомат с тремя числами")
    print("2 | Угадай число (от 1 до 5)")
    print("3 | Камень, ножницы, бумага")
    print("4 | Орёл или решка")
    user_choice = input(Fore.GREEN + Style.BRIGHT + "> Ваш выбор: ")

    if user_choice == '1':
        print(Fore.GREEN + Style.BRIGHT + "> Вы выбрали автомат с тремя числами!")
        print(Fore.GREEN + Style.BRIGHT + "> Числа рандомизируются...")
        time.sleep(4)
        print(Fore.MAGENTA + Style.BRIGHT + "> Вам выпало: ")
        random_num1 = random.randint(1, 7)
        print(f"~ [{random_num1}]")
        random_num2 = random.randint(1, 7)
        print(f"~ [{random_num2}]")
        random_num3 = random.randint(1, 7)
        print(f"~ [{random_num3}]")
        if random_num1 == random_num2 == random_num3 and random_num1 != 7:
            print(Fore.GREEN + Style.BRIGHT + "> Вам выпало 3 одинаковых числа! Ваша ставка умножается на х5")
            bet_money = bet_money * 5
            money = money + bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_num1 == random_num2 == random_num3 and random_num1 == 7:
            print(Fore.GREEN + Style.BRIGHT + "> ВАМ ВЫПАЛО ТРИ СЕМЁРКИ! ВАША СТАВКА УМНОЖАЕТСЯ НА х30")
            bet_money = bet_money * 30
            money = money + bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        else:
            money = money - bet_money
            print(Fore.RED + Style.BRIGHT + f"> Вы проиграли! Теперь у вас {money} рублей!" + Style.RESET_ALL)
    elif user_choice == '2':
        random_number = random.randint(1, 5)
        print(Fore.MAGENTA + Style.BRIGHT + "> Загадываем число..")
        time.sleep(2)
        user_num = input("> Число загадано, попробуй отгадать! (от 1 до 5): ")
        if user_num == random_number:
            print(Fore.GREEN + Style.BRIGHT + "> Поздравляем! Вы угадали число! Ваша ставка умножается на х3")
            bet_money = bet_money * 3
            money = money + bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        else:
            money = money - bet_money
            print(Fore.RED + Style.BRIGHT + f"> Вы не угадали загаданное число! Теперь у вас {money} рублей!" + Style.RESET_ALL)
    elif user_choice == '3':
        random_knb = random.SystemRandom().choice(["Камень", "Ножницы", "Бумагу"])
        user_knb_choice = input(Fore.MAGENTA + Style.BRIGHT + "> Что вы выбираете? ('к' - камень, 'н' - ножницы, 'б' - бумагу): ")
        if user_knb_choice == "к":
            user_knb = "Камень"
        elif user_knb_choice == "н":
            user_knb = "Ножницы"
        elif user_knb_choice == "б":
            user_knb = "Бумагу"
        print(f"> Вы выбрали {user_knb}, а ваш оппонент выбрал {random_knb}")
        if random_knb == "Камень" and user_knb == "Камень":
            print(Fore.YELLOW + Style.BRIGHT + "> Ничья" + Style.RESET_ALL)
        elif random_knb == "Ножницы" and user_knb == "Ножницы":
            print(Fore.YELLOW + Style.BRIGHT + "> Ничья" + Style.RESET_ALL)
        elif random_knb == "Бумагу" and user_knb == "Бумагу":
            print(Fore.YELLOW + Style.BRIGHT + "> Ничья" + Style.RESET_ALL)
        elif random_knb == "Ножницы" and user_knb == "Камень":
            print(Fore.GREEN + Style.BRIGHT + "> Вы выиграли! Ваша ставка умножается на х2")
            bet_money = bet_money * 2
            money = bet_money + money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_knb == "Камень" and user_knb == "Бумагу":
            print(Fore.GREEN + Style.BRIGHT + "> Вы выиграли! Ваша ставка умножается на х2")
            bet_money = bet_money * 2
            money = bet_money + money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_knb == "Бумагу" and user_knb == "Ножницы":
            print(Fore.GREEN + Style.BRIGHT + "> Вы выиграли! Ваша ставка умножается на х2")
            bet_money = bet_money * 2
            money = bet_money + money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_knb == "Ножницы" and user_knb == "Бумагу":
            print(Fore.RED + Style.BRIGHT + "> Вы проиграли!")
            money = money - bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_knb == "Камень" and user_knb == "Ножницы":
            print(Fore.RED + Style.BRIGHT + "> Вы проиграли!")
            money = money - bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
        elif random_knb == "Бумагу" and user_knb == "Камень":
            print(Fore.RED + Style.BRIGHT + "> Вы проиграли!")
            money = money - bet_money
            print(f"> Теперь у вас {money} рублей!" + Style.RESET_ALL)
    elif user_choice == '4':
        print(Fore.MAGENTA + Style.BRIGHT + "> Подбрасываем монетку..")
        time.sleep(2)
        random_or = random.randint(0, 1)
        user_or = input("> Орёл или решка? ('0' - орёл, '1' - решка): ")
        if user_or == random_or:
            bet_money = bet_money * 2
            money = money + bet_money
            print(Fore.GREEN + Style.BRIGHT + f"> Вы угадали! Теперь у вас {money} рублей!" + Style.RESET_ALL)
        else:
            money = money - bet_money
            print(Fore.RED + Style.BRIGHT + f"> Вы проиграли! Теперь у вас {money} рублей!" + Style.RESET_ALL)
    else:
        print("> Вы ввели неверный режим")
        continue
    if money >= 1000000:
        print(Fore.CYAN + Style.BRIGHT + "> Вы накопили миллион рублей! Игра пройдена!")
        print("> Спасибо, что уделили время :)")
        break