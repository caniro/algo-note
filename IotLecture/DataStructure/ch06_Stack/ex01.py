# 스택의 기본

SIZE = 5
stack = [None for _ in range(SIZE)]
# stack = [None] * SIZE
top = -1

top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'
print('바닥:', stack)

data = stack[top]
stack[top] = None
top -= 1
print('pop-->', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop-->', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop-->', data)

print(stack)
