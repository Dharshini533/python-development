stack = []

def push():
    item = input("Enter element to push: ")
    stack.append(item)
    print("Pushed:", item)

def pop():
    if not stack:
        print("Stack Underflow (empty stack)")
    else:
        item = stack.pop()
        print("Popped:", item)

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display():
    print("Stack:", stack)

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        push()
    elif ch == "2":
        pop()
    elif ch == "3":
        peek()
    elif ch == "4":
        display()
    elif ch == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")