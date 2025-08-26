from collections import deque
from datetime import datetime

def display_menu():
    print("\n--- Call Center Menu ---")
    print("1. Add Caller to Operator")
    print("2. Serve Caller from Operator")
    print("3. Show All Queues")
    print("4. Show Call History")
    print("5. Show Average Waiting Time")
    print("6. View Specific Queue")
    print("7. Show Average Waiting Time for Specific Queue")
    print("8. Check If Queue is Empty")
    print("9. Exit")

def main():
    n = int(input("Enter the number of operators: "))
    queues = [deque() for _ in range(n)]
    call_history = [[] for _ in range(n)]

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            operator = int(input(f"Choose operator (1 to {n}): ")) - 1
            if 0 <= operator < n:
                caller = input("Enter caller name: ")
                join_time = datetime.now()
                queues[operator].append((caller, join_time))
                print(f"Added caller '{caller}' to Operator {operator + 1}'s queue.")
            else:
                print("Invalid operator number.")

        elif choice == '2':
            operator = int(input(f"Choose operator (1 to {n}): ")) - 1
            if 0 <= operator < n:
                if queues[operator]:
                    caller, join_time = queues[operator].popleft()
                    served_time = datetime.now()
                    waiting_time = (served_time - join_time).total_seconds()
                    call_history[operator].append({'caller': caller, 'waiting_time': waiting_time})
                    print(f"Caller '{caller}' served from Operator {operator + 1}'s queue. Waiting time: {waiting_time:.2f} seconds.")
                else:
                    print("Queue is empty.")
            else:
                print("Invalid operator number.")

        elif choice == '3':
            print("\nAll Queues:")
            for i in range(n):
                if not queues[i]:
                    print(f"Operator {i + 1}: No callers")
                else:
                    callers = [c[0] for c in queues[i]]
                    print(f"Operator {i + 1}: {callers}")

        elif choice == '4':
            print("\nCall History:")
            for i in range(n):
                print(f"Operator {i + 1}:")
                if not call_history[i]:
                    print("  No calls served yet.")
                else:
                    for record in call_history[i]:
                        print(f"  Caller: {record['caller']}, Waiting Time: {record['waiting_time']:.2f} seconds")

        elif choice == '5':
            print("\nAverage Waiting Time Per Operator:")
            for i in range(n):
                if not call_history[i]:
                    print(f"Operator {i + 1}: No calls served yet.")
                else:
                    avg_wait = sum(record['waiting_time'] for record in call_history[i]) / len(call_history[i])
                    print(f"Operator {i + 1}: {avg_wait:.2f} seconds")

        elif choice == '6':
            operator = int(input(f"Enter operator number (1 to {n}): ")) - 1
            if 0 <= operator < n:
                if queues[operator]:
                    callers = [c[0] for c in queues[operator]]
                    print(f"Operator {operator + 1} queue: {callers}")
                else:
                    print(f"Operator {operator + 1}'s queue is empty.")
            else:
                print("Invalid operator number.")

        elif choice == '7':
            operator = int(input(f"Enter operator number (1 to {n}): ")) - 1
            if 0 <= operator < n:
                if not call_history[operator]:
                    print(f"Operator {operator + 1}: No calls served yet.")
                else:
                    avg_wait = sum(record['waiting_time'] for record in call_history[operator]) / len(call_history[operator])
                    print(f"Operator {operator + 1} Average Waiting Time: {avg_wait:.2f} seconds")
            else:
                print("Invalid operator number.")

        elif choice == '8':
            operator = int(input(f"Enter operator number (1 to {n}): ")) - 1
            if 0 <= operator < n:
                if not queues[operator]:
                    print(f"Operator {operator + 1}'s queue is empty.")
                else:
                    print(f"Operator {operator + 1}'s queue is not empty.")
            else:
                print("Invalid operator number.")

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
