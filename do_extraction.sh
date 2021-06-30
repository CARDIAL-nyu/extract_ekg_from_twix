#!/bin/bash

docker run -it --rm --volume "$PWD":/files_to_process --user $(id -u):$(id -g) tsphan/mri_tools:ecg_from_twix
