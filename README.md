<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# Overview: Relation extraction with spaCy

For details on data sourcing and model training, see this [Colab](https://colab.research.google.com/drive/1marycqYnZzFB-Rqd6crFFYvZvWOtaKoE?usp=sharing) notebook. A copy is stored in `experiments.ipynb`.

To test the best model, follow the installation steps, add a list of newline-delimited sentences to `assets/sentences.txt`, and run `spacy project run infer` after configuring the env variables `TRF_PATH="deepset/minilm-uncased-squad2"` and `MODEL_STRING="minilm-uncased-squad2"` (either directly in `project.yml` or via CLI). See the [Demo](https://colab.research.google.com/drive/1marycqYnZzFB-Rqd6crFFYvZvWOtaKoE#scrollTo=-fl1qdKS1nhZ) section of the [Colab](https://colab.research.google.com/drive/1marycqYnZzFB-Rqd6crFFYvZvWOtaKoE?usp=sharing) notebook for an example. 


### Installation

1. clone the repo and `cd` into it
2. copy one or more [trained model directories](https://drive.google.com/drive/folders/1-5SxyYSaiTy-BzWfGCV7dunHurJkxwdz?usp=sharing) to the `models` directory
2. create a Python environment and install these dependencies:\

    `!pip install -U pip setuptools wheel`\
    `!pip install spacy`\
    `!python -m spacy download en_core_web_trf`\
    `!pip install spacy transformers`
    
3. run any of the commands - for retraining (GPU required), see the [Subtask 4 of the Solution section](https://colab.research.google.com/drive/1marycqYnZzFB-Rqd6crFFYvZvWOtaKoE#scrollTo=sRsbmO2xCd5h) in [Colab](https://colab.research.google.com/drive/1marycqYnZzFB-Rqd6crFFYvZvWOtaKoE?usp=sharing)


### Commands

The following commands are defined by the project. They
can be executed using `spacy project run [name]`
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `train` | Train the model with a Transformer on a GPU and evaluate on the dev corpus. Works fine with Colab GPUs. |
| `evaluate` | Apply model specified in the environment variable TRF_NAME to new, unseen text, and measure accuracy at different thresholds. |
| `infer` | Apply the model to an arbitrary list of sentences, for qualitative evaluation or model probing. |
| `clean` | Remove intermediate files to start inference from a clean slate. |


### Assets

The following assets may be defined arbitrarily:

| File | Source | Description |
| --- | --- | --- |
| `assets/sentences.txt` | Local | Input sentence file for inference, one example per line, separated by newlines. |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
