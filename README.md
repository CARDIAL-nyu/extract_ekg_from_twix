# `extract_ekg_from_twix`

This tool will extract EKG waveforms from all Siemens twix files in the current directory and save them as comma-separated-value formatted files.

## Quickstart

1. Clone this repository:
	```bash
		git clone https://github.com/CARDIAL-nyu/extract_ekg_from_twix.git
	```

2. Change into the directory that you just cloned and copy all your `*.dat` twix files into here:
	```bash
		cd extract_ekg_from_twix
	```

3. Run the `do_extraction.sh` script:
	```bash
		./do_extraction.sh
	```

Once the process is completed, all your *.dat files will have corresponding `.h5` and `_ECG.csv` files.

The `.h5` files are the twix files converted to the vendor-agnostic ISMRMRD format.

The `_ECG.csv` files are the 4 channels of EKG data.
