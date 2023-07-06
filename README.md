# gpt2-fastapi-hugingface
This is an example how to do fine tuning with your own datasets from huggingface gpt2 models

# Installation
1. ```git clone this repository```
2. ```pip install -r requirements.txt``` <br />
3. FYI Huggingface only allowing 1024byte of data on every training, so we should chunk our data <br/>
```run prepare_data.py to generate got.txt into chunked``` <br />

4. ```run models.py to fine tuned our model into existing huggingface data```<br />
Turn on the api by typing this<br />
5. ```uvicorn main:app --reload```<br />

# Hit api
To hit the api you can open postman/any other apps for api post you want<br />

```hit into localhost:8000/generate```<br />
```with this payload as json```<br />
```JSON 
{"prefix": "The young knight",
"max_length": 800,
"top_k": 5 }
```
