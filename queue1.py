from collections import deque

def display_menu():
    print("\n--- Call Center Menu ---")
    print("1. Add Caller to Operator")
    print("2. Serve Caller from Operator")
    print("3. Show Queues")
    print("4. Exit")

def main():
   
    n = int(input("Enter the number of operators: "))


    queues = []
    for i in range(n):
        queues.append(deque())

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':

            operator = int(input(f"Choose operator (1 to {n}): ")) - 1
            if 0 <= operator < n:
                caller = input("Enter caller name: ")
                queues[operator].append(caller)
                print(f"Added caller '{caller}' to Operator {operator + 1}'s queue.")
            else:
                print("Invalid operator number.")

        elif choice == '2':

            operator = int(input(f"Choose operator (1 to {n}): ")) - 1
            if 0 <= operator < n:
                
                if len(queues[operator]) > 0:
                    served = queues[operator].popleft()
                    print(f"Caller '{served}' served from Operator {operator + 1}'s queue.")
                else:
                    print("Queue is empty.")
            else:

                print("Invalid operator number.")

        elif choice == '3':
            print("\nQueues:")
            for i in range(n):
                if len(queues[i]) == 0:
                    print(f"Operator {i + 1}: No callers")
                else:
                    print(f"Operator {i + 1}: {list(queues[i])}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()              