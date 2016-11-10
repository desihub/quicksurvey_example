In this directory we are going to store the files
that [`quicksurvey`](https://github.com/desihub/desisim/blob/master/bin/quicksurvey) needs as an input.

The first set of data files come as product of [`select_mock_targets`](https://github.com/desihub/desitarget/blob/master/bin/select_mock_targets):

* `targets.fits`
* `truths.fits`
* `sky.fits`
* `stdstars.fits`

The second set of files are part of this repository:

* `epochs*.txt`: Set of files that include tile IDs and define the survey strategy.
* `template_fiberassign.txt`: File to be modified every time `fiberassign` runs for a different epoch.