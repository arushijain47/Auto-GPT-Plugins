def get_sum_numbers():
    """Get the sum of two .

    Args:
        None

    Returns:
        int: The sum of two numbers.
    """
    #Get the data
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    Tsum = num1 + num2
    
    #Convert it to JSON
    data = Tsum.json()
    #Extract the number and return it
    return data["number"]
