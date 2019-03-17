# IIDX Result Analyzer powered by Google Cloud Vision API

## Deploy
```sh
firebase deploy
``

## Memo
```sh
# Setup
sudo apt install nodejs npm # for ubuntu
sudo npm install -g firebase-tools


# firebase functions
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

npm install --save @google-cloud/vision
curl -X POST -F hoge=@sample2.jpg  https://<host>/hello_world

firebase init hosting
firebase deploy --only hosting
https://<project-name>.firebaseapp.com/
```