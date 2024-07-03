try:
    n = int(input("Enter the number of elements: "))

    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    max_element = max(arr) if arr else 0
    hash_table = [0] * (max_element + 1)

    for i in range(n):
        hash_table[arr[i]] += 1

    q = int(input("Enter the number of queries: "))

    for _ in range(q):
        number = int(input("Enter query number: "))
        if number < len(hash_table):
            print(hash_table[number])
        else:
            print(0)

except ValueError as e:
    print("Invalid input! Please enter integers only.")

    
