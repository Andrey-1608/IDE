"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """

    После рандомного угадывания числа, применяем геометрическую прогрессию в сторону уменьшения.
    Если схождение меньше 2, чтобы не менять формулу устанавливаем его равным 2 и получается что перебираем по 1.
    
    """
    count = 0
    predict = np.random.randint(1, 101)
    koef = 100

    while number != predict:
        count += 1
        koef = koef / 2
        if koef < 2:
            koef = 2
        if number > predict:
            predict = int(predict + koef/2)
        elif number < predict:
            predict = int(predict - koef/2)
        
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
