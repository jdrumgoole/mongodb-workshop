var MongoClient = require('mongodb').MongoClient;

var url = 'mongodb://localhost:27017/test';

MongoClient.connect(url, function(err, client) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        console.log("Successfully connected to server: ", url );
    }


    db = client.db( "test" ) ;
    db.collection('test').deleteMany({ "hello" : "World!"}, function(err, res ) {

        if ( err ) {
            console.log( err ) ;
            process.exit( 1 )
        } else {
            console.log( `deleted ${ res.deletedCount } document(s)` ) ;;
        }
        // Close the client
        client.close();
    });

    console.log("deleteMany");
});


