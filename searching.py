from pathlib import Path
import json
import matplotlib.pyplot as plt
import time
import random

def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open (file_name, "r") as f:
        data = json.load(f)
    if field not in data:
        return None

    return data[field]

    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

def linear_search(sequence, wanted_number):
    positions = []
    for i, value in enumerate(sequence):
        if value == wanted_number:
            positions.append(i)
    return {"positions": positions, "count": len(positions)}

def binary_search(sez, number):
    left = 0
    right = len(sez) - 1
    while left <= right:
        middle_point = (left + right) // 2

        if sez[middle_point] == number:
            return middle_point
        if sez[middle_point] < number:
            left = middle_point + 1
        else:
            right = middle_point - 1

    return None

def main():
    unordered = read_data("sequential.json", "unordered_numbers")
    target = 8
    linear_result = linear_search(unordered, target)
    print(linear_result)


sizes = [100, 500, 1000, 5000, 10000]
times_linear = []
times_binary = []

for n in sizes:
    sequence = ordered_sequence(n)

    start = time.perf_counter()
    res = binary_search(seq, 5)
    time = time.perf_counter() - start
    times_binary.append(time)

plt.plot(sizes, times_linear)
plt.plot(sizes, times_binary)
plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()




# if __name__ == "__main__":
#     main()
