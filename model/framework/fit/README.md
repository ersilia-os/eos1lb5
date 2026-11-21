# Fit folder: mycobacterium-permeability (eos1lb5)

This folder holds the data, code and results needed to rebuild the model. It is stored with
[eosvc](https://github.com/ersilia-os/eosvc) in the **public** bucket; only this README is
tracked in git.

## Data processing

The six training sets in `data/` were curated by Ersilia from the publications cited in the model metadata, keeping each author's own cut-off. No processing script was kept with them.

## Model building

`src/01_fit_oof.py` builds one LazyQSAR 3.9.3 classifier per task, in slow mode. For each task
it runs five-fold stratified out-of-fold (OOF) cross-validation (seed 42), so every compound
gets one prediction from a model that never saw it. It writes the OOF predictions and metrics to
`results/`, then trains the final model on all compounds into `model/checkpoints/<task>/`.
`src/02_performance.py` plots the OOF ROC curve and the OOF rank of actives and inactives per
task, and collects all metrics in `results/oof_metrics.json`.

```bash
cd src
OMP_NUM_THREADS=1 python 01_fit_oof.py        # or one task: python 01_fit_oof.py valitalo2016
python 02_performance.py
```

| Task | Output column | Training file | Compounds | Actives | OOF AUROC | Descriptors in final model |
|---|---|---|---|---|---|---|
| `valitalo2016` | `epr_rank` | `data/valitalo2016.csv` | 70 | 25 | 0.822 | chemeleon, morgan, rdkit |
| `sarathy2016` | `diff_rank` | `data/sarathy2016.csv` | 280 | 41 | 0.914 | chemeleon, rdkit, clamp |
| `janardhan2016` | `perm_rank_janardhan` | `data/janardhan2016.csv` | 330 | 275 | 0.995 | chemeleon, clamp, morgan |
| `radchenko2023` | `perm_rank_mtbpen` | `data/radchenko2023.csv` | 5,371 | 2,671 | 0.878 | chemeleon, clamp, morgan |
| `lepori2025_mtb` | `perm_rank_lepori_mtb` | `data/lepori2025_mtb.csv` | 1,564 | 702 | 0.906 | chemeleon, rdkit, cddd |
| `lepori2025_msm` | `perm_rank_lepori_msm` | `data/lepori2025_msm.csv` | 1,564 | 688 | 0.916 | chemeleon, cddd, rdkit |
