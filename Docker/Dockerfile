FROM cardialnyu/twix_to_ismrmrd

LABEL maintainer="Timothy S. Phan <timothy.s.phan@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install --no-install-recommends python3 python3-pip python3-numpy python3-pandas -y && \
	python3 -m pip install ismrmrd typer && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY extract_ekg_from_ismrmrd.py /project
COPY extract_ekg_from_twix.sh /project

RUN chmod +x extract_ekg_from_twix.sh && chmod +x extract_ekg_from_ismrmrd.py

WORKDIR /project

ENTRYPOINT ["/project/extract_ekg_from_twix.sh"]

# docker run -it --rm --volume "$PWD":/files_to_process --user $(id -u):$(id -g) tsphan/mri_tools:ecg_from_twix
