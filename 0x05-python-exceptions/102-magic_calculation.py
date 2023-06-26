#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / num
        except Exception:
            result = b + a
            break
    return (result)
