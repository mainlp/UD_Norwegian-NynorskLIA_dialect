#!/bin/sh

echo "Getting LIA data"
wget -np -k -r http://tekstlab.uio.no/glossa/html/transcriptions/lia_norsk/
mv tekstlab.uio.no/glossa/html/transcriptions/lia_norsk lia_norsk
rm -r tekstlab.uio.no

echo "Creating CONLLU files with dialect info"
python3 add_phono.py
