# Clone&Play DESI survey simulation sample

To run `quicksurvey` you need to have the following products installed.

* `desisim`
* `desitarget`
* `fiberassignment`


Clone this repository and `cd` into it
```
git clone https://github.com/forero/quicksurvey_example.git
cd quicksurvey_example
```

Assuming you have `desisim`, `desitarget` and `fiberassign` in your home directory you can now run
the following two commands

And then execute the following two scripts:
```bash
~/desitarget/bin/select_mock_targets -c input/mock_inputs.yaml 
~/desisim/bin/quicksurvey -O output/ -T input/ -f ~/fiberassign/bin/./fiberassign -E input/ -t input/template_fiberassign.txt -N 8
```

The output of the first command should look like this

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

The output of the second command should look like this

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