#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    return 0 
    f=open(filename).read()
    r=f.split(",")
    l=[]
    for i in r:
        l.append(int(i))
    return l
print(read_file(filename="data.txt"))

#Print list from file
