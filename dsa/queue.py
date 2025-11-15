queue = []

def enqueue():
    item = input("Enter element to enqueue: ")
    queue.append(item)
    print("Enqueued:", item)

def dequeue():
    if not queue:
        print("Queue Underflow (empty queue)")
    else:
        item = queue.pop(0)
        print("Dequeued:", item)

def display():
    print("Queue:", queue)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        enqueue()
    elif ch == "2":
        dequeue()
    elif ch == "3":
        display()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")