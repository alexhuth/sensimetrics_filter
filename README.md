# sensimetrics_filter
code for filtering WAV files using filters supplied by Sensimetrics.

`load.py` contains the function `load_filter()`, which reproduces exactly the output from the `load_filter` MATLAB function supplied by Sensimetrics.

`apply_filter.py` contains the function `filter_wavfile()`, which applies filters to a WAV file and saves the result.

NB: results have not been compared to Sensimetrics' software, user beware!
