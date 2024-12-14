"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """

    После рандомного угадывания числа, находим середину между между угадонным числом и мксимумом или минимумом
    и эту середину опять сравниваем с загадонным числом, и так в цикле
    
    """
    count = 1
    predict = np.random.randint(1, 101)
    
    znach_min = 0
    znach_max = 100

    while number != predict:
        count += 1
        if (znach_max - znach_min) < 3:
            predict+=1
        if number > predict:
            znach_min = predict
            predict = int((znach_max+predict) / 2)
           
        elif number < predict:
            znach_max = predict
            predict = int((znach_min+predict) / 2)
            
        
        print(number,predict)
        
        

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
