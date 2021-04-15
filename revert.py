import argparse

import qiime2
import pandas as pd
import skbio
from q2_types.feature_data import DNAIterator
from biom.util import biom_open
from biom import Table

parser = argparse.ArgumentParser()
parser.add_argument(
    '--biom-qza', help='Biom table of counts.', required=True)
parser.add_argument(
    '--seq-qza', help='Sequences.', required=True)
parser.add_argument(
    '--biom-out', help='Biom table of counts without hashes.', required=True)
parser.add_argument(
    '--seq-out', help='Sequences without hashes.', required=True)
args = parser.parse_args()

table = qiime2.Artifact.load(args.biom_qza).view(pd.DataFrame)
seqs = qiime2.Artifact.load(args.seq_qza).view(DNAIterator)
lookup = {n.metadata['id']: str(n) for n in seqs}
table_cols = list(map(lambda x: lookup[x], table.columns))
with biom_open(args.biom_out, 'w') as f:
    Table(table.values.T, list(table_cols), list(table.index)).to_hdf5(f, 'formatted')
open(args.seq_out, 'w').write(''.join(list(map(lambda x: f'>{x}\n{x}\n', table_cols))))
