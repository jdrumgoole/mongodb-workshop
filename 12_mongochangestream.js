
const yargs = require( 'yargs') ;

var MongoClient = require('mongodb').MongoClient

var uri = 'mongodb://localhost:27017/IOTDB';

var printTemp = function( doc ) {
    console.log( `Name : ${doc.name} ${doc.temp}` )
};

const argv = yargs.argv ;

if (argv.uri ) {
    uri = argv.uri ;
}

console.log( "Using uri: ", uri ) ;

MongoClient.connect(uri, function(err, client) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        console.log("Successfully connected to server: ", uri );
    }

    //console.log( db ) ;
    // Find some documents in our collection

    db = client.db( "IOTDB" ) ;
    changeStream = db.collection('sensor_data').watch() ;

    changeStream.on( "change", function( change ) {
        console.log( change ) ;
    } ) ;

    // Declare success
    console.log("changeStream");
});


