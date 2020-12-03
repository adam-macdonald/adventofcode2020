with open("input.txt", "r") as file:
    buffer = file.read()
    lines = buffer.splitlines()
    i = 0

    for line in lines:
        policy = line.split(" ")[0]
        requirement = line.split(" ")[1][:-1]
        password = line.split(" ")[2]

        if password.count(requirement) < int(policy.split("-")[0]):
            continue
        if password.count(requirement) > int(policy.split("-")[1]):
            continue
        i += 1

    print(str(i))