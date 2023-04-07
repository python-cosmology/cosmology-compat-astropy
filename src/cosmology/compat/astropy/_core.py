"""The Cosmology API compatability wrapper for Astropy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Union, cast

import astropy.cosmology as astropy_cosmology  # noqa: TCH002
from astropy.units import Quantity
from numpy import floating
from numpy.typing import NDArray
from typing_extensions import TypeAlias  # noqa: TCH002

from cosmology.api import CosmologyNamespace
from cosmology.api import CosmologyWrapper as CosmologyWrapperAPI

__all__: list[str] = []


NDFloating: TypeAlias = NDArray[floating[Any]]
InputT: TypeAlias = Union[Quantity, NDFloating, float]

################################################################################


@dataclass(frozen=True)
class CosmologyWrapper(CosmologyWrapperAPI[Quantity, InputT]):
    """The Cosmology API wrapper for :mod:`astropy.cosmology.Cosmology`."""

    cosmo: astropy_cosmology.Cosmology

    def __cosmology_namespace__(
        self, /, *, api_version: str | None = None
    ) -> CosmologyNamespace:
        """Returns an object that has all the cosmology API functions on it.

        Parameters
        ----------
        api_version: Optional[str]
            string representing the version of the cosmology API specification
            to be returned, in ``'YYYY.MM'`` form, for example, ``'2020.10'``.
            If ``None``, it return the namespace corresponding to latest version
            of the cosmology API specification.  If the given version is invalid
            or not implemented for the given module, an error is raised.
            Default: ``None``.

            .. note:: currently only `None` is supported.

        Returns
        -------
        `cosmology.api.CosmologyNamespace`
            An object representing the Astropy cosmology API namespace.
        """
        import cosmology.compat.astropy as namespace

        return cast(CosmologyNamespace, namespace)

    @property
    def name(self) -> str | None:
        """The name of the cosmology instance."""
        return cast(Union[str, None], self.cosmo.name)
