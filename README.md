# IIDX Result Analyzer powered by Google Cloud Vision API

## Deploy

```sh
# gcloud
gcloud beta functions deploy hello_world --trigger-http --runtime=python37
```

## Memo
```
# firebase

cd analyze
firebase init functions
firebase deploy --only functions

# Function URL (hello_world): https://<host>/hello_world

curl 'https://<host>/hello_world?text=hi!'
# Hello,World with : hi!

firebase functions:delete hello_world

npm install --save multer

firebase functions:log

curl -X POST -F hoge=@sample.jpg  https://<host>/hello_world
finish : {"sample.jpg":{"filename":"sample.jpg","mimetype":"image/jpeg"}}
```