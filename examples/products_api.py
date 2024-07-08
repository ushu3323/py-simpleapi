from simpleapi import Router, Response, start_server
PORT = 3000

class PostRepository:
    posts = [
        dict(title="My first post", author="John doe"),
        dict(title="My second post", author="")
    ]

    @classmethod
    def get(cls):
        return cls.posts

    @classmethod
    def create(cls, title: str, author: str):
        cls.posts.append(dict(title, author))

router = Router()

@router.get("/")
def hello(res: Response):
    res.set_status(200)
    res.set_text("Hello world!")

@router.get("/posts")
def get_posts(res: Response):
    res.set_status(200)
    posts = PostRepository.get()
    res.set_json(posts)

@router.post("/posts")
def create_post(ctx: Response):
    ctx.send_response(201)
    ctx.send_header()


start_server(PORT, router)