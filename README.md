# Mycobacterium cell wall penetration

Compendium of models to predict the likelihood that a molecule enters the lungs (from Valitalo et al, 2016), diffuses through the caseum lesions (from Sarathy et al, 2016) and finally permeates through the bacterial cell wall (from Janardhan et al, 2016, Radchenko et al, 2023, Lepori et al 2025). The models are classifiers built based on the referenced data, using author-informed cut-offs for permeation. This model complements MycPermCheck (eos8d8a).

This model was incorporated on 2025-11-25.Last packaged on 2025-11-26.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1lb5`
- **Slug:** `mycobacterium-permeability`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `Tuberculosis`, `Permeability`, `ADME`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `6`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of lung diffusion and cell wall penetration.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| epr_proba | float | high | Probability of the compound to accumulate in the epithelial lining fluid |
| diff_proba | float | high | Probability of the compound to diffuse on caseum lesions |
| perm_proba_janardhan | float | high | Probability of the compound to penetrate the cell wall according to the dataset from Janardhan et al 2016 |
| perm_proba_mtbpen | float | high | Probability of the compound to penetrate the cell wall according to the MtbPen dataset |
| perm_proba_lepori_mtb | float | high | Probability of the compound to penetrate the cell wall in Mtb according to the dataset from Lepori et al 2025 |
| perm_proba_lepori_msm | float | high | Probability of the compound to penetrate the cell wall in Msm according to the dataset from Lepori et al 2025 |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos1lb5](https://hub.docker.com/r/ersiliaos/eos1lb5)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1lb5.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1lb5.zip)

### Resource Consumption
- **Model Size (Mb):** `12`
- **Environment Size (Mb):** `1911`
- **Image Size (Mb):** `7516.16`

**Computational Performance (seconds):**
- 10 inputs: `39.75`
- 100 inputs: `45.15`
- 10000 inputs: `1247.68`

### References
- **Source Code**: [https://github.com/ersilia-os/ai2050-mtb-penetration](https://github.com/ersilia-os/ai2050-mtb-penetration)
- **Publication**: [https://pubmed.ncbi.nlm.nih.gov/27626295/](https://pubmed.ncbi.nlm.nih.gov/27626295/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1lb5
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1lb5
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
