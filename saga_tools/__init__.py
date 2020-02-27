# pylint:disable=missing-docstring
from immutablecollections import immutabledict
from vistautils.memory_amount import MemoryAmount, MemoryUnit

from saga_tools.version import version as __version__  # noqa

SLURM_MEMORY_UNITS = immutabledict(
    [
        (MemoryUnit.KILOBYTES, "K"),
        (MemoryUnit.MEGABYTES, "M"),
        (MemoryUnit.GIGABYTES, "G"),
        (MemoryUnit.TERABYTES, "T"),
    ]
)


def to_slurm_memory_string(memory_request: MemoryAmount) -> str:
    return f"{memory_request.amount}" f"{SLURM_MEMORY_UNITS[memory_request.unit]}"
