import uvicorn

if __name__=="__main__":
    uvicorn.run('app.main:app',host="localhost",port=8000, reload=True)

    #간단하게 유비콘 실행하기