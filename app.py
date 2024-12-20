from fastapi import FastAPI, Header
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def read_root(hello: str = Header(None)) -> str:
    if hello and hello.strip().lower() == "kitware":
        return "beep-boop-greetings-human"
    elif not hello:
        return "hello header not set"
    else:
        return "hello header not set to Kitware (case insensitive)"
