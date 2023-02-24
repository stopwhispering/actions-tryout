from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




if __name__ == "__main__":
    import uvicorn

    if __name__ == "__main__":
        uvicorn.run(
            "actions.main:app",
            host="localhost",
            port=5000,
            # reload=True
        )
