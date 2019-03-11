# IIDX Result Analyzer powered by Google Cloud Vision API

## Deploy

```sh
gcloud beta functions deploy hello_world --trigger-http --runtime=python37
```

## Memo
```
cd analyze
firebase init functions
firebase deploy --only functions

# Function URL (hello_world): https://<host>/hello_world

curl 'https://<host>/hello_world?text=hi!'
# Hello,World with : hi!

firebase functions:delete hello_world

```