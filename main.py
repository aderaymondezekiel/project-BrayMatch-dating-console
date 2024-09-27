# Import the UUID library to generate unique user IDs
import uuid

class User:
    def __init__(self, name, age, gender, interests):
        # Initialize a new user with a unique ID and given attributes
        self.user_id = uuid.uuid4()  # Generate a unique user ID
        self.name = name  # User's name
        self.age = age  # User's age
        self.gender = gender  # User's gender
        self.interests = interests  # List of user's interests

    def update_profile(self, name=None, age=None, gender=None, interests=None):
        # Update the user's profile information with new values if provided
        if name: 
            self.name = name  # Update name if provided
        if age: 
            self.age = age  # Update age if provided
        if gender: 
            self.gender = gender  # Update gender if provided
        if interests: 
            self.interests = interests  # Update interests if provided

    def view_profile(self):
        # Return the user's profile information as a dictionary
        return {
            'user_id': str(self.user_id),  # Convert UUID to string for display
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'interests': self.interests,
        }

class Admin:
    def __init__(self):
        # Initialize the Admin with an empty list to store users
        self.users = []

    def create_user(self, name, age, gender, interests):
        # Create a new user and add them to the users list
        user = User(name, age, gender, interests)  # Instantiate a new User object
        self.users.append(user)  # Add the new user to the list of users
        print(f"User {name} created successfully with ID: {user.user_id}")  # Confirm user creation

    def update_user(self, user_id, name=None, age=None, gender=None, interests=None):
        # Update an existing user's profile if they are found by ID
        user = self.find_user(user_id)  # Find the user by their ID
        if user:
            user.update_profile(name, age, gender, interests)  # Update user profile with new data
            print(f"User {user_id} updated successfully.")  # Confirm user update
        else:
            print(f"User {user_id} not found.")  # Inform if user is not found

    def delete_user(self, user_id):
        # Delete a user from the list if they are found by ID
        user = self.find_user(user_id)  # Find the user by their ID
        if user:
            self.users.remove(user)  # Remove the user from the list
            print(f"User {user_id} deleted successfully.")  # Confirm user deletion
        else:
            print(f"User {user_id} not found.")  # Inform if user is not found

    def view_all_users(self):
        # Print the profiles of all users in the list
        if self.users:
            for user in self.users:
                print(user.view_profile())  # Display each user's profile
        else:
            print("No users found.")  # Inform if no users exist

    def match_profiles(self):
        # Find and display matches between users based on shared interests
        matches = MatchAlgorithm.match(self.users)  # Use the MatchAlgorithm to find matches
        if matches:
            for match in matches:
                print(f"Match: {match[0]['name']} and {match[1]['name']}")  # Display each match
        else:
            print("No matches found.")  # Inform if no matches are found

    def find_user(self, user_id):
        # Search for a user by their user ID and return the user object if found
        for user in self.users:
            if str(user.user_id) == user_id:  # Compare user ID as string
                return user  # Return the user object if found
        return None  # Return None if user is not found

class MatchAlgorithm:
    @staticmethod
    def match(users):
        # Match users based on shared interests and return a list of matched pairs
        matches = []
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                if MatchAlgorithm.are_compatible(users[i], users[j]):  # Check compatibility
                    matches.append((users[i].view_profile(), users[j].view_profile()))  # Add to matches
        return matches  # Return the list of matched pairs

    @staticmethod
    def are_compatible(user1, user2):
        # Determine if two users are compatible by checking for shared interests
        for interest in user1.interests:
            if interest in user2.interests:  # Check if any interest matches
                return True  # Return True if a match is found
        return False  # Return False if no matches are found

def main():
    admin = Admin()  # Create an instance of the Admin class
    while True:
        # Display the main menu for the BrayMatch Dating Console
        print("\nWelcome to BrayMatch Dating Console")
        print("Please choose from the menu below:")
        print("1. Create User")
        print("2. View All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Find User")
        print("6. View Match Profiles")
        print("7. Exit")

        choice = input("Enter your choice: ")  # Get user input for menu choice
        if choice == '1':
            # Collect user information and create a new user
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            interests = input("Enter interests (comma separated): ").split(',')
            admin.create_user(name, age, gender, interests)  # Create a new user
        elif choice == '2':
            # View all user profiles
            admin.view_all_users()
        elif choice == '3':
            # Update a user's profile by their user ID
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            gender = input("Enter new gender (leave blank to skip): ")
            interests = input("Enter new interests (leave blank to skip): ").split(',')
            admin.update_user(user_id, name, age, gender, interests)  # Update the user's profile
        elif choice == '4':
            # Delete a user by their user ID
            user_id = input("Enter user ID to delete: ")
            admin.delete_user(user_id)
        elif choice == '5':
            # Find and display a user's profile by their user ID
            user_id = input("Enter user ID to find: ")
            user = admin.find_user(user_id)
            if user:
                print("User found:")
                print(user.view_profile())
            else:
                print(f"User with ID {user_id} not found.")
        elif choice == '6':
            # View matched profiles based on interests
            admin.match_profiles()
        elif choice == '7':
            # Exit the BrayMatch Dating Console
            print("Exiting BrayMatch Dating Console. Thank you for using BrayMatch dating Console. Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
