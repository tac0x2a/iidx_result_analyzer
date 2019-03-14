const functions = require('firebase-functions');
const os = require('os');
const fs = require('fs');
const path = require('path');
const Busboy = require('busboy');

// Imports the Google Cloud client libraries
const vision = require('@google-cloud/vision');
// Creates a client
const client = new vision.ImageAnnotatorClient();

//{ "result": "success/failed", "body":{}}
exports.hello_world = functions.https.onRequest((req, res) => {
    console.info("hello_world is called.");

    if (req.method !== 'POST') {
        res.status(405).send('Method Not Allowed');
        return;
    }

    const busboy = new Busboy({ headers: req.headers });
    let uploadedFile = "";

    // This callback will be invoked for each file uploaded.
    busboy.on('file', (fieldname, file, filename, encoding, mimetype) => {
        console.log(filename);
        console.log(fieldname);
        console.log(encoding);
        console.log(mimetype);
        console.log('upload file: ' + filename + ' metadata: ' + mimetype);

        const tmpdir = os.tmpdir();
        const filepath = path.join(tmpdir, filename)

        uploadedFile = filepath;

        file.pipe(fs.createWriteStream(filepath));
    });

    busboy.on('finish', () => {
        console.log('finish : ' + uploadedFile);

        client
            .textDetection(uploadedFile)
            .then(results => {
                const detections = results[0].textAnnotations;

                detections.forEach(text => console.log(text));

                res.status(200).send(JSON.stringify(detections));

                fs.unlinkSync(uploadedFile);
                return;
            })
            .catch(err => {
                console.error('ERROR:', err);
                res.status(405).send('Failed : ' + err);

                fs.unlinkSync(uploadedFile);
            });
    });

    busboy.end(req.rawBody);
});