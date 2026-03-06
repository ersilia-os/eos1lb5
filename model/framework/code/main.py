import os
import csv
import sys
import pandas as pd

from lazyqsar.api.binary_qsar_predict import predict, prepare_files, read_output_array

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

MODELPATH = os.path.join(root, "..", "..", "checkpoints")

models = ["valitalo2016", "sarathy2016", "janardhan2016", "radchenko2023", "lepori2025_mtb", "lepori2025_msm"]

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# create files for lazyqsar api
files = prepare_files(smiles_list, models)

# run predictions
predict(MODELPATH, files["input_csv"], files["output_csv"], files["models_txt"])

# read predictions from output_csv
R = read_output_array(files["output_csv"])

# write output in a .csv file
df = pd.DataFrame(R, columns = ["epr_proba", "diff_proba", "perm_proba_janardhan", "perm_proba_mtbpen", "perm_proba_lepori_mtb", "perm_proba_lepori_msm"])

# write output in a .csv file
df.to_csv(output_file, index=False)

# removing temporary files
os.remove(files["input_csv"])
os.remove(files["output_csv"])
os.remove(files["models_txt"])