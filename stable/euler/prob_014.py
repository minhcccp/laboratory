# From: https://projecteuler.net/problem=14
from typing import Dict, List

if __name__ == "__main__":
    record_dict: Dict[int, int] = {number: 0 for number in range(1, int(1e6))}
    record_dict[1] = 1

    for starting_number in record_dict:
        if not record_dict[starting_number]:

            def transformer(input_number: int) -> int:
                if input_number % 2:
                    return input_number * 3 + 1
                else:
                    return input_number // 2

            result_list: List[int] = [starting_number]
            while not (
                additional_record := record_dict.get((previous := result_list[-1]), 0)
            ):
                result_list.append(transformer(previous))
            else:
                result_list.pop()

            for index, result in enumerate(result_list):
                if result in range(starting_number, int(1e6)):
                    record_dict[result] = len(result_list) - index + additional_record

    # From: https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    print(max(record_dict, key=record_dict.get))
