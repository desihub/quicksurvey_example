# Clone&Play DESI survey simulation sample

The following commands should be enough to simulate a small DESI patch of 100 sq. deg on cori.
This will run separately a `dark` and a `bright` survey.

A notebook showing simple plots for the spatial distribution in the results `plot_quicksurvey_results.ipynb`.

More details can be found in `readme.ipynb`.


1. Source the latest desihub packages
```bash
source /project/projectdirs//desi/software/desi_environment.sh master
```

2. Checkout the quicksurvey_example (this repository) to scratch space
```bash
cd $SCRATCH
git clone https://github.com/desihub/quicksurvey_example
cd quicksurvey_example
```

3. Generate mock target catalogs 

Dark 
```bash
select_mock_targets --no-spectra --nproc 4 --nside 16 --seed 10 \
    -c $SCRATCH/quicksurvey_example/targets/no_spectra/dark/input.yaml \
    --output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/dark \
    --tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_dark.fits
```

Bright
```bash
select_mock_targets --no-spectra --nproc 4 --nside 16 --seed 10   \
	-c $SCRATCH/quicksurvey_example/targets/no_spectra/bright/input.yaml   \
	--output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/bright  \
	--tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_bright.fits
```

4. Combine individual healpix files into the full catalog
```bash
join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/dark
join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/bright
```

5. Rename the standard stars
```bash
mv $SCRATCH/quicksurvey_example/targets/no_spectra/dark/standards-dark.fits $SCRATCH/quicksurvey_example/targets/no_spectra/dark/standards.fits
mv $SCRATCH/quicksurvey_example/targets/no_spectra/bright/standards-bright.fits $SCRATCH/quicksurvey_example/targets/no_spectra/bright/standards.fits

```

6. Run quicksurvey
```bash
quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/dark    \
	    -E $SCRATCH/quicksurvey_example/survey/subset_exposures_dark.fits  \
	    --output_dir $SCRATCH/quicksurvey_example/zcat/dark  \
	    -f $(which fiberassign)    \
	    -D $SCRATCH/quicksurvey_example/fiberassign/subset_dark_fiberassign_dates.txt
```

```bash
quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/bright \
	    -E $SCRATCH/quicksurvey_example/survey/subset_exposures_bright.fits \
	    --output_dir $SCRATCH/quicksurvey_example/zcat/bright  \
	    -f $(which fiberassign)   \
	    -D $SCRATCH/quicksurvey_example/fiberassign/subset_bright_fiberassign_dates.txt
```
