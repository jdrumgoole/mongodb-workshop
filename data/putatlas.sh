#!/usr/bin/env bash
mongoimport --uri 'mongodb+srv://santander:bancobanco@bancosantanderworkshop-ffp4c.mongodb.net/MUGS' --collection mug_members --drop --file mug_members.json