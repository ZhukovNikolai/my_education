"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    # Старый алгоритм угадывания
    # while True:
    #     count += 1
    #     predict_number = np.random.randint(1, 101)  # предполагаемое число
    #     if number == predict_number:
    #         break  # выход из цикла если угадали
    # return count 

    
    low = 1    # нижняя граница поиска
    high = 101    # верхняя граница 
    mid = high // 2    #середина
    
    while True:
        count += 1
        predict_number = mid  # предполагаемое число, всегда середина
        if number > predict_number:
            low = mid+1       # если число больше, исключаем все, что меньше середины
        elif number < predict_number:
            high = mid-1      # если число меньше, то все, что больше середины
        else:
            break
        mid = (low + high)//2 #определяем новую середину
    return count 


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
