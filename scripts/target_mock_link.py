import numpy as np
import os
import argparse
import yaml

from desitarget.mock.io import decode_rownum_filenum
from desitarget.mock.io import load_all_mocks
from astropy.table import Table
import desitarget.mock.io as dtmockio


parser = argparse.ArgumentParser()
parser.add_argument('--config','-c',default='input.yaml')
parser.add_argument("--targettype", "-T", help="Target type (i.e. LRG, QSO, ELG)", type=str, default="MWS")
parser.add_argument("--input_dir", "-I", help="Path to the truth.fits and target.fits files", type=str, default="./")
args = parser.parse_args()


with open(args.config,'r') as pfile:
    params = yaml.load(pfile)


#remove information from sources different than args.targettype
source_name = args.targettype
keys = []
for k in params['sources'].keys():
    keys.append(k)

for k in keys:
    if k!=source_name:
        params['sources'].pop(k)

# load the mocks
mock_dict = load_all_mocks(params)

# load truth
truth_table = Table.read(os.path.join(args.input_dir, 'truth.fits'))
print('loaded {} truth items'.format(len(truth_table)))

# load targets
target_table = Table.read(os.path.join(args.input_dir, 'targets.fits'))
print('loaded {} target items'.format(len(target_table)))



ii = truth_table['SOURCETYPE']==source_name
rowid, fileid = decode_rownum_filenum(truth_table['MOCKID'][ii])

fileid_to_read = np.array(list(set(fileid)))
print(fileid_to_read)

n = np.count_nonzero(ii)
mock_ra = np.empty((0))
mock_dec = np.empty((0))

dict_format_func = {'galaxia':'_load_mock_mws_file'}

for i in fileid_to_read:
    filename =  mock_dict[source_name]['FILES'][i]
    source_format = params['sources'][source_name]['format']

    func_name = dict_format_func[source_format]
    func = getattr(dtmockio, func_name)
    result = func(filename)

    rows_to_get = rowid[fileid==i]
    mock_ra = np.append(mock_ra, result['RA'][rows_to_get])

    print(result)


from IPython import embed; embed()
