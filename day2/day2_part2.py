with open("input.txt", "r") as file:
    buffer = file.read()
    lines = buffer.splitlines()
    i = 0

    for line in lines:
        policy = line.split(" ")[0]
        requirement = line.split(" ")[1][:-1]
        password = line.split(" ")[2]
        pos_a = int(policy.split("-")[0])
        pos_b = int(policy.split("-")[1])

        # world's most horrendous xor below, i have slept 3 hours today idfc
        if password[pos_a - 1] == requirement and password[pos_b - 1] == requirement:
            continue
        if password[pos_a - 1] == requirement:
            i += 1
        if password[pos_b - 1] == requirement:
            i += 1


    print(str(i))