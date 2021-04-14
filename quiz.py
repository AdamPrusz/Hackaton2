def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as er:
        print("error", err)

    return(num_each, leftovers)

