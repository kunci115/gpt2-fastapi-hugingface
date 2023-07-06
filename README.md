# gpt2-fastapi-hugingface
```pip install -r requirements.txt```
```run prepare_data.py to generate got.txt into chunked```
```run models.py to fine tuned our model into existing huggingface data```
turn on the api by typing this
```uvicorn main:app --reload```

# hit api
to hit the api you can open postman/any other apps for api post you want

```hit into localhost:8000/generate```
```with this payload as json```
```{"prefix": "The young knight","max_length": 800,"top_k": 5 ```