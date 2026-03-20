def count_words(file_path):
    with open(file_path , 'r' )as f :
        content = f.read()

    words = content.split()

    total = len(words)

    print(f"total of words is = {total}")

count_words('archive.txt')
