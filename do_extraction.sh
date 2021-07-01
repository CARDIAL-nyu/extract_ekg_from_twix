#!/bin/bash

docker run -it --rm --volume "$PWD":/files_to_process --user $(id -u):$(id -g) cardialnyu/ekg_from_twix
