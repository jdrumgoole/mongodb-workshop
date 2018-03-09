var MongoClient = require('mongodb').MongoClient

var url = 'mongodb://localhost:27017/test';

var manyDocs = [
    { a : 1 },
    { b : 2 },
    { c : 3 },
    { d : 4 },
    { e : 5 },
    { f : 6 },
];

MongoClient.connect(url, function(err, client) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        console.log("Successfully connected to server: ", url );
    }

    //console.log( db ) ;
    // Find some documents in our collection

    db = client.db( "test" ) ;
    db.collection('test').insertMany( manyDocs, (err, res ) => {
        if (err) {
            throw err ;
        } else {
            console.log(`Inserted ${res.insertedCount} doc(s)` );
        }
    }) ;

    // Close the client
    client.close();

    // Declare success
    console.log("Called insertMany()");
});


