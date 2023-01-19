"""The Cosmology API compatability library for Astropy.

This library provides wrappers for Astropy cosmology objects to be compatible
with the Cosmology API. The available wrappers are:

- :class:`.AstropyCosmology`: the Cosmology API wrapper for
  :mod:`astropy.cosmology.Cosmology`.


There are the following required objects for a Cosmology-API compatible library:

- constants: a module of constants. See
  :mod:`cosmology.compat.astropy.constants` for details.
"""

from . import constants
from .core import AstropyCosmology

__all__ = [
    # Cosmology API
    "constants",
    # Wrappers
    "AstropyCosmology",
]
