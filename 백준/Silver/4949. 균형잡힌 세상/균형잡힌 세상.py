while True:
    sentence = input()
    if sentence == ".":
        break

    stack = []

    for s in sentence:
        if s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)

        elif s == '(' or s == '[':
            stack.append(s)

    if stack:
        print("no")
    else:
        print("yes")
        