# quicksurvey_example

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
