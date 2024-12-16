from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def read_root(hello: str = Header(None)):
    if hello and hello.strip().lower() == "kitware":
        return "KTLbqCUse"
    elif not hello:
        return "hello header not set"
    else:
        return "hello header not set to kitware"
