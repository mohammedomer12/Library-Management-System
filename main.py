from library import Library
def main():
    print('Welcome to the Qatar National Library')
    library = Library('books.csv', 'members.csv')
    while True:

        print('1. Add Books')
        print('2. Remove Books')
        print('3. Search for Books')
        print('4. Display Books')
        print('5. Add Member')
        print('6. Remove Member')
        print('7. Search for Member')
        print('8. Display Members')
        print('9. Borrow Book')
        print('10. Return Book')
        print('11. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            year = input('Enter book year: ')
            pages = input('Enter book pages: ')
            library.add_book(title, author, year, pages)
        elif choice == '2':
            title = input('Enter book title: ')
            library.remove_book(title)
        elif choice == '3':
            title = input('Enter book title: ')
            library.search_book(title)
        elif choice == '4':
            library.view_books()
        elif choice == '5':
            name = input('Enter member name: ')
            member_id = input('Enter id of member: ')
            library.add_member(name, member_id)
        elif choice == '6':
            member_id = input('Enter member id: ')
            library.remove_member(member_id)
        elif choice == '7':
            keyword = input('Enter name/member_id: ')
            library.search_member(keyword)
        elif choice == '8':
            library.view_members()
        elif choice == '9':
            title = input('Enter book title: ')
            member_id = input('Enter id of member: ')
            library.borrowed(title, member_id)
        elif choice == '10':
            title = input('Enter book title: ')
            member_id = input('Enter id of member: ')
            library.return_book(member_id, title)
        elif choice == '11':
            print('Thank You')
            break
if __name__ == '__main__':
    main()