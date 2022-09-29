DEBUG = True


def corpFlightBookings(bookings, n):
    print("Bookings = ", bookings)
    myList = [0] * (n + 2)
    for start, end, val in bookings:
        myList[start] += val
        myList[end + 1] -= val
        if DEBUG:
            print(f"start = {start}, end = {end}, val = {val}.")
            print("myList = ", myList)
    if DEBUG: print("finish first stage.")
    for i in range(1, n + 2):
        myList[i] += myList[i - 1]
        if DEBUG:
            print("myList = ", myList, end="\n")
    return myList[1:-1]


# corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)

corpFlightBookings([[3, 3, 5], [1, 3, 20], [1, 2, 15]], 3)
