def days_passed_since_birth(birthday):
    """
    Calculates the number of days passed since the given birthday,
    excluding the birth year and the current year.

    Ensures the input format is "DD-MM-YYYY". If not, prints "Invalid format".

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The number of days passed (excluding birth year and current year) or "Invalid format"
    """

    # Step 1: Check if the input is exactly 10 characters long
    if len(birthday) != 10:
        print("Invalid format")
        return

    # Step 2: Check if the third and sixth characters are '-'
    if birthday[2] != "-" or birthday[5] != "-":
        print("Invalid format")
        return

    # Step 3: Try extracting the birth year (last 4 characters)
    try:
        birth_year = int(birthday[6:])  # Convert "YYYY" to an integer
    except ValueError:  # If conversion fails, input is invalid
        print("Invalid format")
        return

    current_year = 2025

    # Step 4: Calculate the number of full years passed (excluding birth and current year)
    full_years = (current_year - birth_year - 2)

    # Step 5: Multiply by 365 to get the total number of days
    total_days = full_years * 365

    return total_days

# Example Test Cases
print(days_passed_since_birth("21-02-2000"))  # Expected: 8395
print(days_passed_since_birth("10-10-1995"))  # Expected: 9855
print(days_passed_since_birth("01-01-2010"))  # Expected: 4745

# Invalid Cases
print(days_passed_since_birth("sadfasd"))  # Expected: "Invalid format"
print(days_passed_since_birth("21-02-20X5"))  # Expected: "Invalid format"
print(days_passed_since_birth("21022000"))  # Expected: "Invalid format"
print(days_passed_since_birth("21/02/2000"))  # Expected: "Invalid format"
