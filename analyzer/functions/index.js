const functions = require('firebase-functions');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });


exports.hello_world = functions.https.onRequest((req, res) => {
    const original = req.query.text;
    res.send("Hello,World with : " + original);
})