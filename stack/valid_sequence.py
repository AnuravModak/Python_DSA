def validateStackSequences(pushed, popped):
    stack = []
    i = 0
    j = 0
    while i < len(pushed):
        while len(stack) > 0 and stack[-1] == popped[j]:
            stack.pop(len(stack) - 1)
            j += 1
        stack.append(pushed[i])
        i += 1
    while len(stack) > 0:
        if not stack[-1] == popped[j]:
            return False
        stack.pop(len(stack) - 1)
        j += 1
    return True

print(validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))