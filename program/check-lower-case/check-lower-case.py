def is_lower_case(char: str) -> bool:
    if char.lower() == char:
        return True
    else:
        return False


char_inp = input()
i
if is_lower_case(char_inp):
    print("Lower Case")
else:
    print("Not Lower Case")
