""" 1.Write a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name ,Author.
That class contains one class variable as NoOfBooks which is initialies to 0.
There is one instance methods of class as Display which displays name , Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
    After creating the class create the two objects of BookStore class as
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()  # Linux System Programming by Robert Love. No of books : 1
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # C Programming by Dennis Ritchie. No of books : 2  """

NoOfBooks = 0


class BookStore:

    def __init__(self, Val1, Val2):
        global NoOfBooks
        NoOfBooks += 1
        self.Name = Val1
        self.Author = Val2

    def Display(self):
        print('{0} by {1}. No Of Books : {2}'.format(self.Name, self.Author, NoOfBooks))


def main():
    Book_Name = input('Enter the Name Of Book : ')
    Author_Name = input('Enter the Name Of Author : ')

    obj1 = BookStore(Book_Name, Author_Name)
    obj1.Display()

    Book_Name = input('Enter the Name Of Book : ')
    Author_Name = input('Enter the Name Of Author : ')

    obj2 = BookStore(Book_Name, Author_Name)
    obj2.Display()


if __name__ == "__main__":
    main()
