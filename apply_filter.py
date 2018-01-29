import numpy as np
from scipy import signal
from scipy.io import wavfile

from load import load_filter

def filter_wavfile(wavpath, outwavpath, lfilter_path, rfilter_path):
    """Apply sensimetrics filters to a WAV file, saving out a filtered version.
    
    Parameters
    ----------
    wavpath : str
        Path to WAV file you want to filter. Must have 44100 Hz sampling rate.
    
    outwavpath : str
        Path where filtered WAV file will be saved. Output will always be stereo,
        44100 Hz, and 32-bit int.
    
    lfilter_path : str
        Path to .bin file containing filter for the left channel, supplied by Sensimetrics.
    
    rfilter_path : str
        Path to .bin file containing filter for the right channel.
    """
    # load wav file
    wav_fs, wavdata = wavfile.read(wavpath)
    
    # check that fs is 44100
    if not wav_fs == 44100:
        raise ValueError('WAV file must be sampled at 44100 Hz to apply filter, exiting')
    
    # check if wav data is mono or stereo
    is_mono = len(wavdata.shape) == 1
    
    # if mono, duplicate the mono channel to left and right
    if is_mono:
        lwav, rwav = wavdata, wavdata
    else:
        lwav, rwav = wavdata.T
    
    # load the filters
    lfilt, _ = load_filter(lfilter_path)
    rfilt, _ = load_filter(rfilter_path)
    
    # filter the two channels
    #if wavdata.dtype == np.int32:
    #    NORM = 2147483647
    #else:
    #    NORM = 1.0
    NORM = np.iinfo(wavdata.dtype).max
    NORM32 = 2147483647
    
    lwav_filt = signal.convolve(lwav.astype(float) / NORM, lfilt, 'same') * NORM32
    rwav_filt = signal.convolve(rwav.astype(float) / NORM, rfilt, 'same') * NORM32
    
    # write the result
    wavdata_filt = np.vstack([lwav_filt, rwav_filt]).T.astype(np.int32)
    wavfile.write(outwavpath, 44100, wavdata_filt)
