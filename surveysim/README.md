After running surveysim as described in the top level README.md, this
directory will contain a multiple fits files:

* `obslist{YEARMMDD}.fits` - tables of what tiles were observed on what days
  under what conditions (seeing, moon, etc.)
* `obslist_all.fits` - a concatenation of the other obslist tables
* `obsplan{YEARMMDD}.fits` - daily plan of what might get observed
  (as opposed to obslist which is what actually was observed)
* tiles_observed.fits - used internal to the simulator to track what tiles
  have been observed already

