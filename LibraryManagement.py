class Library():
    def __init__(self,list_of_books,Library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
            else:
                print(f"Sorry, This book is lend by {self.lend_data[book]}")
        else:
            print("please enter correct Name, Note: Names are case sensitive")

    def return_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("We already have this book, no need to return")
        else:
            print("please enter correct Name, Note: Names are case sensitive")

    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

def main():
    #Default variables
    list_books = ['Harry Potter','Sherlock Holmes','A week with gandhi','War and peace', 'shadow of ladakh']
    Library_name = 'Dhruvin'
    secret_key = 1234

    Dhruvin = Library(list_books,Library_name)

    print(f"Welcome To {Dhruvin.library_name} library\n'q' for exit,\n'd' for Display Book,\n'l' for lend book,\n'r' for Return Book \n'a' for Add Book,\n'del' for Delete Book\n ")

    Exit = False
    while (Exit is not True):
        _input = input(">>")
        
        if _input == "q":
            Exit = True

        elif _input == "d":
            Dhruvin.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("**Book Lended**\n")
            Dhruvin.lend_book(_input3,_input2)

        elif _input == "a":
            _input2 = input("Book name:")
            Dhruvin.add_book(_input2)
            print("**Added**")

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Which Book you want to delete?:")
                if(_input2 in list_books):
                    Dhruvin.delete_book(_input2)
                    print("**Deleted**")
                else:
                    print("We don't have this book to delete")
            else:
                print("Incorrect key")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Dhruvin.return_book(_input3,_input2)

        else:
            print("please enter correct option, try again!")

# if __name__ == "__main__":
main()