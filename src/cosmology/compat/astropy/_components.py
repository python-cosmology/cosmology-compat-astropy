"""The cosmology API."""

from __future__ import annotations

from typing import TYPE_CHECKING

import astropy.units as u
import numpy as np

__all__: list[str] = []

if TYPE_CHECKING:
    from astropy.cosmology import FLRW
    from astropy.units import Quantity

    from cosmology.compat.astropy._core import InputT


class TotalComponent:
    cosmo: FLRW

    @property
    def Omega_tot0(self) -> Quantity:
        return np.asarray(self.cosmo.Otot0) << u.one

    def Omega_tot(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Otot(z)) << u.one


class CurvatureComponent:
    cosmo: FLRW

    @property
    def Omega_k0(self) -> Quantity:
        return np.asarray(self.cosmo.Ok0) << u.one

    def Omega_k(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Ok(z)) << u.one


class MatterComponent:
    cosmo: FLRW

    @property
    def Omega_m0(self) -> Quantity:
        return np.asarray(self.cosmo.Om0) << u.one

    def Omega_m(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Om(z)) << u.one


class BaryonComponent:
    cosmo: FLRW

    @property
    def Omega_b0(self) -> Quantity:
        # TODO: cache
        return (
            np.asarray(self.cosmo.Ob0) if self.cosmo.Ob0 is not None else np.zeros(())
        ) << u.one

    def Omega_b(self, z: InputT, /) -> Quantity:
        try:
            return np.asarray(self.cosmo.Ob(z)) << u.one
        except ValueError:
            return np.asarray(np.zeros_like(z)) << u.one


class NeutrinoComponent:
    cosmo: FLRW

    @property
    def Omega_nu0(self) -> Quantity:
        return np.asarray(self.cosmo.Onu0) << u.one

    @property
    def Neff(self) -> Quantity:
        return np.asarray(self.cosmo.Neff) << u.one

    @property
    def m_nu(self) -> tuple[Quantity, ...]:
        return tuple(self.cosmo.m_nu.to(u.eV))

    def Omega_nu(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Onu(z)) << u.one


class DarkEnergyComponent:
    cosmo: FLRW

    @property
    def Omega_de0(self) -> Quantity:
        return np.asarray(self.cosmo.Ode0) << u.one

    def Omega_de(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Ode(z)) << u.one


class DarkMatterComponent:
    cosmo: FLRW

    @property
    def Omega_dm0(self) -> Quantity:
        # TODO: cache
        return (
            np.asarray(
                self.cosmo.Odm0 if self.cosmo.Odm0 is not None else self.cosmo.Om0,
            )
            << u.one
        )

    def Omega_dm(self, z: InputT, /) -> Quantity:
        try:
            return np.asarray(self.cosmo.Odm(z)) << u.one
        except ValueError:
            return np.asarray(self.cosmo.Om(z)) << u.one


class PhotonComponent:
    cosmo: FLRW

    @property
    def Omega_gamma0(self) -> Quantity:
        return np.asarray(self.cosmo.Ogamma0) << u.one

    def Omega_gamma(self, z: InputT, /) -> Quantity:
        return np.asarray(self.cosmo.Ogamma(z)) << u.one