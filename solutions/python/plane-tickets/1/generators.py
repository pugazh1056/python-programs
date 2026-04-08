import string
import random

def generate_seat_letters(number):
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    count = 0
    row = 1

    while count < number:
        if row == 13:
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:
            if count >= number:
                break
            yield f"{row}{letter}"
            count += 1

        row += 1


def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = seat + flight_id + "000"
        yield code[:12]