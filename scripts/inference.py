import typer
from pathlib import Path
import spacy
from spacy.tokens import DocBin, Doc

from rel_pipe import make_relation_extractor, score_relations
from rel_model import create_relation_model, create_classification_layer, create_instances, create_tensors

import numpy
from spacy.vocab import Vocab
from spacy import Language

import random
import typer
from pathlib import Path
import spacy
from spacy.tokens import DocBin, Doc
from spacy.training.example import Example
from wasabi import Printer

# make the factory work
from rel_pipe import make_relation_extractor, score_relations, score_relations_with_negs

# make the config work
from rel_model import create_relation_model, create_classification_layer, create_instances, create_tensors


Doc.set_extension("rel", default={}, force=True)
msg = Printer()

def main(sentence_path: Path, model_path: Path, outf_path: Path):
    ner = spacy.load('en_core_web_trf')
    relation_extractor = spacy.load(model_path)

    docs, ids = [], set()
    with open(sentence_path, 'r') as f:
        texts = f.readlines()

    docs = list(ner.pipe(texts))
    processed = []
    for i, doc in enumerate(docs):
        # msg.info(doc.ents)
        doc.ents = [e for e in doc.ents if e.label_ in ['PERSON', 'ORG']]
        # msg.info(doc.ents)
        for name, proc in relation_extractor.pipeline:
            doc = proc(doc)
            # msg.info(doc._.rel)
            for value, rel_dict in doc._.rel.items():
                        for e in doc.ents:
                            for b in doc.ents:
                                if e.start == value[0] and b.start == value[1] and rel_dict['PERSON_AND_COMPANY'] > 0.3:
                                    processed.append({'index' : i, 'person_and_company' : (e.text, b.text)})
    for p in processed:
        msg.info(p)
    with open(outf_path, 'w') as f:
        for o in processed:
            f.write(str(o))
            f.write('\n')

if __name__ == "__main__":
    typer.run(main)
