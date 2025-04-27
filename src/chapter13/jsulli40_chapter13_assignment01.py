#!/usr/bin/env python3
"""
This module models and visualizes projected population growth of cities.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    March 27, 2025

Chapter
    13

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter13/jsulli40_chapter13_assignment01.py

Problem Description
    Write a program (function) to create a database called
    population_(your initials). For ex: population_SM would be my database.
    Create a table named population with the following fields;
        1. City, 2. year, 3. population.
    Choose 10 cities in Florida and insert data into the population table for
    the year 2023.
    Create a function to the simulate population growth for the next 20 years
    at a 2% growth rate for each year. Insert this data into the population
    table.
    Using matplotlib, create a function to show the population growth for a
    city. Let the user know the 10 cities as options and ask them to choose
    one and display the population growth for the city visually.
    This assignment will have at least three functions.
    Submit your .py file in this assignment and in your repository.
    You DO NOT NEED a technical design document for this assignment.
"""

import matplotlib.pyplot as plt
import numpy as np

DATA_ORIG = [
    ("Jacksonville", 2023, 985843),
    ("Miami", 2023, 455924),
    ("Tampa", 2023, 403364),
    ("Orlando", 2023, 320742),
    ("St. Petersburg", 2023, 263553),
    ("Port St. Lucie", 2023, 245021),
    ("Cape Coral", 2023, 224455),
    ("Hialeah", 2023, 221300),
    ("Tallahassee", 2023, 202221),
    ("Fort Lauderdale", 2023, 184255)
]
"""
Original data for population table.

Top ten cities in Florida by population in 2023, as sourced from: 
https://www2.census.gov/programs-surveys/popest/tables/2020-2023/cities/totals/SUB-IP-EST2023-POP-12.xlsx .

See ./SUB-IP-EST2023-POP-12.xlsx for local version, retrieved 04/27/2025.
"""


def main():
    """
    Entry function for when code is invoked directly.

    Get data, simulate growth, and plot specific city with projected growth.
    """
    population_data = get_data()
    population_data = simulate_growth(population_data)
    plot_population_growth(population_data)


def get_data() -> np.ndarray:
    """
    Creates a numpy structured array with data from DATA_ORIG.

    Returns:
        np.ndarray: A structured NumPy array containing data for city (str),
            year (int), and population (int).
    """
    return np.array(DATA_ORIG, dtype=[
        ("city", "U50"),
        ("year", "i4"),
        ("population", "i8")
    ])


def simulate_growth(population_data: np.ndarray) -> np.ndarray:
    """
    Simulate population growth for the next 20 years at a 2% growth rate for
    each city in population data.

    Args:
        population_data (np.ndarray): The original population data.

    Returns:
        np.ndarray: A structured NumPy array containing both the original and
            simulated population data.
    """
    growth_list = []

    #   Iterate over each unique city in orig data.
    cities = np.unique(population_data["city"])
    for city in cities:
        #   Filter orig data by city and sort by year.
        city_data = population_data[population_data["city"] == city]
        city_data = np.sort(city_data, order="year")

        #   Retrieve the latest year and its associated population.
        data_year = city_data[-1]["year"]
        population = city_data[-1]["population"]

        #   Simulate growth for the next 20 years.
        for year in range(data_year + 1, data_year + 21):
            population = int(population * 1.02)
            growth_list.append((city, year, population))

    #   Return orig data concatenated with growth data.
    growth_data = np.array(growth_list, dtype=population_data.dtype)
    return np.concatenate((population_data, growth_data))


def plot_population_growth(population_data: np.ndarray) -> None:
    """
    Retrieves city from user and plots population data for that city.

    Args:
        population_data: The population data for all available cities to plot.
    """
    #   Print unique city names for user to choose from.
    print("Available Cities to Plot")
    cities = np.unique(population_data['city'])
    index_width = len(str(len(cities)))
    for index, city in enumerate(cities, start=1):
        print(f"{index:0{index_width}d}.\t{city}")

    #   Retrieve city index to print.
    input_index = int(input("\nEnter the number corresponding to the city " +
                            "to view: "))

    #   Validate input.
    if 1 <= input_index <= len(cities):
        #   Retrieve sorted data for selected city.
        selected_city = cities[input_index - 1]
        city_data = population_data[population_data['city'] == selected_city]
        city_data = np.sort(city_data, order='year')
        #   Plot year and population data for selected city.
        years = city_data['year']
        populations = city_data['population']
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f"Population Growth of {selected_city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.tight_layout()
        plt.legend([selected_city])
        plt.show()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
