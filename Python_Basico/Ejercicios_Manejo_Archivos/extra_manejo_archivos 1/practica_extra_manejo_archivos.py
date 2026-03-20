def read_in_one_line(input_file, output_file):

    # Read all lines of the original file
    with open(input_file, 'r') as file:
        lines = file.read()
    print(lines)
    # Join into a single line
    one_line = " ".join(line.strip() for line in lines)

    # keep in new archive
    with open(output_file, 'w') as file:
        file.write(one_line)
    print(one_line)
    print("File successfully converted to a single line.")

read_in_one_line("text.txt", "one_line.txt")

