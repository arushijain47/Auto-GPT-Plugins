import requests


def get_num_astronauts():
    """Get the sum of two .

    Args:
        None

    Returns:
        int: The number of astronauts in space.
    """
    #Get the data
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    Tsum = num1 + num2
    
    #Convert it to JSON
    data = Tsum.json()
    #Extract the number and return it
    return data["number"]
