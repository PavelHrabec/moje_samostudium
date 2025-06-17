



def div(start, end):
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0 and num % 3 != 0:
            result.append(num)
    return result


print(div(0, 20))  # [2, 4, 8, 10, 14, 16, 20]

