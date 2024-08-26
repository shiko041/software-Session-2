def format_string(s, operations):
    length = len(s)

    def __uppercase(s):
        new_s = ''
        for i in range(length):
            if 'a' <= s[i] <= 'z':
                new_s += chr(ord(s[i]) - 32)
            else:
                new_s += s[i]
        return new_s

    def __reverse(s):
        new_s = ''
        for i in range(length - 1, -1, -1):
            new_s += s[i]
        return new_s

    def __capitalize(s):
        if 'a' <= s[0] <= 'z':
            new_s = chr(ord(s[0]) - 32) + s[1:]
        else:
            new_s = s
        return new_s

    for op in operations:
        if op == 'uppercase':
            s = __uppercase(s)
        elif op == 'reverse':
            s = __reverse(s)
        elif op == 'capitalize':
            s = __capitalize(s)
        else:
            print("Unknown function")
            return

    return s

s = "hello world"
operations = ['uppercase', 'reverse']
print(format_string(s, operations))
