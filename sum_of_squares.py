def sum_of_squares(n):
    list_of_squares = []
    for side_of_square in range(1, n):
        square_volume = pow(side_of_square, 2)
        if square_volume < n:
            list_of_squares.append(square_volume)
        else:
            break
    # couples of volume search
    list_of_couples_squares = []
    for first_square in list_of_squares:
        for second_square in list_of_squares:
            if (first_square + second_square) == n:
                couple_of_squares = (first_square, second_square)
                list_of_couples_squares.append(couple_of_squares)

    if len(list_of_couples_squares):
        for pair_of_squares in list_of_couples_squares:
            # In Pycharm it works fine, but www.umimeprogramovat.cz does not support it! Why?
            # print (f'{n} = {pair_of_squares[0]} + {pair_of_squares[1]}')

            # This is older way and isnot recommended. But www.umimeprogramovat.cz accepted it
            print(n, "=", pair_of_squares[0], "+", pair_of_squares[1])

    else:
        print("Nejde to.")


if __name__ == "__main__":
    sum_of_squares(13)
    print("---")
    sum_of_squares(14)
