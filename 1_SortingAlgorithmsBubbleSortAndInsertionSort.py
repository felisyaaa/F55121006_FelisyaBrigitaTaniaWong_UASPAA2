import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def print_iterations(arr, sort_name):
    print(f"\nFirst 5 iterations of {sort_name} Sort:")
    for i in range(min(5, len(arr))):
        print(arr[i], end=" ")
    print("\n")

    print(f"Last 5 iterations of {sort_name} Sort:")
    for i in range(max(len(arr) - 5, 0), len(arr)):
        print(arr[i], end=" ")
    print("\n")


def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33,
           90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84,
           32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6,
           3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Before sorting:")
    print(arr)

    choice = input("1. Bubble Sort\n2. Insertion Sort\nChoose sorting method: ")
    if choice == "1":
        sorted_arr, execution_time = bubble_sort(arr.copy())
        sort_name = "Bubble"
    elif choice == "2":
        sorted_arr, execution_time = insertion_sort(arr.copy())
        sort_name = "Insertion"
    else:
        print("Invalid choice. Program ends.")
        return

    print("\nAfter sorting:")
    print(sorted_arr)

    print_iterations(sorted_arr, sort_name)
    print(f"Sorting computation time: {execution_time} seconds")


if __name__ == "__main__":
    main()
