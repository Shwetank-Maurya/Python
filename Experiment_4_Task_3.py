# ---- BINARY FILE OPERATIONS ----
import pickle

try:
    student_data = {"name": "Alice", "age": 20, "grade": "A"}

    # Writing to a binary file
    with open("student_data.bin", "wb") as file:
        pickle.dump(student_data, file)
    print("Binary data written successfully to student_data.bin")

    # Reading from the binary file
    with open("student_data.bin", "rb") as file:
        loaded_data = pickle.load(file)
        print("\n--- Binary File Content ---")
        print(loaded_data)

except (FileNotFoundError, IOError) as e:
    print(f"File error: {e}")
except pickle.UnpicklingError:
    print("Error: Could not unpickle the data.")
