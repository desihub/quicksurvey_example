# Clone&Play DESI survey simulation sample

### code setup

Quick setup at NERSC edison using pre-installed code:

```bash
module use /global/common/edison/contrib/desi/modulefiles
module load desimodules
```

That will configure everything you need to run quicksurvey except the
input files in this repository.

Clone this repository and `cd` into it
```
git clone https://github.com/desihub/quicksurvey_example.git
cd quicksurvey_example
```

### surveysim

Run the observing operations simulator "surveysim" from within the
`surveysim/` subdirectory (it will dump a lot of fits files there):
```bash
cd surveysim
cat ../input/epoch*.txt > tilelist.txt
ipython
```

From within ipython:
```python
from surveysim.surveysim import surveySim
tilelist = np.loadtxt('tilelist.txt', dtype=int)
surveySim((2020,1,1), (2020,6,1), tilesubset=tilelist)
```

This will leave a bunch of fits files in the current directory; the most
important is `obslist_all.fits` with the order and observing conditions
for each tile.

TODO: update surveysim to have an `outputdir` option.

### mock target catalog

Go back to the top level directory of this repository (`cd ..`) and
generate a mock target catalog with
```bash
time select_mock_targets -c input/mock_inputs.yaml --output_dir input/ \
  --realtargets /project/projectdirs/desi/target/catalogs/targets-dr3.1-0.8.1.fits
```
That will take ~7 minutes and output several files in the `input/` directory
(they are ouput of `select_mock_targets` but input to `quicksurvey`):
* `targets.fits` - a target catalog analogous to a real data target catalog
* `truth.fits` - row-matched truth information about those targets
* `sky.fits` and `stdstars.fits` - sky and standard star targets for fiberassign
* `mtl.fits` - the first pass "merged target list", also for fiberassign

### quicksurvey

Now run the `quicksurvey` wrapper of fiberassign, quickcat, and merged
target list generation:
```bash
time quicksurvey --output_dir output/  \
  --targets_dir input/  \
  --fiberassign_exec `which fiberassign` \
  --template_fiberassign input/template_fiberassign.txt \
  --obsconditions surveysim/obslist_all.fits \
  --fiberassign_dates input/fiberassign_dates.txt
```
(if you don't have quicksurvey and fiberassign in your `$PATH`, provide
the full path to them)

This will take ~5 minutes.  See `output/README.md` for details of what
is written there.

If you want to run observing epochs with a pre-determined tile list and
median observing conditions, you can specify the location of `epoch{n}.txt`
files (n is 0-indexed, one tile per line in each file).
```bash
time quicksurvey --output_dir output/  \
  --targets_dir input/  \
  --fiberassign_exec `which fiberassign` \
  --template_fiberassign input/template_fiberassign.txt \
  --epochs_dir input/ \
  --n_epochs 3
```

Coming soon:
To pick up where you left off, you can use `--start_epoch` (0-indexed):
```bash
time quicksurvey --output_dir output/  \
  --targets_dir input/  \
  --fiberassign_exec `which fiberassign` \
  --template_fiberassign input/template_fiberassign.txt \
  --epochs_dir input/ \
  --start_epoch 3 \
  --n_epochs 6
```
Note: `--n_epochs` is the total number of epochs including the ones that
you are skipping

### Log output

The output of `surveysim` should look like this
```
2020-01-01 19:00:00
The survey will start from scratch.
WARNING: ErfaWarning: ERFA function "dtf2d" yielded 1 of "dubious year (Note 6)" [astropy._erfa.core]

Conditions at the beginning of the night: 
	Seeing:  0.8936879533080855 arcseconds
	Transparency:  1.0
	Cloud cover:  17.118102355534635 %
On the night starting  2020-01-01 19:00:00.000 , we observed  3  tiles.
There are  186 left to observe.

Conditions at the beginning of the night: 
	Seeing:  1.2598259444024036 arcseconds
	Transparency:  0.8293976510609495
	Cloud cover:  24.86994679717109 %
On the night starting  2020-01-02 19:00:00.000 , we observed  3  tiles.
There are  183 left to observe.

Bad weather forced the dome to remain shut for the night.
On the night starting  2020-01-03 19:00:00.000 , we observed  0  tiles.
There are  183 left to observe.

...

Conditions at the beginning of the night: 
	Seeing:  0.6912051898633905 arcseconds
	Transparency:  0.7057028458005875
	Cloud cover:  0.9656024269303759 %
On the night starting  2020-04-16 19:00:00.000 , we observed  1  tiles.
There are  0 left to observe.

```

The output of `selec_mock_targets` should look like this

