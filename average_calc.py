#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/14/2023
# This program will generate 10 random numbers between 1 and 100.
# It will then calculate the average of all the numbers.
# My program uses a list and a loop to do what is listed above.

# Importing math module and my constants.
import random
import constants


def main():
    # Explaining my program to the user.
    print(
        "Welcome! My program will generate 10 numbers from 1 to 100 and will calculate their average."
    )

    # Initializing my counter and sum to 0
    counter = 0
    sum = 0

    # Declaring my variable as a list.
    list_of_int = []

    # This loop generates the random numbers and adds them to the list.
    for counter in range(0, constants.MAX_ARRAY_SIZE):
        # Generating a random number.
        random_number = random.randint(constants.MIN_NUMBER, constants.MAX_NUMBER)

        # Appending the list to the random numbers.
        list_of_int.append(random_number)

        # Displaying the generated numbers.
        print(
            "{} added to the list at position {}".format(list_of_int[counter], counter)
        )

    # The second loop calculates the sum and average of the numbers.
    for counter in range(0, constants.MAX_ARRAY_SIZE):
        # Setting my sum variable to add my list to my counter, which will calculate the sum of all the numbers.
        sum += list_of_int[counter]

    # Calculating the average.
    # Dividing the sum of all the generated numbers by 10 (amount of numbers).
    average = sum / constants.MAX_ARRAY_SIZE

    # Displaying the average to the user.
    print("\nThe average of these numbers is {}".format(average))


if __name__ == "__main__":
    main()
