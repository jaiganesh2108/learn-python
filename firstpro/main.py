from day2.db import collection
from bson.objectid import ObjectId

# CREATE
def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))

    user = {
        "name": name,
        "email": email,
        "age": age
    }

    result = collection.insert_one(user)
    print(f"✅ User created with ID: {result.inserted_id}")


# READ
def read_users():
    users = collection.find()
    print("\n📄 All Users:")
    for user in users:
        print(f"""
ID: {user['_id']}
Name: {user['name']}
Email: {user['email']}
Age: {user['age']}
------------------------
""")


# UPDATE
def update_user():
    user_id = input("Enter user ID to update: ")
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))

    result = collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"name": name, "age": age}}
    )

    if result.matched_count:
        print("✏️ User updated successfully")
    else:
        print("❌ User not found")


# DELETE
def delete_user():
    user_id = input("Enter user ID to delete: ")

    result = collection.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.deleted_count:
        print("🗑️ User deleted successfully")
    else:
        print("❌ User not found")


# MENU
def menu():
    while True:
        print("""
========================
1. Create User
2. Read Users
3. Update User
4. Delete User
5. Exit
========================
""")

        choice = input("Choose option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()