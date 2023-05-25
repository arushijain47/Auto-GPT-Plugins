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

    #Convert the integers to lists
    num1_list = list(num1)
    num2_list = list(num2)
    
    #Sum the lists
    Tsum = sum(num1_list, num2_list)

    #Convert it to JSON
    data = Tsum.json()
    #Extract the number and return it
    return data["sum"]
