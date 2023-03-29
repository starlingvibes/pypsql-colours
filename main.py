#!/usr/bin/env python3

import os
import psycopg
import random
from dotenv import load_dotenv

load_dotenv()

# mapping the days of the week to the colours worn
day_to_colour = {
    'MONDAY': 	["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    'TUESDAY': ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    'WEDNESDAY': ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    'THURSDAY': ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    'FRIDAY': ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"],
}

# mapping the colours to the frequency of the colours worn
colour_to_frequency = {}
for key, values in day_to_colour.items():
    for colour in values:
        if colour in colour_to_frequency:
            colour_to_frequency[colour] += 1
        else:
            colour_to_frequency[colour] = 1

# mapping the colours to the frequency of the colours worn
colour_to_frequency = {}
for key, values in day_to_colour.items():
    for colour in values:
        if colour in colour_to_frequency:
            colour_to_frequency[colour] += 1
        else:
            colour_to_frequency[colour] = 1

# Connect to an existing database
with psycopg.connect(f"dbname=bincom user=postgres password={os.getenv('PASSWORD')}") as conn:
    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE colours_and_frequencies (
                id serial PRIMARY KEY,
                colour text,
                frequency integer)
            """)

        for key, value in colour_to_frequency.items():
            cur.execute(
                "INSERT INTO colours_and_frequencies (colour, frequency) VALUES (%s, %s)",
                (key, value))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM colours_and_frequencies")
        cur.fetchone()
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()


def get_mean_colour():
    """
    Get the mean colour throughout the week

    Returns: the mean colour as a string
    """
    out = []
    for key, values in day_to_colour.items():
        for colour in values:
            out.append(colour)

    sum_freq = sum(colour_to_frequency.values())
    mean_freq = sum_freq // len(colour_to_frequency)
    return out[mean_freq]


def get_colour_frequency():
    """
    Get the most frequent colour worn throughout the week

    Returns: the most frequent colour worn throughout the week
    """
    max_freq = max(colour_to_frequency.values())
    for k, v in colour_to_frequency.items():
        if v == max_freq:
            return k


def get_median_colour():
    """
    Get the median colour throughout the week

    Returns: the median colour as a string
    """
    out = []
    for key, values in day_to_colour.items():
        for colour in values:
            out.append(colour)
    return out[len(out) // 2]


def get_variance_of_colours():
    """
    Get the variance of the colours worn throughout the week

    Returns: the variance of the colours worn throughout the week
    """
    out = []
    for key, values in day_to_colour.items():
        for colour in values:
            out.append(colour)

    sum_freq = sum(colour_to_frequency.values())
    mean_freq = sum_freq // len(colour_to_frequency)
    deviations = [(x - mean_freq) ** 2 for x in colour_to_frequency.values()]
    variance = sum(deviations) // len(colour_to_frequency)
    return out[variance]


def probability_colour_is_red():
    """
    Get the probability that the colour worn is red

    Returns: the probability that the colour worn is red
    """
    probability = colour_to_frequency['RED'] / \
        sum(colour_to_frequency.values())
    return f"{probability:.2%}"


def recursive_search(num_list, target):
    """
    This function performs a recursive binary search on a list of numbers to find the target value.
    """
    if not num_list:
        return False

    mid_index = len(num_list) // 2
    mid_value = num_list[mid_index]

    if mid_value == target:
        return True
    elif mid_value > target:
        return recursive_search(num_list[:mid_index], target)
    else:
        return recursive_search(num_list[mid_index + 1:], target)


"""
2nd phase of assessment
"""


def random_binary():
    """
    Program that generates random 4 digits number of 0s and 1s and
    convert the generated number to base 10.
    """
    res = ""

    for _ in range(4):
        random_bit = random.randint(0, 1)
        res += str(random_bit)
    return f"{int(res, 2)}"


def sum_first_50_fibonacci_numbers():
    """
    Program that returns the sum of the first 50 Fibonacci numbers
    """
    fib1, fib2 = 0, 1
    total_sum = 0

    for i in range(50):
        fib = fib1 + fib2
        total_sum += fib

        # update the values of the previous two Fibonacci numbers
        fib1, fib2 = fib2, fib

    return total_sum


if __name__ == "__main__":
    print(get_mean_colour())
    print(get_colour_frequency())
    print(get_median_colour())
    print(get_variance_of_colours())
    print(probability_colour_is_red())
    print(random_binary())
    print(sum_first_50_fibonacci_numbers())
    print(recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
