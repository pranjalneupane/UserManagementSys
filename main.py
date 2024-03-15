import csv

class UserManagementSystem:
    def __init__(self, csv_filename='users.csv'):
        self.csv_filename = csv_filename
        self.fields = ['Name', 'Email', 'Age']
        self.users = []

    def save_users(self):
        with open(self.csv_filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.users)

    def load_users(self):
        try:
            with open(self.csv_filename, 'r') as file:
                reader = csv.DictReader(file)
                self.users = [row for row in reader]
        except FileNotFoundError:
            self.users = []

    def create_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        age = input("Enter user age: ")

        user = {
            'Name': name,
            'Email': email,
            'Age': age
        }

        self.users.append(user)
        print("User created successfully!")
        self.save_users()

    def list_users(self):
        print("\nList of Users:")
        for user in self.users:
            print(f"Name: {user['Name']}, Email: {user['Email']}, Age: {user['Age']}")
        print()

    def edit_user(self):
        self.list_users()
        try:
            user_index = int(input("Enter the index of the user you want to edit: ")) - 1
            if 0 <= user_index < len(self.users):
                name = input("Enter new name: ")
                email = input("Enter new email: ")
                age = input("Enter new age: ")

                self.users[user_index]['Name'] = name
                self.users[user_index]['Email'] = email
                self.users[user_index]['Age'] = age

                print("User information updated successfully!")
                self.save_users()
            else:
                print("Invalid user index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_user(self):
        self.list_users()
        try:
            user_index = int(input("Enter the index of the user you want to delete: ")) - 1
            if 0 <= user_index < len(self.users):
                del self.users[user_index]
                print("User deleted successfully!")
                self.save_users()
            else:
                print("Invalid user index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def run(self):
        self.load_users()

        while True:
            print("\nUser Management System Menu:")
            print("1. Create User")
            print("2. List Users")
            print("3. Edit User")
            print("4. Delete User")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.list_users()
            elif choice == '3':
                self.edit_user()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                print("Exiting User Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    user_management_system = UserManagementSystem()
    user_management_system.run()