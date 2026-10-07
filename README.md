# Mycobacterium cell wall penetration

Scores how far a compound travels along the route to Mycobacterium tuberculosis, which shelters in necrotic lung lesions beyond the reach of many drugs. Ersilia assembled six LazyQSAR classifiers from published data covering entry into lung epithelial lining fluid (56 clinically measured drugs), diffusion into caseum (279 compounds in a binding assay) and cell wall permeation from inferred activity data, the 5,371-compound MtbPen set and a click-chemistry screen in both M. tuberculosis and M. smegmatis. Each uses the cut-off its own authors defined, so the six scores share no common scale.

This model was incorporated on 2025-11-25.Last packaged on 2026-08-07.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1lb5`
- **Slug:** `mycobacterium-permeability`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `Antimicrobial activity`, `Permeability`, `ADME`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `6`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probabilities from six classifiers covering lung fluid entry, caseum diffusion and mycobacterial cell wall permeation across four datasets.

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
- **Environment Size (Mb):** `5841`
- **Image Size (Mb):** `5785.7`

**Computational Performance (seconds):**
- 10 inputs: `192.98`
- 100 inputs: `109.59`
- 10000 inputs: `948.27`

### References
- **Source Code**: [https://github.com/ersilia-os/ai2050-mtb-penetration](https://github.com/ersilia-os/ai2050-mtb-penetration)
- **Publication**: [https://doi.org/10.1021/acsinfecdis.6b00051](https://doi.org/10.1021/acsinfecdis.6b00051)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2016`
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
