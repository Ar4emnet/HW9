try:
    with open('text.txt', 'r') as first_file:
        with open('text.txt', 'w') as second_file:
            for line in first_file:
                words = line.split()
                long_words = [word for word in words if len(word) >= 7]
                second_file.write(' '.join(long_words) + '\n')
    first_file.close()
    second_file.close()
except Exception as e:
    print(e)
