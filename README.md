# Python Assignment BOT Shreyasi

## Overview
This repository contains two Python scripts and an SQL query file:
1. **WeatherData.py**: A user-driven program that collects weather data (temperature and humidity) for multiple cities and provides the average temperature and humidity for each city, handling missing data and input errors.
2. **PrimeFactor.py**: A user-driven program that calculates the prime factorization of a given integer, ensuring valid input and providing a list of prime factors with their respective exponents.
3. **queries.txt**: Contains SQL queries for manipulating a `products` table in a database, specifically to increase the price of all products by 10% and display their updated prices.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Error Handling](#error-handling)

## Prerequisites
- Python 3.x installed on your system.
- A code editor like Visual Studio Code or any other text editor.
- Basic knowledge of Python and terminal/command-line operations.
- An SQL database (such as MySQL, PostgreSQL, or SQLite) to run the queries.

## Installation
1. Clone the repository or download the code files:
   ```bash
   git clone https://github.com/coolCoderD/PythonAssignment.git
   cd PythonAssignment


## Usage
### Running WeatherData.py
1. Navigate to the directory containing `WeatherData.py`.
2. Run the script using the command:
   ```bash
   python WeatherData.py

3. Follow the on-screen instructions to enter the number of weather records, city names, and their respective temperature and humidity data.

### Running PrimeFactor.py
1. Navigate to the directory containing `PrimeFactor.py`.
2. Run the script using the command:
   ```bash
   python PrimeFactor.py

3.Follow the prompt to enter an integer, and the program will display its prime factorization.

### Using SQL Queries in queries.txt
1. Open the `queries.txt` file to view the SQL queries.
2. Copy the content of the file to your SQL database editor.

   

   Make sure that your database has a table named `products` with the columns `id`, `name`, and `price` before running these queries.


   ### File Descriptions

- **WeatherData.py**: A Python script that:
  - Accepts user input for multiple weather records.
  - Handles missing data and input errors.
  - Calculates and displays average temperature and humidity for each city.

- **PrimeFactor.py**: A Python script that:
  - Accepts user input for a single integer.
  - Validates the input and computes its prime factorization.
  - Returns a list of tuples containing prime factors and their exponents.

- **queries.txt**: Contains SQL queries to update and display product prices in a `products` table.

### Error Handling

- **WeatherData.py**: 
  - Handles invalid input (e.g., non-numeric temperature/humidity values) and empty city names.
  - Prompts users for correct input or skips invalid entries.

- **PrimeFactor.py**: 
  - Ensures that the entered value is an integer greater than 1.
  - Displays an appropriate message for invalid inputs.

