# Clone&Play DESI survey simulation sample

The following commands should be enough to simulate a small DESI patch of 100 sq. deg.

```bash
cd $SCRATCH

git clone git@github.com:desihub/quicksurvey_example.git


select_mock_targets --no-spectra -c $SCRATCH/quicksurvey_example/targets/no_spectra/dark/select-mock-targets-dark.yaml --nside 16 --output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/dark --seed 10 --tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_dark.fits

join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/dark

select_mock_targets --no-spectra -c $SCRATCH/quicksurvey_example/targets/no_spectra/bright/select-mock-targets-bright.yaml --nside 16 --output_dir $SCRATCH/quicksurvey_example/targets/no_spectra/bright --seed 10 --tiles $SCRATCH/quicksurvey_example/survey/subset_tiles_bright.fits

join_mock_targets --mockdir $SCRATCH/quicksurvey_example/targets/no_spectra/bright


quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/dark -E $SCRATCH/quicksurvey_example/survey/subset_exposures_dark.fits  --output_dir $SCRATCH/quicksurvey_example/zcat/dark -f $(which fiberassign) -t $SCRATCH/quicksurvey_example/fiberassign/template_fiberassign_dark.txt -D $SCRATCH/quicksurvey_example/fiberassign/subset_dark_fiberassign_dates.txt

quicksurvey -T $SCRATCH/quicksurvey_example/targets/no_spectra/bright -E $SCRATCH/quicksurvey_example/survey/subset_exposures_bright.fits  --output_dir $SCRATCH/quicksurvey_example/zcat/bright -f $(which fiberassign) -t $SCRATCH/quicksurvey_example/fiberassign/template_fiberassign_bright.txt -D $SCRATCH/quicksurvey_example/fiberassign/subset_bright_fiberassign_dates.txt
```
