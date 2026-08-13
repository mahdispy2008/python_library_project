class Library:
    def __init__(self):
        self.books = []


    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        print(f"book {title} added successfully.")

                    
    def remove_book(self, title):  
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book) 
                print(f"book {title} removed successfully")
                return
        print(f"book'{title}' not found.") 


    def search_book(self,title):
        for book in self.books:
            if book["title"] == title:
                print("found the book")
                print("title:", book["title"])
                print("author:", book["author"])
                return book
        print(f"book'{title}' not found.")        
        return None
        
        
    def show_books(self):
        if not self.books:
            print("the library is empty.")            
        else:
            print("---The Library Books---")                
            for book in self.books:
                print(f"Title:{book['title']}, Author:{book['author']}")