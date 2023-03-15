from collections import deque

def reverse(s):
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(s)))
if __name__ == '__main__':
 
    s = 'Reverse me'
    s = reverse(s)
    print(s)