# xarray talk by Daniel González

Environment populated with:

conda install -c conda-forge xarray cfgrib cartopy cdsapi pip jupyter

## How to fetch the files

The full route involves setting up the CDS API to access data from the Climate Data Store,
then using the dl_*.py scripts to fetch the datasets. However, that is a bit cumbersome as
it requires the user to register for an account, set up the API key and then wait for the
request to be processed by the ECMWF datacenter. Therefore, the .grib files have been made
available through the links in the files.txt file.
