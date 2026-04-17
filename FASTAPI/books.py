from fastapi import Body, FastAPI
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category':'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category':'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category':'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category':'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category':'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category':'math'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'My favourite book!'}

# # path parameter
# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {'dynamic_param' : dynamic_param}

# @app.get("/books/{book_title}")
# async def read_book(book_title: str):
#     for book in BOOKS:
#         if book.gets('title').casefold() == book.title.casefold():
#             return book

# @app.get("/books/")
# async def read_category_by_query(category:str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)

#     return books_to_return




# # query paramter
# @app.get("/books/{book_author}/")  # dynamic parameter
# async def read_author_category_by_query(book_author: str, category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == book_author.casefold() and \
#                 book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)

#     return books_to_return


# post http request method
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book) 


# put http request method
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# Delete  http request method
@app.delete("/books/delete_book")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# To create a new API Endpoint that can fetch all the books from a specific author using either Path parameter or Query Parameters.
# using Query parameter - we are passing it as a query with author name as /books/author/?author_name == Author 
@app.get("/books/author")
async def books_fetch_path(author_name: str):
    books_to_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author_name.casefold():
            books_to_return.append(BOOKS[i])
    return books_to_return

 
# Using Path parameter - as in this we are directly passing it to the url the value so its is the path parameter
@app.get("/books/{author}")
async def books_fetch(author: str):
    books_to_return = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author.casefold():
            books_to_return.append(BOOKS[i])
    return books_to_return

