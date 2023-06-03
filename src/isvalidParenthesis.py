def isValid(string):
    if len(string) % 2 != 0:
        return False

    check_stack = []
    # last_p = string[0]

    for parenthesis in string:
        # print(f"last_p: {last_p}")

        if not check_stack:
            last_p = parenthesis

        check_stack.append(parenthesis)

        print(f"stack looks like: {check_stack}")

        if last_p == "(":
            next_shud = ")"

        elif last_p == "{":
            next_shud = "}"

        elif last_p == "[":
            next_shud = "]"

        else:
            return False

        if parenthesis == next_shud:
            check_stack.pop()
            if check_stack:
                check_stack.pop()

            if check_stack:
                last_p = check_stack[-1]

            print(f"parenthesis matched : stack looks like: {check_stack}")

        else:
            last_p = parenthesis

    return len(check_stack) == 0


print(isValid("()])"))
