import csv
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}, pages: {self.pages}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def __str__(self):
        return f"name: {self.name}, id: {self.member_id}"

class Library:
    def __init__(self, book_file, members_file):
        self.book_file= book_file
        self.members_file= members_file
        self.books = []
        self.members = []
        self.load_books()
        self.load_members()

    def add_book(self, title , author , year , pages):
        book = Book(title, author, year , pages)
        self.books.append(book)
        self.save_books()
        print('Book added to the library')

    def save_books(self):
        with open(self.book_file , 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'author', 'year', 'pages'])
            for i in self.books:
                writer.writerow([i.title, i.author, i.year, i.pages])

    def load_books(self):
        try:
            with open(self.book_file , 'r', newline = '') as file:
                reader = csv.reader(file)
                try:
                    next(reader)
                except StopIteration:
                    return

                for row in reader:
                    self.books.append(Book(row[0], row[1], int(row[2]), int(row[3])))
        except FileNotFoundError:
            print(f'File {self.book_file} not found')

    def view_books(self):
        count = 0
        for i in self.books:
            count += 1
            print(i)
        print(f'There are {count} books')

    def search_book(self, keyword):
        found_book = []
        for i in self.books:
            if keyword.lower() in i.title.lower() or keyword.lower() in i.author.lower():
                found_book.append(i)
        if found_book:
            for book in found_book:
                print(book)
        else:
            print('No book found')

    def add_member(self, name , member_id):
        member = Member(name, member_id)
        self.members.append(member)
        self.save_members()

    def save_members(self):
        with open(self.members_file , 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'member_id'])
            for i in self.members:
                writer.writerow([i.name, i.member_id])

    def view_members(self):
        count = 0
        for i in self.members:
            count += 1
            print(i.name)
        print(f'There are {count} members')

    def search_member(self, keyword):
        found = [member for member in self.members if keyword.lower() in member.name.lower() or keyword.lower() in member.member_id.lower()]
        if found:
            for i in found:
                print(i.name)
        else:
            print('No member found')

    def load_members(self):
        try:
            with open(self.members_file , 'r', newline = '') as file:
                reader = csv.reader(file)
                try:
                    next(reader)
                except StopIteration:
                    return
                for row in reader:
                    self.members.append(Member(row[0], row[1]))
        except FileNotFoundError:
            print(f'File {self.members_file} not found')

    def remove_book(self, title):
        for i in self.books:
            if i.title == title:
                self.books.remove(i)
                self.save_books()
                print('Book removed')
                return
        print('No book found with that title {}'.format(title))

    def remove_member(self, member_id):
        for i in self.members:
            if i.member_id == member_id:
                self.members.remove(i)
                self.save_members()
                print('Member removed')
                return
        print('No member found with that id {}'.format(member_id))

    def borrowed(self, title , member_id):
        for i in self.books:
            if i.title.lower() == title.lower():
                for j in self.members:
                    if j.member_id == member_id:
                        j.borrowed_books.append(i)
                        self.books.remove(i)
                        self.save_books()
                        print(f'Borrowed {i.title} by member {member_id}')
                        return
                print(f'member with id {member_id} has not been found in the library')
        print(f'book {title} is not there in the library' )

    def return_book(self, member_id , title):
        for i in self.members:
            if i.member_id == member_id:
                for j in i.borrowed_books:
                    if j.title.lower() == title.lower():
                        i.borrowed_books.remove(j)
                        self.books.append(j)
                        self.save_books()
                        print(f'Borrowed {j.title} has been returned by member {member_id}')
                        return
                print(f'the book : {title} has not been found in the borrowed books')
        print(f'Wrong member id: {member_id}, Retry !!')


