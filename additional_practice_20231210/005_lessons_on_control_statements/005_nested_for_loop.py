for i in range(1, 6):
    for num in range(i):
        if num < i - 1:
            # print * with a " " at the back for the non-last *
            print("*", end=" ")
        else:
            # print * with a new line character "\n" for the last *
            print("*", end="\n")
