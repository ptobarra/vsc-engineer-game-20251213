import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# We are going to create a simple Python script that prints "Hello, World!" to the console.
def main():
    name = input("What is your name? ")

    while True:
        age_input = input("What is your age? ")
        try:
            age = int(age_input)
        except ValueError:
            print("Please enter your age as a whole number.")
            continue

        if age <= 0 or age > 120:
            print("Please enter an age between 1 and 120.")
            continue

        break

    print("\nHello, World!")
    print(f"Hello {name}!")
    print(f"You are {age} years old!\n")


if __name__ == "__main__":
    clear_screen()
    main()
