import os
import typer
import numpy as np
import pandas as pd
import ismrmrd

app = typer.Typer()


@app.command()
def process_dir(path_to_files: str = typer.Argument('/files_to_process')):
    """Loops through all ISMRMRD .h5 files and extracts EKG waveforms into CSV files.

    Parameters
    ----------
    path_to_files : str
        Path to the folder containing all the *.h5 ISMRMRD files

    """
    for root, dirs, files in os.walk(path_to_files):
        for a_file in files:
            # Only process files that have the .h5 extension
            if a_file.lower().endswith('.h5'):
                _path_to_dat = os.path.join(root, a_file)
                typer.echo(_path_to_dat)
                try:
                    proc_file(_path_to_dat)
                except:
                    continue

@app.command()
def proc_file(path_to_file: str):
    """Processes a single ISMRMRD .h5 file to extract the EKG waveforms into CSV files.

    Parameters
    ----------
    path_to_file : str
        Path to the .h5 ISMRMRD file containing the raw scanner data


    """

    # Invalid/incorrect files should generally fail to open here
    try:
        f = ismrmrd.Dataset(path_to_file, '/dataset', False)
    except:
        typer.echo('\n\tFailed to open {_path_to_dat}!\n'.format(_path_to_dat=_path_to_dat))


    try:
        # Figure out the number of waveform objects and then iterate through to grab all waveform_id=0 (EKG)
        nwaveforms = f.number_of_waveforms()
        read_waveforms = [f.read_waveform(i) for i in range(0, nwaveforms) if f.read_waveform(i).waveform_id == 0]

        # List comprehension above puts them in an odd format. This re-arranges to fit nicely into pandas DataFrame.
        x1 = np.hstack((read_waveforms[0].data, read_waveforms[1].data))
        for a_stack in read_waveforms[2:]:
            x1 = np.hstack((x1, a_stack.data))

        # Siemens twix files have EKG recorded at sampling rate of 400 Hz. Create the time array:
        t1 = np.arange(0, x1.shape[1])/400.0
    except:
        typer.echo('\n\tFailed to read waveforms for {_path_to_dat}!\n'.format(_path_to_dat=_path_to_dat))

    try:
        # Use pandas to save a CSV file with the columns labeled appropriately
        path_to_output = path_to_file.replace('.h5', '_ECG.csv')
        pd.DataFrame(np.vstack((t1, x1)).T,
            columns=['time_sec', 'ch1', 'ch2', 'ch3', 'ch4', 'isTrigger_boolean']).to_csv(path_to_output, index=False)

    except:
        typer.echo('\n\tFailed to save CSV for {_path_to_dat}!\n'.format(_path_to_dat=_path_to_dat))


if __name__ == '__main__':
    app()
