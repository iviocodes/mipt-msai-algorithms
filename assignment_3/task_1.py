def is_regular(str):
    stack = []
    brackets_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for char in str:
        if char in brackets_dict:
            stack.append(char)
        else:
            if len(stack) == 0 or brackets_dict[stack.pop()] != char:
                return False

    return True if len(stack) == 0 else False


if __name__ == "__main__":
    print("yes" if is_regular(input()) else "no")
