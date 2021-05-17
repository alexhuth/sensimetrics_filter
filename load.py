import numpy as np

def load_filter(fpath):
    """Function to load sensimetrics filter from .bin file. To match the MATLAB
    function this also returns a hard-coded sampling rate of 44100.
    
    Parameters
    ----------
    fpath : str
        Path to the .bin file that you want to load.
    
    Returns
    -------
    filt : ndarray
        The filter as an impulse response function.
    
    fs : int = 44100
        Sampling rate in Hz, hard-coded to 44100.
    """
    with open(fpath, 'rb') as f:
        filt = np.frombuffer(f.read(), dtype=np.float)
    
    return filt, 44100
