from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# 1. Define your data structure properly
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# FIXED: Changed "tilte" to "title" to match your Pydantic schema
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like Irish Potatoes", "id": 2}
]

def find_post(id: int):
    for p in my_posts:
        if p['id'] == id:
            return p
    return None

# FIXED: Changed "return p" to "return i" so it actually returns the index
def find_index_post(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
    return None

@app.get("/")
def read_root():
    return {"message": "Hello Mr.DCT"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # NOTE: post.dict() is deprecated in Pydantic v2; use post.model_dump() if using newer versions
    post_dict = post.model_dump() if hasattr(post, "model_dump") else post.dict()
    post_dict['id'] = randrange(0, 100000)
    # FIXED: Changed square brackets [] to parentheses () for the append method
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    # FIXED: Added a check for if the post index doesn't exist to prevent a crash
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
