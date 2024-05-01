class Selection:
    @staticmethod
    def selection_sort(array):
        array_length = len(array)  # Get the length of the array
        for index in range(array_length):  # Iterate through the array
            print("Iteration", index+1)
            min_index = index  # Assume the current element is the minimum
            for position in range(index+1, array_length):  # Iterate through the unsorted part of the array
                print("  Comparing elements at index", min_index, "and", position, ":", array[min_index], "and", array[position])
                if array[position] < array[min_index]:  # Find the minimum element in the unsorted part of the array
                    print("    Updating minimum index to", position)
                    min_index = position  # Update the index of the minimum element
            # Swap the found minimum element with the first element
            array[index], array[min_index] = array[min_index], array[index]
            # Print current state of the list
            print("  Current state of the list:", array)
