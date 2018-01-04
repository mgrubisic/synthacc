"""
Tests for 'ground.recordings' module.
"""


import os
import unittest

import numpy as np

from synthacc.spectral import DFT, plot_fass
from synthacc.io.esgmd2 import read_fas

from synthacc.ground.recordings import (Waveform, Seismogram, Recording,
    ne_to_rt, rt_to_ne, plot_seismograms, plot_recordings)


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data', 'recordings')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')

TIME_DELTA = 0.005

with open(os.path.join(DATA_DIR, 'amplitudes.txt'), 'r') as f:
    AMPLITUDES = list(np.array(f.read().split(), dtype=float))

UNIT = 'm/s2'

PGM = 3.8996000


class TestSeismogram(unittest.TestCase):
    """
    """

    s = Seismogram(TIME_DELTA, AMPLITUDES, UNIT) ## ESGMD2 004676xa

    def test_properties(self):
        """
        """
        self.assertEqual(self.s.time_delta, TIME_DELTA)
        self.assertListEqual(list(self.s.amplitudes), AMPLITUDES)
        self.assertEqual(self.s.unit, UNIT)

        self.assertEqual(self.s.pgm, PGM)
        self.assertEqual(self.s.gmt, 'acceleration')

    def test_get_pgm(self):
        """
        """
        self.assertEqual(self.s.get_pgm(UNIT), PGM)
        self.assertEqual(self.s.get_pgm(None), PGM)

    def test_get_dft(self):
        """
        """
        cal_dft = self.s.get_dft('m/s2')
        self.assertEqual(type(cal_dft), DFT)
        cal_fas = cal_dft.fas
        tgt_fas = read_fas(os.path.join(DATA_DIR, '004676xa.fas'))
        fs = os.path.join(OUTPUT_DIR, 'recordings.seismogram.dft.png')
        plot_fass([tgt_fas, cal_fas], labels=['tgt', 'cal'], colors=['r', 'b'],
            widths=[2, 0.5], title='dft calculation', png_filespec=fs)
