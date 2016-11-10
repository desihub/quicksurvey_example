# quicksurvey_example

To run `quicksurvey` you need to have the following products installed.

* `desisim`
* `desitarget`
* `fiberassignment`

And then execute the following two scripts:

```bash
~/desitarget/bin/select_mock_targets -c input/mock_inputs.yaml 
~/desisim/bin/quicksurvey -O output/ -T input/ -f ~/fiberassign/bin/./fiberassign -E input/ -t input/template_fiberassign.txt -N 8
```
