import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        "src.api.app:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )