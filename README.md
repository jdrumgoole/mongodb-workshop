# mongdb-workshop

This repo contains working example for a Node.js based introductory
workshop for MongoDB. There is a basic set of CRUD examples and
a Change Stream example.

Users are expected to have Node.js, NPM and Python installed to run
all the programs. Users may find the mtools package useful for running
replica sets locally. 

## dependencies

Install [Node.js](https://nodejs.org/en/) (this code has been tested
witb Node 9.9.0).

Install the
[MongoDB Node.js Driver](https://mongodb.github.io/node-mongodb-native/).
`
JD10Gen:mongodb-workshop jdrumgoole$ npm install mongodb
+ mongodb@3.0.4
added 6 packages from 4 contributors in 2.52s
JD10Gen:mongodb-workshop jdrumgoole$
`


Install (Python[https://www.python.org/downloads/] (this code has been tested with python 2.7)

Install [Mtools](https://github.com/rueckstiess/mtools). If you have
installed python you can install mtools by using the Python package
installer. 

`
JD10Gen:~ jdrumgoole$ pip install mtools
Collecting mtools
  Downloading mtools-1.3.2-py2-none-any.whl (853kB)
    100% |████████████████████████████████| 860kB 1.5MB/s
Installing collected packages: mtools
Successfully installed mtools-1.3.2
JD10Gen:~ jdrumgoole$
`

## Data

Repo for MongoDB Workshop code and data.

Please run *data/putgroups.sh* to load the test data prior to running
the other node.js scripts. This will create a **MUGS** database and a
**mug_groups** collection.

Many of the scripts in the workshop expect the **MUGS** database and
**mug_groups** collection to exist.

## Scripts

`01_mongoclient.js` : Basic client that connects to a MongoDB Server
`02_mongofindone.js` : Simple query returning a single document.
`03_mongofindmany.js` : Query that returns several documents using a cursor
`04_mongoinsertone.js` : Inserting a single document
`05_mongoinsertmany.js` : Inserting mutiple documents
`06_mongoupdateone.js` : Update a document in place
`07_mongoupdatemany.js` : Update several documents in place
`08_mongodeletelone.js` : Delete a single document
`09_mongodeletemany.js` : Delete multiple documents
`10_mongocreateindex.js` : Create a (btree) index on a collection
`11_mongoindexinformation.js`: Get information about indexes
`12_mongodropindex.js` : Remove an index
`13_mongoaggregate.js` : Use the MongoDB aggregation framework
`14_send_data.py` : Python program to create multiple clients for the
change stream.
`15_mongochangestream.js`: Node.js client to respond to change stream events
`atlas_changestream.sh` : Start a Node.js client for an Atlas database
`send_data_to_atlas.sh` : Write data to a MongoDB Atlas database.

## Connecting to Atlas
See [my blog post](https://blog.joedrumgoole.com/2018/03/22/connecting-to-mongodb-atlas/) for more details on connecting to Atlas databases. 