```bash
According to config in:    input/mock_inputs.yaml

The following populations and paths are specified:
type: BGS
 format: durham_mxxl_hdf5 
 path: /project/projectdirs/desi/mocks/bgs/MXXL/desi_footprint/v0.0.3
type: ELG
 format: gaussianfield 
 path: /project/projectdirs/desi/mocks/GaussianRandomField/v0.0.4
type: LRG
 format: gaussianfield 
 path: /project/projectdirs/desi/mocks/GaussianRandomField/v0.0.4
type: LYAQSO
 format: lyaqso 
 path: /project/projectdirs/desi/mocks/lya_forest/v0.0.2
type: MWS_MAIN
 format: galaxia 
 path: /project/projectdirs/desi/mocks/mws/galaxia/alpha/v0.0.2/bricks
type: MWS_WD
 format: wd100pc 
 path: /project/projectdirs/desi/mocks/mws/wd100pc/v0.0.1
type: SKY
 format: gaussianfield 
 path: /project/projectdirs/desi/mocks/GaussianRandomField/v0.0.1/2048
type: STD_FSTAR
 format: galaxia 
 path: /project/projectdirs/desi/mocks/mws/galaxia/alpha/v0.0.2/bricks
type: TRACERQSO
 format: gaussianfield 
 path: /project/projectdirs/desi/mocks/GaussianRandomField/v0.0.4
...
Great total of 2331880 targets 117142 stdstars 548276 sky pos
Started writing StdStars file
Finished writing stdstars file
Started writing sky to file
Finished writing sky file
Started writing Targets file
Finished writing Targets file
Started computing the MTL file
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.5910322666168213
DEBUG: calc_priority has 2331880 unobserved targets
0 of 2331880 targets have priority zero, setting N_obs=0.
Started writing the first MTL file
Finished writing mtl file
Started writing Truth file
Finished writing Truth file
done!
```

The output of the `quick_survey` should look like this

```bash
Epoch 0
462 tiles to be included in fiberassign
Thu Nov 10 15:32:54 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.7434730529785156
DEBUG: calc_priority has 2331880 unobserved targets
0 of 2331880 targets have priority zero, setting N_obs=0.
Thu Nov 10 15:33:15 2016 Finished MTL
Thu Nov 10 15:33:15 2016 Launching fiberassign
Thu Nov 10 15:35:14 2016 Finished fiberassign
Thu Nov 10 15:35:14 2016 58 tiles to gather in zcat
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype BGS. Simply assigning a redshift from the truth table.
WARNING in desisim.quickcat.get_redshift_efficiency()
	 We are not modelling yet the redshift efficiency for type: STAR. Set to 1.0
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype GALAXY. Simply assigning a redshift from the truth table.
Thu Nov 10 15:35:42 2016 Finished zcat
Epoch 1
404 tiles to be included in fiberassign
Thu Nov 10 15:35:42 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.6160461902618408
DEBUG: calc_priority has 2104725 unobserved targets
136267 of 2331880 targets have priority zero, setting N_obs=0.
/global/common/edison/contrib/desi/conda/conda_3.5-20160829/lib/python3.5/site-packages/astropy/table/column.py:1095: MaskedArrayFutureWarning: setting an item on a masked array which has a shared mask will not copy the mask and also change the original mask array in the future.
Check the NumPy 1.11 release notes for more information.
  ma.MaskedArray.__setitem__(self, index, value)
Thu Nov 10 15:36:23 2016 Finished MTL
Thu Nov 10 15:36:23 2016 Launching fiberassign
Thu Nov 10 15:38:11 2016 Finished fiberassign
Thu Nov 10 15:38:11 2016 57 tiles to gather in zcat
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype BGS. Simply assigning a redshift from the truth table.
WARNING in desisim.quickcat.get_redshift_efficiency()
	 We are not modelling yet the redshift efficiency for type: STAR. Set to 1.0
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype GALAXY. Simply assigning a redshift from the truth table.
Thu Nov 10 15:38:44 2016 Finished zcat
...
Epoch 7
57 tiles to be included in fiberassign
Thu Nov 10 15:52:37 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.6403970718383789
DEBUG: calc_priority has 939883 unobserved targets
1250903 of 2331880 targets have priority zero, setting N_obs=0.
Thu Nov 10 15:53:27 2016 Finished MTL
Thu Nov 10 15:53:27 2016 Launching fiberassign
Thu Nov 10 15:54:00 2016 Finished fiberassign
Thu Nov 10 15:54:00 2016 57 tiles to gather in zcat
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype BGS. Simply assigning a redshift from the truth table.
WARNING in desisim.quickcat.get_redshift_efficiency()
	 We are not modelling yet the redshift efficiency for type: STAR. Set to 1.0
WARNING desisim.quickcat.get_observed_redshifts()
	 We dont have a model for objtype GALAXY. Simply assigning a redshift from the truth table.
Thu Nov 10 15:55:29 2016 Finished zcat

```

The `inputs` and `outputs` directories include each a `README` files explaining their structure.

### Development code

To run `quicksurvey` you need to have the following products installed.

* `desisim`
* `desitarget`
* `fiberassignment`

To run `surveysim` you additionally need the following

* `desisurvey`
* `surveysim`
* `specsim`
* `desimodel`
* `desiutil` (?)

To replace one of the pre-installed copies with your own git clone,

```bash
module unload desisim
git clone https://github.com/desihub/desisim
export PYTHONPATH=`pwd`/desisim/py:$PYTHONPATH
export PATH=`pwd`/desisim/bin:$PATH
```

Some of us use personal module files to set PATH and PYTHONPATH;
Others use configuration scripts to do the same.
If you prefer to install all DESI code from your own checkouts, you can
get the non-DESI python dependencies with:
```bash
module use /global/common/edison/contrib/desi/modulefiles
module load desi-conda
```
