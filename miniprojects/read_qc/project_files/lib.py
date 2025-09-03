from collections import namedtuple
from pathlib import Path

import numpy as np
from Bio import SeqUtils


def quality_scores(seq_record):
    pass


def mean_quality_score(seq_record):
    pass


def gc_percent(seq_record):
    pass


def maybe_strip_primer(seq_record, primers):
    pass


def is_quality_good(seq_record):
    pass


def sample_id(path: Path) -> str:
    pass


def filtered_outfile_name(path):
    directory = path.resolve().parent

    # Strip off the .fq.gz
    sample_name = ...

    outfile_name = f"{sample_name}.filtered.fq"

    return directory.joinpath(outfile_name)


ReadInfo = namedtuple(...)


def make_read_info(sample, seq_record):
    pass
