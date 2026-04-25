===================================
Welcome to openczjp's documentation
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Home <self>
   Development Notes <devnotes/index>


--------
Overview
--------

openczjp = Open Commuting Zones in Japan

In 1987, the USDA's Economic Research Service (ERS) and its partners at land grant universities developed 'Commuting Zones' (CZ's) and 'Labor Market Areas' (LMA's) `Tolbert & Killian (1987) <ref-tolbert1987labor_>`_ as delineated geographic areas for measuring integrated labor processes. These delineations were successful and were used for research in academia and for program and public policy formulation. This success led to a second delineation after the 1990 Census and a revision of the CZs after the 2000 Census. For the 2010 Census, `Fowler, Rhubart, & Jensen (2016) <ref-fowler2016reassessing_>`_ undertook substantial revision of CZs with more robust measures of fit both for CZs and for the counties that belong to them. Using microdata from `IPUMS`_, Fowler updated and published new CZs for the 2020 Census `(See Fowler, 2024) <ref-fowler2024new_>`_. Fowler placed all related code and data in the Github repository `CommutingZones2020`_.

.. _CommutingZones2020: https://github.com/csfowler/CommutingZones2020

.. _IPUMS: https://www.ipums.org/

`Acemoglu et al (2016) <ref-acemoglu2016import_>`_ used CZs to analyse the effect of Chinese imports on employment in the United States and find that import growth from China between 1990 and 2011 led to an employment reduction of 2.4 million workers.

Working from commuting data derived from Japanese population census microdata in relation to research on domestic fertility `Ichimura et al. (2025) <ref-ichimura_kakenhi_15h05692_>`_, `Adachi et al (2020) <ref-adachi2020commuting_>`_ delineated commuting zones in Japan using `Killian & Tolbert's (1993) <ref-killian1993mapping_>`_ methodology applied to municipalities. Adachi placed related data and code in the Github repository `computing_zone_japan`_. `Adachi, Kawaguchi & Saito (2024) <ref-adachi2024robots_>`_ used these CZs in a shift-share analysis of the effects of robots on local labor markets in Japan.

.. _computing_zone_japan: https://github.com/daisukeadachi/commuting_zone_japan

`openczjp` has the following objectives:

#. Port `computing_zone_japan`_, which is in R, into Python and replicate its CZs using more readily available commuting data from the Japanese Population Census

#. Port `CommutingZones2020`_, which is also in R, into Python, and apply its methods and measures of fit to Japanese CZs

#. Provide `openczjp` as a Python package that will enable researchers to formulate and test their own CZ models

------------
Bibliography
------------

.. include:: ../.pandoc/bibliography.rst

