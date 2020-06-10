#!/usr/bin/env bash

source $BIN_DIR/utils

echo "-----> Starting corpora installation"

# Assumes NLTK_DATA environment variable is already set
# $ heroku config:set NLTK_DATA='/app/nltk_data'

# Install the default corpora to NLTK_DATA directory
python -m textblob.download_corpora

# Open the NLTK_DATA directory
cd ${NLTK_DATA}

# Delete all of the zip files in the NLTK DATA directory
find . -name "*.zip" -type f -delete

echo "-----> Finished corpora installation"