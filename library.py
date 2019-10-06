
class Library:

    def __init__(self, name, books):
        self.name = name
        self.book = books
        self.lended_book = {}

    def show_book(self):
        for books in self.book:
            print(books)

    def lend(self, user, book):
        if book not in self.lended_book.keys():
            if book not in self.book:
                print(f"Sorry we dont have {book} book:\n")
            else:
                print("Book is available ")
                self.lended_book.update({book:user})
                print("Database is updated ")
                self.book.remove(book)
        else:
            print("Enter the book present in library : ")

    def add(self, book):
        self.book.append(book)
        print("The book has been succesfully donated ")

    def returns(self, book):
        self.book.append(book)
        self.lended_book.pop(book)



if __name__ == "__main__":

    l1 = Library("Faraz Library",["Python", "C++", "Java", "Harry Potter"])
    while True:
        print("1: To display the book : ")
        print("2: To lend the book : ")
        print("3: To add the book to library : ")
        print("4: To return the book to library: ")
        try:
            n = int(input("Enter the following number to perform the task :"))
        except:
            print("wrong input")
            continue

        if n == 1:
            print("The books available are :")
            l1.show_book()

        elif n == 2:
            user = input("Enter the name of the user :")
            lends = input("Enter the book you want to lend :")
            l1.lend(user ,lends)

        elif n == 3:
            add_book = input("Enter the book you want to donate to library :")
            l1.add(add_book)

        elif n == 4:
            returns = input("Enter the book you want to return : ")
            l1.returns(returns)
        else:
            print("Give correct integer ")

        print("enter 'q' to quit : ")
        print("enter any button to continue: ")
        m = input()
        if m == 'q':
            print("Thanks for visiting our library :")
            quit()
        if m == 'c':
            continue


