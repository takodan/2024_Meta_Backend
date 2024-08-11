def read_file(file_name):
    """ Reads in a file.
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """

    with open(file_name, "r") as f:
        content = f.read()
        # print(content)
        # print(type(content))
        return content


def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """

    with open(file_name, "r") as f:
        content = f.readlines()
        return content


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """

    file_lines = file_contents.split("\n")
    with open(output_filename, "w") as f:
        print("Writing:", file_lines[0])
        f.write(file_lines[0].strip())

    return



def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """

    with open(file_name, "r") as f:
        i = 1
        result =[]
        for line in f.readlines():
            if i % 2 == 0:
                # print("r", result)
                result.append(line)
            i += 1
    # print("r", result)
    return result


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """

    with open(file_name , "r") as f:
        content =  list(f.readlines())
        result = list(reversed(content))
        # print(result)
        return result


def main():
    file_contents = read_file("sampletext.txt")
    print("List:", read_file_into_list("sampletext.txt"))
    print()
    write_first_line_to_file(file_contents, "oneline.txt")
    print()
    print("Even:", read_even_numbered_lines("sampletext.txt"))
    print()
    print("Reverse:", read_file_in_reverse("sampletext.txt"))
    print()

if __name__ == "__main__":
    main()