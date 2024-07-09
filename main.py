from fastapi import FastAPI, HTTPException
from schema import Post
# crea un paquete unico
from uuid import uuid4

app = FastAPI()

# info to fill
posts_list = []


@app.get("/")
def read_root():
    return {"Hello": "World"}

""""
Getters
"""
# dame todos los posts
@app.get("/posts")
async def get_all_posts():
    return posts_list

@app.get("/posts/{post_id}")
async def get_post(post_id: str):
    print(post_id)
    for post in posts_list:
        if post["id"] == post_id:
            return post

    # raise an error in case of fail
    raise HTTPException(status_code=404, detail="Post not found")


""""
Posts
"""
@app.post("/posts")
async def save_post(post: Post):
    post.id = str(uuid4())
    posts_list.append(post.dict())
    return posts_list[-1]


"""
Delete 
"""
@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    for index, post in enumerate(posts_list):
        if post["id"] == post_id:
            # quita el elemento de la list
            posts_list.pop(index)
            return {"message": "Post deleted successfully"}

    # si no lo encontramos mostramos el siguiente mensaje
    raise HTTPException(status_code=404, detail="Post not found")


"""
Update
"""

@app.put("/posts/{post_id}")
async def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts_list):
        if post["id"] == post_id:
            posts_list[index]["title"] = updatePost.title
            posts_list[index]["author"] = updatePost.author
            posts_list[index]["content"] = updatePost.content
            return {"message": "Post update successfully"}

    raise HTTPException(status_code=404, detail="Post not found")







