#!/bin/bash
#############################################################################
# Simulate the baseline survey strategy described in DESI-doc-1767-v3.
# Note that this is one random realization of the observing conditions.
# Change the random seed for a different realization.
# This will take ~4 hours to run and writes ~1.7G to $DESISURVEY_OUTPUT.
# Remove the --scores option to reduce the output size to ~50M.
#############################################################################
export DESISURVEY=${SCRATCH}'/quicksurvey_example/survey'
PLAN_ARGS='--verbose --fa-delay 1m'
SIM_ARGS='--verbose --scores --seed 123 --strategy HA+fallback'

surveyinit --verbose
surveyplan --create ${PLAN_ARGS}
surveysim ${SIM_ARGS}

while :
do
    (surveyplan ${PLAN_ARGS}) || break
    (surveysim --resume ${SIM_ARGS}) || break
done
