with open("input.txt", "r") as file:
    buffer = file.read()
    x = 1
    y = 1
    width = len(buffer.splitlines()[0])
    height = len(buffer.splitlines())
    trees_hit = 0
    output = ""

    for row in buffer.splitlines():
        # task states the pattern repeats, we can treat x values > width as if
        # they were just starting from the beginning of the row again
        mod = x % width

        if row[mod - 1] == "#":
            # hit tree
            output = row[:mod - 1] + "X" + row[mod - 1:]
            trees_hit += 1
        if row[mod - 1] == "." and y != 1:
            # didnt hit tree
            output = row[:mod - 1] + "O" + row[mod - 1:]
        # increment x & y coords
        x += 3
        y += 1

    print("Trees hit: " + str(trees_hit)) # output