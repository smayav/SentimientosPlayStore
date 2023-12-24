from fastapi import FastAPI, Request
from pydantic import BaseModel
from model import get_prediction

app = FastAPI()

class TextParameter(BaseModel):
    text: str

# @app.post('/predict')
# def predict(text_parameter: TextParameter):
#     text = text_parameter.text
#     return {
#         "message": get_prediction(text)
#     }
    
@app.post('/predict')
def predict(text_parameter: TextParameter):
    text = text_parameter.text
    result = get_prediction(text)
    return {
        "result": result
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

