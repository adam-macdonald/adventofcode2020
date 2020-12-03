with open("input.txt", "r") as file:
    buffer = file.read()
    x = 1
    y = 1
    width = len(buffer.splitlines()[0])
    height = len(buffer.splitlines())
    trees_hit = 0

    for i in range(0, height, 1):
        row = buffer.splitlines()[i]
        mod = x % width
        # task states the pattern repeats, we can treat x values > width as if
        # they were just starting from the beginning of the row again

        if row[mod - 1] == "#":
            # hit tree
            trees_hit += 1
        if row[mod - 1] == "." and y != 1:
            # didnt hit tree
            pass

        # increment x & y coords
        x += 3
        y += 1

    print("Trees hit: " + str(trees_hit)) # output