"""
The 'io.syngine' module. Module to get data from the IRIS Synthetics Engine
(Syngine). Syngine (Krischer et al., 2017) is a webservice that quickly returns
synthetic seismograms custom requested by the user. The IRIS DMC stores
precalculated TB scale databases of Green's Functions for several different 1D
reference models. The Green's Functions were generated by Tarje Nissen-Meyer &
colleagues using AxiSEM (Nissen-Meyer et al., 2014), an axi-symmetric spectral
element method for 3D (an-)elastic, anisotropic and acoustic wave propagation
in spherical domains. It requires axisymmetric background models and runs
within a 2D computational domain, thereby reaching all desired highest
observable frequencies (up to 2Hz) in global seismology. The requested
synthetic seismograms are calculated using Instaseis (van Driel et al., 2015),
a Python library built for storing wavefield databases with a fast extraction
algorithm.

IRIS DMC (2015), Data Services Products: Synthetics Engine
https://doi.org/10.17611/DP/SYNGINE.1 (last accessed 25/01/2018)
"""


import io

from obspy import read as _read
import requests

from ..apy import is_pos_integer, is_number, is_pos_number, is_string
from ..units import MOTION_SI as SI_UNITS
from ..earth.geo import is_lon, is_lat
from ..source.moment import MomentTensor
from ..recordings import Seismogram, Recording


DEFAULT_MODEL = 'ak135f_2s'


def get_recording_url(src_lon, src_lat, src_depth, mt, rcv_lon, rcv_lat, model=None, stf=None, duration=None, gmt='dis', components='ZRT', validate=True):
    """
    src_depth: positive number, depth of source (in m)
    mt: 'source.moment.MomentTensor' instance
    stf: pos integer
    duration: positive number, duration (in s) (default: None)
    gmt: string ('dis', 'vel' or 'acc') (default: 'dis')
    components: string ('ZRT' or 'ZNE) (default: 'ZRT')
    """
    if validate is True:
        assert(is_number(src_lon) and is_lon(src_lon))
        assert(is_number(src_lat) and is_lon(src_lat))
        assert(is_pos_number(src_depth))
        assert(type(mt) is MomentTensor)
        assert(is_number(rcv_lon) and is_lon(rcv_lon))
        assert(is_number(rcv_lat) and is_lon(rcv_lat))
        if model is not None:
            assert(is_string(model))
        if stf is not None:
            assert(is_pos_integer(stf))
        if duration is not None:
            assert(is_pos_number(duration))
        assert(gmt in SI_UNITS)
        assert(components in ('ZRT', 'ZNE'))

    url = 'http://service.iris.edu/irisws/syngine/1/query?'

    url += 'model=%s' % (model or DEFAULT_MODEL,)

    url += '&sourcelongitude={}&sourcelatitude={}&sourcedepthinmeters={}'.format(
        '%f' % (src_lon,), '%f' % (src_lat,), src_depth)

    rr, tt, pp, rt, tp, pr = mt.get_six('USE')
    rp = pr
    url += '&sourcemomenttensor={:e},{:e},{:e},{:e},{:e},{:e}'.format(
        rr, tt, pp, rt, rp, tp).replace('+', '')

    if stf is not None:
        url += '&sourcewidth=%s' % stf

    url += '&receiverlongitude={}&receiverlatitude={}'.format(rcv_lon, rcv_lat)

    if duration is not None:
        url += '&endtime={}'.format(duration)

    url += '&units={}'.format(
        {'dis': 'displacement', 'vel': 'velocity', 'acc': 'acceleration'}[gmt])

    url += '&components={}'.format(components)

    url += '&format=miniseed'

    return url


def get_recording(src_lon, src_lat, src_depth, mt, rcv_lon, rcv_lat, model=None, stf=None, duration=None, gmt='dis', components='ZRT', validate=True):
    """
    src_depth: positive number, depth of source (in m)
    mt: 'source.moment.MomentTensor' instance
    stf: pos integer
    duration: positive number, duration (in s) (default: None)
    gmt: string ('dis', 'vel' or 'acc') (default: 'dis')
    components: string ('ZRT' or 'ZNE) (default: 'ZRT')
    """
    url = get_recording_url(src_lon, src_lat, src_depth, mt, rcv_lon, rcv_lat,
        model, stf, duration, gmt, components, validate)

    stringio_obj = io.BytesIO(requests.get(url).content)
    s = _read(stringio_obj, format='MSEED')

    u = SI_UNITS[gmt]

    components = {c: Seismogram.from_trace(t, u) for c, t in zip(components, s)}

    r = Recording(components)

    return r
