
var mongodb = require( "mongodb") ;

var mongoClient = mongodb.MongoClient ;

const url = "mongodb://localhost:27017" ;

mongoClient.connect( url, function( err, client ) {
    if ( err ) {
        console.log( "Failed to connect to :", url ) ;
        process.exit( 1 )
    } else {
        console.log( "Connected to:", url ) ;
    }

    const testDB = client.db( "test")  ;

    testDB.command( { "isMaster" : 1 }, function( err, res ) {
        if (err ) {
            console.log("isMaster error")
        } else {
            console.log(res);

        }
        client.close() ;
    });
    console.log( "mongoClient") ;

})

