#!/bin/sh
/usr/local/m/versions/3.6.3/bin/mongoimport  --db MUGS --collection mug_members --drop --file mug_members.json
