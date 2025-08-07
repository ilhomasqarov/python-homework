import json

def read_students():
    try:
        with open('students.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
        for s in students:
            print(f"Name: {s.get('name')}, Age: {s.get('age')}, Major: {s.get('major')}")
    except FileNotFoundError:
        print("students.json file not found.")



def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4)

def add_book(books):
    title = input("Book title: ")
    author = input("Author: ")
    year = input("Year: ")
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Book added.")

def update_book(books):
    title = input("Title of the book to update: ")
    for book in books:
        if book['title'].lower() == title.lower():
            book['author'] = input("New author: ")
            book['year'] = input("New year: ")
            save_books(books)
            print("Book updated.")
            return
    print("Book not found.")

def delete_book(books):
    title = input("Title of the book to delete: ")
    new_books = [b for b in books if b['title'].lower() != title.lower()]
    if len(new_books) == len(books):
        print("Book not found.")
    else:
        save_books(new_books)
        print("Book deleted.")
    return new_books

def list_books(books):
    if not books:
        print("No books found.")
        return
    for b in books:
        print(f"{b['title']} by {b['author']} ({b['year']})")

def main():
    books = load_books()

    while True:
        print("\nChoose an option:")
        print("1. Show student details")
        print("2. Get Tashkent weather")
        print("3. Manage books")
        print("4. Recommend a movie by genre")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            read_students()
        elif choice == '2':
            get_weather()
        elif choice == '3':
            while True:
                print("\nBooks options: add, update, delete, list, back")
                cmd = input("Enter command: ").lower()
                if cmd == 'add':
                    add_book(books)
                elif cmd == 'update':
                    update_book(books)
                elif cmd == 'delete':
                    books = delete_book(books)
                elif cmd == 'list':
                    list_books(books)
                elif cmd == 'back':
                    break
                else:
                    print("Invalid command.")
        elif choice == '4':
            recommend_movie()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

