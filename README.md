# gpt2-fastapi-hugingface
```pip install -r requirements.txt``` <br />
```run prepare_data.py to generate got.txt into chunked``` <br />
```run models.py to fine tuned our model into existing huggingface data```<br />
turn on the api by typing this<br />
```uvicorn main:app --reload```<br />

# hit api
to hit the api you can open postman/any other apps for api post you want<br />

```hit into localhost:8000/generate```<br />
```with this payload as json```<br />
```JSON 
{"prefix": "The young knight",
"max_length": 800,
"top_k": 5 }
```
