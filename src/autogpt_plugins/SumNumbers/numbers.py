def get_sum_numbers():
    """Get the sum of two numbers.

    Args:
        None

    Returns:
        int: The sum of two numbers.
    """
    #Get the data
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    #Convert the integers to lists
    #num1_list = list(num1)
    #num2_list = list(num2)
    
    #Sum the lists
    #Tsum = sum(num1_list, num2_list)
    Tsum = num1 + num2
    return(Tsum)

    #Convert it to JSON
    
    #json_string = json.dumps({"Tsum": Tsum})

    #Extract the number and return it
    #return json_string["Tsum"]
