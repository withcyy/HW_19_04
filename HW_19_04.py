class NumberList:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if number not in self.numbers:
            self.numbers.append(number)
        else:
            print("This number already exists in the list.")

    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
            print("Number removed from the list.")
        else:
            print("Number not found in the list.")

    def show_list(self, reverse=False):
        if reverse:
            print("List in reverse order:")
            for number in reversed(self.numbers):
                print(number)
        else:
            print("List in normal order:")
            for number in self.numbers:
                print(number)

    def check_number(self, number):
        if number in self.numbers:
            print("Number exists in the list.")
        else:
            print("Number does not exist in the list.")

    def replace_number(self, old_number, new_number, replace_all=False):
        if old_number in self.numbers:
            if replace_all:
                index = 0
                while old_number in self.numbers[index:]:
                    index = self.numbers.index(old_number, index)
                    self.numbers[index] = new_number
                    index += 1
            else:
                index = self.numbers.index(old_number)
                self.numbers[index] = new_number
            print("Number replaced in the list.")
        else:
            print("Number not found in the list.")

def show_menu():
    print("1. Add a new number to the list")
    print("2. Remove all occurrences of a number from the list")
    print("3. Show the contents of the list (choose the order)")
    print("4. Check if a value is in the list")
    print("5. Replace values in the list")
    print("0. Exit")

    choice = input("Enter (1-0):")
    return choice

number_list = NumberList()

while True:
    choice = show_menu()

    if choice == '1':
        number = int(input("Enter the number to add: "))
        number_list.add_number(number)
    elif choice == '2':
        number = int(input("Enter the number to remove: "))
        number_list.remove_number(number)
    elif choice == '3':
        order_choice = input("Enter 'normal' or 'reverse': ")
        if order_choice.lower() == 'reverse':
            number_list.show_list(reverse=True)
        else:
            number_list.show_list()
    elif choice == '4':
        number = int(input("Enter the number to check: "))
        number_list.check_number(number)
    elif choice == '5':
        old_number = int(input("Enter the number to replace: "))
        new_number = int(input("Enter the new number: "))
        replace_all = input("Replace all occurrences? (yes/no): ").lower() == 'yes'
        number_list.replace_number(old_number, new_number, replace_all)
    elif choice == '0':
        print("end")
        break
    else:
        print("Error!!!")