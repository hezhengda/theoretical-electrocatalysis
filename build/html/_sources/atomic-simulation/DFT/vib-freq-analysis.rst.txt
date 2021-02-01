How to calculate the vibrational frequencies?
==============================================

Calculating vibrational frequencies is very important in computation. From the vibrational frequencies we can: (1) compare with vibrational spectroscopy (e.g. IR) (2) calculate the corrections of zero-point energy and the entropy contribution to the DFT energy in order to get the free energy of the system: :math:`G=E+ZPE-T*S`. The formulation for ZPE and T*S are shown in below:

.. math::

    ZPE = \frac{1}{2}\sum_ihc\nu_i

.. math::

    T*S = k_B\{\frac{A}{k_BT}\frac{1}{\exp(A)-1}-\ln[1-\exp(-A)]\}

where: :math:`A=hc\nu_i/k_BT`, and :math:`\nu_i` is the vibrational frequencies we get from the simulation (unit: cm^-1). In here the unit of the speed of light (c) needs to be cm/s. **Pay extra attention to the unit!**

The procedure for calculating vibrational frequency is really simple:

**Quantum Espresso**

**Step 1**: Do the geometric optimization on the structure 

**Step 2**: Get the optimized structure, then create another file called :code:`INP_PH` for the :code:`ph.x` software.

An example of INP_PH is shown in below:

.. code-block:: bash

    Normal modes for CO2
    &inputph
    tr2_ph=1.0d-14,
    prefix='CO2',
    amass(1)=12.010,
    amass(2)=15.999,
    outdir='$TMP_DIR'
    epsil=.true.,
    trans=.true.,
    asr=.true.
    fildyn='dmat.co2'
    nat_todo = 2
    /
    0.0 0.0 0.0
    1 3 # the index for the atoms that we want to calculate (usually the adsorbates)

The execution of the :code:`ph.x` can be written as: :code:`ph.x -i INP_PH > OUT_PH`.

.. note::

    The file listed in here needs to be adjusted to your own system.

**VASP** 

VASP is easier than Quantum Espresso, we only need to adjust the value for :code:`IBRION=5`, and add :code:`NFREE=2` to our system (which I think is more straightforward than Quantum Espresso, just personal opinion.)
