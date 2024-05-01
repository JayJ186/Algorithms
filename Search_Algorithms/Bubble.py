class Bubble:
    @staticmethod
    def bubble_sort(array):
        array_length = len(array)  # Get the length of the array
        for index in range(array_length):  # Iterate through the array
            print("Iteration", index+1)
            for position in range(0, array_length-index-1):  # Iterate through unsorted part of the array
                print("  Comparing elements at position", position, "and", position+1, ":", array[position], "and", array[position+1])
                if array[position] > array[position+1]:  # Check if adjacent elements are in the wrong order
                    print("    Swapping", array[position], "and", array[position+1])
                    # Swapping elements
                    array[position], array[position+1] = array[position+1], array[position]
                    # Print current state of the list
                    print("Current state of the list:", array)
