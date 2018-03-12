var MongoClient = require('mongodb').MongoClient ;

var uri = 'mongodb://localhost:27017/test';


MongoClient.connect( uri, function(err, client) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        console.log("Successfully connected to server: ", uri );
    }

    db = client.db( "test" ) ;
    db.collection('test').insertOne({ "hello" : "World!"}, function(err, res ) {

        if ( err ) {
            console.log( err ) ;
            process.exit( 1 )
        } else {
            console.log( `Inserted ${ res.insertedCount } document` ) ;
            console.log( `objectID : ${res.insertedId}`)
        }
        // Close the client
        client.close();
    });

    console.log("insertOne");
});


