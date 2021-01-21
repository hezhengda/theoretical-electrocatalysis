How to calculate the energy and do geometric relaxation on a chemical system?
===============================================================================

If we want to calculate the energy, we will need:

* The structure of the chemical system (The detailed discussion about how to construct the chemical system are shown in this page: :ref:`How to build the chemical structures?`)
* The code that we want to use 
* The input file (or input parameters) for the simulation.

So in below, we will introduce how to get the energy from different softwares.

**Step 1**: Prepare the structure of the chemical system that you want to investigate

.. toggle::

    .. note::
    
        In here, it is very important to ask yourself questions in below:

        * How large the system do I need?
        * Do I need to consider solvation environment? If solvation is needed, do I consider then explicitly or implicitly?
        * What is the configuration of the surface?
        * Do I have all the possibilities?

**Step 2**: Choose the software that you want to use

.. toggle::

    .. note::

        The two most popuplar softwares for calculting the energy by DFT method would be: (1) `Quantum Espresso <https://www.quantum-espresso.org/>`_  (2) `VASP <https://www.vasp.at/>`_ . The difference is that VASP would cost (lots of) money, but Quantum Espresso is open-source, that means it is free to use. But you can choose whatever you want.

**Step 3**: Prepare the input files for the software

.. toggle::

    .. note::
    
        Usually the input file contains the parameters for the DFT simulations. When we think about a DFT simulation, we need those things:

        * Chemical structure 
        * Pseudopotential for all the elements 
        * k-points mesh for the system 
        * parameters for electronic relaxation (SCF cycle)
        * parameters for atomic relaxation (if we want to relax the system)
        * parameters for cell relaxation (if we want to relax the cell and the atomic positions at the same time)

        We can divide all the parameters in the software into these 6 categories we have mentioned above, it will help us understand how DFT simulation actually works.

Now let's get into the examples, we will use the adsorption of CO on Pt(111) as our example.

Quantum Espresso 
-----------------



VASP 
------