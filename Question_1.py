def count_cjeb(word):
    """
    The function will find all occurences of words that start with "C" and end with "jeb"
    It will do this with words of unlimited length
    :param word: the string to be searched
    :return: the number of occurences of the pattern
    """
    words = word.split()  # Split text into words
    count = 0 # define var count

    for word in words:
        if len(word) >= 4 and word[0] == "C" and word[-3:] == "jeb":  # Must match both conditions
            count += 1

    return count

# Examples:
print(count_cjeb("Cexamplejeb Ctextjeb Cvalidwordjeb"))
print(count_cjeb("Chello worldjeb Ctextjeb"))
print(count_cjeb("Cnotvalid anotherword jebtest"))
print(count_cjeb("random text Cword jeb Cvalidjeb"))
print(count_cjeb("Cstart butnotend Cotherword jebend"))
print(count_cjeb(""))