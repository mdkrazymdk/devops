#!/bin/bash

export $(grep -v '^#' .env | xargs)

echo "Waiting for DB..."
sleep 5

echo "Initializing Database..."
docker compose exec -T db psql -U $POSTGRES_USER -d $POSTGRES_DB -f /sql_scripts/init.sql

echo "Done!"
