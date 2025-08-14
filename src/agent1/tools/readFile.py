

def readFile(path):
    """
    Reads a file and returns its content as a string.

    :param path: The path to the file to read.
    :return: The content of the file.
    """

    # Open the file in read mode
    with open(path, 'r') as f:
        # Read the file content and return it
        return f.read()
