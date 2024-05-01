class Insertion:
    @staticmethod
    def insertion_sort(array):
        for index in range(1, len(array)):  # Iterate through the array starting from the second element
            print("Iteration", index)
            key = array[index]  # Select the current element to be inserted
            position = index - 1  # Initialize a pointer to the previous element
            print("Analyzing element at index", position, "(", array[position], ")", "to element at index", position + 1, "(", array[position + 1], ")")
            while position >= 0 and key < array[position]:  # Move elements of arr[0..index-1] that are greater than key, to one position ahead of their current position
                print("  Moving element", array[position], "to the right")
                array[position + 1] = array[position]  # Shift the element to the right
                position -= 1  # Move the pointer to the left
            array[position + 1] = key  # Insert the key into its correct position
            # Print current state of the list
            print("  Current state of the list:", array)
