hash=[-1]*10
size=10
count=0

def resize():
    global hash, size, count
    old = hash
    size *= 2
    hash = [-1] * size
    count = 0
    for x in old:
        if x != -1 and x != -2:
            insert(x)

def insert(number):
    global count
    if count >= size // 2:
        resize()

    index=number%size
    for i in range(size):
        next=(index+i)%size
        if hash[next] == -1 or hash[next]==-2:
            hash[next]=number
            count+=1
            return
    print("Hash table is full. Cannot insert", number)

def search(number):
    x=number%size
    for i in range(size):
        next=(x+i)%size
        if hash[next]==number:
            return next
        if hash[next]==-1 :
           break
    return -1

def delete(number):
    x=number%size
    for i in range (size):
        next=(x+i)%size
        if hash[next]==number:
            hash[next]=-2
            count-=1
            return next
        if hash[next]==-1:
          break
    return -1
          
while True:
    print("\nMenu:")
    print("1. Insert number")
    print("2. Search number")
    print("3. Display hash table")
    print("4. Delete")
    print("5. Exit")

    choice = input("choice: ")

    if choice == '1':
        num = int(input("Enter number to insert: "))
        insert(num)

    elif choice == '2':
        num = int(input("Enter number to search: "))
        pos = search(num)
        if pos != -1:
            print(f"{num} found at index {pos}")
        else:
            print(f"{num} not found in the hash table.")

    elif choice == '3':
        print("Hash table:", hash)


    elif choice == '4':  
        num=int(input("Enter a number you want to delete: "))
        pos=delete(num)
        if pos!=-1:
            print(f"{num} deleted from index {pos}")
        else:
            print(f"{num} not found in the hash table.")
     

    elif choice == '5':
        print("Exiting.....................")
        break

    else:
        print("Invalid choice")