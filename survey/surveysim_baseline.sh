#!/bin/bash
#############################################################################
# Simulate the baseline survey strategy described in DESI-doc-1767-v3.
# Note that this is one random realization of the observing conditions.
# Change the random seed for a different realization.
# This will take ~1 hours to run and writes ~50MB to $DESISURVEY_OUTPUT.
#############################################################################
export DESISURVEY_OUTPUT=${SCRATCH}'/quicksurvey_example/survey'

INIT_ARGS='--verbose --config-file '${DESISURVEY_OUTPUT}/'config.yaml'
PLAN_ARGS='--verbose --fa-delay 1m --config-file '${DESISURVEY_OUTPUT}/'config.yaml'
SIM_ARGS='--verbose --seed 123 --strategy HA+fallback --config-file '${DESISURVEY_OUTPUT}/'config.yaml'

surveyinit ${INIT_ARGS}
surveyplan --create ${PLAN_ARGS}
surveysim ${SIM_ARGS}

while :
do
    (surveyplan ${PLAN_ARGS}) || break
    (surveysim --resume ${SIM_ARGS}) || break
done
