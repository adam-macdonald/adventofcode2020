with open("input.txt", "r") as file:
    buffer = file.read()
    expenses = buffer.splitlines()

    for expense in expenses:
        for comparison in expenses:
            for second_comparison in expenses:
                if (int(expense) + int(comparison) + int(second_comparison)) == 2020:
                    print(str(int(expense) * int(comparison) * int(second_comparison)))