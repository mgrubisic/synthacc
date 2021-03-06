# Synthacc
A Python toolbox for kinematic earthquake ground motion modelling!

The current version is 0.0.1, which means *totally not ready to be used by someone else*, but if you want you can try and help me improving the library!

Bart Vleminckx @ Royal Observatory of Belgium (bart . vleminckx @ observatory . be)


## Installation
I use Synthacc from source on Windows 10 (64-bit) with Python 3.6 in a [Miniconda](http://conda.pydata.org/miniconda.html) virtual environment. Install the dependencies from the [conda-forge](https://conda-forge.org) channel.

```
conda install -c conda-forge --file requirements.txt
```

So no [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell) anymore thanks to conda! Only *scikit-fmm* has to be installed with pip.

```
pip install scikit-fmm
```

Clone the Synthacc repository and add its folder to the PYTHONPATH environment variable. Ready!


## References
* Aki K. and Richards P (2002). Quantitative Seismology (2nd edition). University Science Books.
* Akkar S., Sandikkaya M., Senyurt M., Sisi A., Ay B., Traversa P., Douglas J., Cotton F., Luzi L., Hernandez B. and Godey S. (2014). Reference database for seismic ground-motion in Europe (RESORCE). Bulletin of Earthquake Engineering, 12(1), 311-339.
* Ambraseys N., Smit P., Douglas J., Margaris B., Sigbjornsson R., Olafsson S., Suhadolc P. and Costa G. (2004). Internet-Site for European Strong-Motion Data. Bollettino di Geofisica Teorica ed Applicata, 45(3), 113-129.
* Beyreuther M., Barsch R., Krischer L., Megies T., Behr Y. and Wassermann J. (2010). ObsPy: A Python Toolbox for Seismology. Seismological Research Letters, 81(3), 530-533.
* Boore D. (2003). Simulation of Ground Motion Using the Stochastic Method. Pure and Applied Geophysics, 160(3-4), 635-676.
* Cartwright D. and Longuet-Higgins M. (1956). The statistical distribution of maxima of a random function. Proceedings of the Royal Society of London. Series A, 237(1209), 212-232.
* Cotton F. and Coutant O. (1997). Dynamic stress variations due to shear faults in a plane-layered medium. Geophysical Journal International, 128, 676-688.
* Graves R. and Pitarka A. (2010). Broadband Ground-Motion Simulation Using a Hybrid Approach. Bulletin of the Seismological Society of America, 100(5A), 2095-2123.
* Graves R. and Pitarka A. (2016). Kinematic Ground-Motion Simulations on Rough Faults Including Effects of 3D Stochastic Velocity Perturbations. Bulletin of the Seismological Society of America, 106(5), 2136-2153.
* Hanks T. and Kanamori H. (1979). A Moment Magnitude Scale. Journal of Geophysical Research, 84(B5), 2348-2350.
* Havskov J. and Ottemöller L. (2010). Routine Data Processing in Earthquake Seismology. Springer.
* Johnston A. and Schneider J. (1994). Seismotectonic interpretations and conclusions from the stable continental region seismicity database, in The Earthquake of Stable Continental Regions. Volume 1: Assessment of Large Earthquake Potential. Report to Electric Power Research Institute, TR-102261-V1.
* Jost M. and Herrmann R. (1989). A Student's Guide to and Review of Moment Tensors. Seismological Research Letters, 60(2), 37-57.
* Kikuchi M. and Kanamori H. (1991). Inversion of complex body waves - part III. Bulletin of the Seismological Society of America, 81(6), 2335-2350.
* Krischer L., Hutko A., van Driel M., Stähler S., Bahavar M., Trabant C. and Nissen-Meyer T. (2017). On-demand custom broadband synthetic seismograms. Seismological Research Lettets, 88(4), 1127-1140.
* Leonard M. (2014). Self-Consistent Earthquake Fault-Scaling Relations: Update and Extension to Stable Continental Strike-Slip Faults. Bulletin of the Seismological Society of America 104(6), 2953-2965.
* Liu P. and Archuleta R. (2004). A new nonlinear finite fault inversion with three-dimensional Green’s functions: Application to the 1989 Loma Prieta, California, earthquake. Journal of Geophysical Research, 109, B02318.1-15.
* Liu P., Archuleta R. and Hartzell S. (2006). Prediction of Broadband Ground-Motion Time Histories: Hybrid Low/High-Frequency Method with Correlated Random Source Parameters. Bulletin of the Seismological Society of America, 96(6), 2118-2130.
* Mai P. and Beroza G. (2002). A spatial random field model to characterize complexity in earthquake slip. Journal of Geophysical Research, 107, B11, ESE 10 1-21.
* Mai P., Spudich P. and Boatwright J. (2005). Hypocenter Locations in Finite-Source Rupture Models. Bulletin of the Seismological Society of America, 95(3), 965-980.
* Minson S. and Dreger D. (2008). Stable inversions for complete moment tensors. Geophysical Journal International, 174, 585-592.
* Newmark N. (1959). A method of computation for structural dynamics. Journal of Engineering Mechanics, 85(EM3), 67-94.
* Nigam N. and Jennings P. (1969). Calculation of response spectra from strong-motion earthquake records. Bulletin of the Seismological Society of America, 59(2), 909-922.
* Nissen-Meyer T., van Driel M., Stähler S., Hosseini K., Hempel S., Auer L., Colombi A. and Fournier A. (2014). AxiSEM: broadband 3-D seismic wavefields in axisymmetric media. Solid Earth, 5, 425-445.
* Pagani M., Monelli D., Weatherill G., Danciu L., Crowley H., Silva V., Henshaw, P. Butler L., Nastasi M., Panzeri L., Simionato M. and Vigano D. (2014). OpenQuake Engine: An Open Hazard (and Risk) Software for the Global Earthquake Model. Seismological Research Letters, 85(3), 692–202.
* Schmedes J., Archuleta R. and Lavallée D. (2010). Correlation of earthquake source parameters inferred from dynamic rupture simulations. Journal of Geophysical Research, 115, B03304.1-B03304.12
* Shearer P. (2009). Introduction to Seismology (2nd edition). Cambridge University Press.
* Somerville P., Irikura K., Graves R., Sawada S., Wald D., Abrahamson N., Iwasaki Y., Kagawa T., Smith N. and Kowada A. (1999). Characterizing Crustal Earthquake Slip Models for the Prediction of Strong Ground Motion. Seismological Research Letters, 70(1), 59-80.
* Somerville P., Collins N., Abrahamson N., Graves R. and Saikia C. (2001). Ground motion attenuation relations for the central and eastern United States. Report to U.S. Geological Survey.
* Stein S. and Wyession M. (2003). An Introduction to Seismology, Earthquakes, and Earth Structure. Blackwell Publishing.
* Thingbaijam K., Mai P. and Goda K. (2017). New Empirical Earthquake Source-Scaling Laws. Bulletin of the Seismological Society of America, 107(5), 2225-2246.
* Vallée M. and Douet V. (2016). A new database of source time functions (STFs) extracted from the SCARDEC method. Physics of the Earth and Planetary Interiors, 257, 149-157.
* Vallée M., Charléty J., Ferreira A., Delouis B. and Vergoz J. (2011). SCARDEC: a new technique for the rapid determination of seismic moment magnitude, focal mechanism and source time functions for large earthquakes using body-wave deconvolution. Geophysical Journal International, 184, 338-358.
* van Driel M., Krischer L., Stähler S., Hosseini K. and Nissen-Meyer T. (2015). Instaseis: instant global seismograms based on a broadband waveform database. Solid Earth, 6, 701-717.
* Wang R. (1999). A Simple Orthonormalization Method for Stable and Efficient Computation of Green’s Functions. Bulletin of the Seismological Society of America, 89(3), 733–741.
* Wells D. and Coppersmith K. (1994). New Empirical Relationships among Magnitude, Rupture Length, Rupture Width, Rupture Area, and Surface Displacement. Bulletin of the Seismological Society of America, 84(4), 974-1002.
* Wesnousky, S. (2008). Displacement and Geometrical Characteristics of Earthquake Surface Ruptures: Issues and Implications for Seismic-Hazard Analysis and the Process of Earthquake Rupture. Bulletin of the Seismological Society of America, 98(4), 1609-1632.


