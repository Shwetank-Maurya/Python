# ---- CSV FILE OPERATIONS ----
import csv

try:
    # Writing data to a CSV file
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade"])
        writer.writerow(["Alice", 20, "A"])
        writer.writerow(["Bob", 22, "B"])
        writer.writerow(["Charlie", 19, "A"])
    print("Data written successfully to students.csv")

    # Reading data from the CSV file
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        print("\n--- CSV File Content ---")
        for row in reader:
            print(row)

except Exception as e:
    print(f"An error occurred: {e}")
