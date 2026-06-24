def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors_sum = 0

    for i in range(1, number // 2 + 1):
        if number % i == 0:
            factors_sum += i

    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    else:
        return "deficient"