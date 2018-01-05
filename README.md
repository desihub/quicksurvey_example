# Clone&Play DESI survey simulation sample

The following commands should be enough to simulate a small DESI patch of 100 sq. deg on cori.
This will run separately a `dark` and a `bright` survey.
More details can be found in `readme.ipynb`.

```bash
# If you don't do this in your .bash* files:
source /project/projectdirs//desi/software/desi_environment.sh 17.12

# Checkout the quicksurvey_example to scratch space
cd $SCRATCH
git clone https://github.com/desihub/quicksurvey_example

# Generate dark time mock target catalogs
select_mock_targets --no-spectra --nside 16 --seed 10 \
    -c $SCRATCH/quicksurvey_example/targets/no_spectra/dark/select-mock-targets-dark.yaml \
    --output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/dark \
    --tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_dark.fits

# Combine individual healpix files into the full catalog
join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/dark

# Now repeat for the bright time survey
select_mock_targets --no-spectra --nside 16 --seed 10 \
    -c $SCRATCH/quicksurvey_example/targets/no_spectra/bright/select-mock-targets-bright.yaml \
    --output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/bright \
    --tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_bright.fits

join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/bright

# Run quicksurvey for the dark time; this includes surveysims, fiberassign, and quickcat
quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/dark \
    -E $SCRATCH/quicksurvey_example/survey/subset_exposures_dark.fits \
    --output_dir $SCRATCH/quicksurvey_example/zcat/dark \
    -f $(which fiberassign) \
    -t $SCRATCH/quicksurvey_example/fiberassign/template_fiberassign_dark.txt \
    -D $SCRATCH/quicksurvey_example/fiberassign/subset_dark_fiberassign_dates.txt

# Run quicksurvey for the bright time
quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/bright \
    -E $SCRATCH/quicksurvey_example/survey/subset_exposures_bright.fits \
    --output_dir $SCRATCH/quicksurvey_example/zcat/bright \
    -f $(which fiberassign) \
    -t $SCRATCH/quicksurvey_example/fiberassign/template_fiberassign_bright.txt \
    -D $SCRATCH/quicksurvey_example/fiberassign/subset_bright_fiberassign_dates.txt
```
