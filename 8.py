def is_valid_url(url):
    """
    Checks if a given string is a valid URL
    A valid URL:
    - Contains at least one dot '.'
    - Has characters before and after the dot

    :param url: The string to check
    :return: True if it's a valid URL, False otherwise
    """

    # Step 1: Find the first dot '.' in the URL
    dot_index = -1  # Initialize to -1 to check if a dot exists

    for i in range(len(url)):
        if url[i] == ".":  # Find first dot
            dot_index = i
            break

    # Step 2: If there's no dot, it's not a valid URL
    if dot_index == -1:
        return False

    # Step 3: Ensure there is at least one character before and after the dot
    if dot_index == 0 or dot_index == len(url) - 1:
        return False

    return True  # Passed all checks


# Example Test Cases
print(is_valid_url("http://google.com"))
print(is_valid_url("https://example.org"))
print(is_valid_url("google.com"))
print(is_valid_url("www.site.net"))
print(is_valid_url("notavalidurl"))
print(is_valid_url("http://site."))
print(is_valid_url(".com"))
print(is_valid_url("ftp://example.com"))