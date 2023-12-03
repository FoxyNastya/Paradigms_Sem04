import math


def pearson_correlation(array1, array2):
   
    # Расчет корреляции Пирсона. Проверка на то, что массивы одинаковой длины
    if len(array1) != len(array2):
        raise ValueError("Внимание, массивы должны быть одинаковой длины")

    n = len(array1)

    # Расчет среднего значения
    mean_x = sum(array1) / n
    mean_y = sum(array2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array1]) / float(len(array1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array2]) / float(len(array2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array1, array2)]) / float(len(array1)) 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array1 = [1, 2, 3, 4, 5, 7, 77]
array2 = [6, 7, 8, 9, 5, 6, 7]

correlation = round(pearson_correlation(array1, array2), 4)
print(f"Корреляция Пирсона: {correlation}")
