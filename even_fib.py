from typing import List


def get_even_fib(number: int) -> List:
    result = [0] if number > 0 else []
    pre_prev, prev = 0, 1
    while len(result) < number:
        current = pre_prev + prev
        if current % 2 == 0:
            result.append(current)
        pre_prev = prev
        prev = current
    return result


if __name__ == '__main__':
    len_result_seq = int(input('Enter the length of result sequence:\n'))
    print(f'Result sequence: {get_even_fib(len_result_seq)}')
