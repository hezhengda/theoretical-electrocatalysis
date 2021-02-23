How to calculate the vibrational frequencies?
==============================================

Calculating vibrational frequencies is very important in computation. From the vibrational frequencies we can: (1) compare with vibrational spectroscopy (e.g. IR) (2) calculate the corrections of zero-point energy and the entropy contribution to the DFT energy in order to get the free energy of the system: :math:`G=E+ZPE-T*S`. The formulation for ZPE and T*S are shown in below:

.. math::

    ZPE = \frac{1}{2}\sum_ihc\nu_i

.. math::

    T*S = k_B\{\frac{A}{k_BT}\frac{1}{\exp(A)-1}-\ln[1-\exp(-A)]\}

where: :math:`A=hc\nu_i/k_BT`, and :math:`\nu_i` is the vibrational frequencies we get from the simulation (unit: cm^-1). In here the unit of the speed of light (c) needs to be cm/s. **Pay extra attention to the unit!**
