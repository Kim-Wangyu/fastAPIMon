from email.mime import image
from odmantic import AIOEngine, Model


class BookModel(Model):
    keyword:str
    publisher:str
    price: int
    image: str

    class Config:
        collection = "books"


#db (fastapi-pj)  --> collection(books)  -->document {
# keyword : 파이썬,publisher :ㅇㅇ출판사
# }