#!/bin/bash

cd /files_to_process
for f in *.dat; do siemens_to_ismrmrd -f $f -o $f.h5 -Z ; done

python3 /project/extract_ekg_from_ismrmrd.py process-dir
