from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from livraria import auth, authors, books, categories, publishers

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(publishers.router)

authors.router.include_router(books.router, prefix="/{author_id}")
app.include_router(authors.router)
app.include_router(books.router)
