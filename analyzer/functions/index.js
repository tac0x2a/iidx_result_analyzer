const functions = require('firebase-functions');
const os = require('os');
const Busboy = require('busboy');

//{ "result": "success/failed", "body":{}}
exports.hello_world = functions.https.onRequest((req, res) => {
    console.info("hello_world is called.");

    if (req.method !== 'POST') {
        res.status(405).send('Method Not Allowed');
        return;
    }

    const busboy = new Busboy({ headers: req.headers });
    let uploads = {};

    // This callback will be invoked for each file uploaded.
    busboy.on('file', (fieldname, file, filename, encoding, mimetype) => {
        console.log(filename);
        console.log(fieldname);
        console.log(encoding);
        console.log(mimetype);
        uploads[filename] = { filename, mimetype };
        console.log('upload file: ' + filename + ' metadata: ' + mimetype);

        file.resume(); // ignore file contens
    });

    busboy.on('finish', () => {
        console.log('finish : ' + JSON.stringify(uploads));
        res.status(200).send('finish : ' + JSON.stringify(uploads));
    });

    busboy.end(req.rawBody);
});