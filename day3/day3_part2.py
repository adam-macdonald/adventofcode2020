def main():
    # just passing the parameters for how the toboggan travels down the slope
    # to the function which calculates if a tree has been hit (same as part 1)
    # ... then prints the result to the console
    print(traverse_slope(1, 1) * traverse_slope(3, 1) * traverse_slope(5, 1) * traverse_slope(7, 1) * traverse_slope(1, 2))

def traverse_slope(x_incr, y_incr):
    with open("input.txt", "r") as file:
        buffer = file.read()
        x = 1
        y = 1
        width = len(buffer.splitlines()[0])
        height = len(buffer.splitlines())
        trees_hit = 0

        # note use of y_incr if the speed down the hill is > 1
        for i in range(0, height, y_incr):
            row = buffer.splitlines()[i] # get current row
            mod = x % width

            if row[mod - 1] == "#":
                # hit tree
                trees_hit += 1
            if row[mod - 1] == "." and y != 1:
                # didnt hit tree
                pass

            # increment x & y coords
            x += x_incr
            y += y_incr
        return trees_hit

if __name__ == "__main__":
        main()