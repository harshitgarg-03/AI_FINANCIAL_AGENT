# def main():
#     print("Hello from ai-financial-agent!")


# if __name__ == "__main__":
#     main()


from fastapi import FastAPI

app = FastAPI();
@app.get("/")
def Home():
    return {"message": "AI Financial Advisor "}