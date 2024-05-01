# Main.py
import Insertion  # Import the Bubble class from bubble.py

def main():
    array = [5, 3, 8, 1, 2]
    Insertion.Insertion.insertion_sort(array)
    print("Sorted array:", array)

if __name__ == "__main__":
    main()
