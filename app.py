import sqlite3

# 1. DATABASE SETUP (Must be first)
connection = sqlite3.connect('notes.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
''')

# 2. DEFINE FUNCTIONS (The "Tools" for the menu)
def add_note(title, content):
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    connection.commit()
    print("\n✅ Note saved successfully!")

def show_notes():
    cursor.execute('SELECT * FROM notes')
    rows = cursor.fetchall()
    print("\n--- YOUR SAVED NOTES ---")
    if not rows:
        print("No notes found.")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]} | Content: {row[2]}")

# 3. THE MENU (Must be last so it can "see" the functions above it)
def main_menu():
    while True:
        print("\n--- NOTE MANAGER ---")
        print("1. Add a Note")
        print("2. View All Notes")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            title = input("Enter Title: ")
            content = input("Enter Content: ")
            add_note(title, content)
        
        elif choice == '2':
            show_notes()
        
        elif choice == '3':
            print("Closing database... Goodbye!")
            connection.close()
            break 
        
        else:
            print("❌ Invalid choice, try again.")

# 4. START THE APP
main_menu()