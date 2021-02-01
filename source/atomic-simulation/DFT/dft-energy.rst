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

**Quantum Espresso**

If you have the :code:`cif` file for your structure, then you can use `Tools on Materials Cloud <https://www.materialscloud.org/work/tools/qeinputgenerator>`_ to get the input file.

For our system (:code:`examples/Pt111-CO.cif`, you can view this from `github <https://github.com/hezhengda/theoretical-electrocatalysis>`_ ), the input file for pw.x in Quantum Espresso is:

.. code-block:: Bash

    &CONTROL
    calculation = 'scf' # The type of calculation that you want to make 
    etot_conv_thr =   1.8000000000d-04 # convergence criteria for total energy 
    forc_conv_thr =   1.0000000000d-04 # convergence criteria for total force 
    outdir = './out/' # the output folder
    prefix = 'aiida' # the prefix, used for output files 
    pseudo_dir = './pseudo/' # the folder for pseudopotential
    tprnfor = .true. # print the force in the end 
    tstress = .true. # print the stress of the cell in the end 
    verbosity = 'low' # how much information do you want to print 
    /
    &SYSTEM
    degauss =   1.4699723600d-02 # value for gaussian-smearing 
    ecutrho =   8.0000000000d+02 # cutoff energy for electronic density 
    ecutwfc =   1.0000000000d+02 # cutoff energy for wave function
    ibrav = 0 # means we need to specify cell parameter in the CELL_PARAMETERS part 
    nat = 18 # number of atoms in our system 
    ntyp = 3 # number of types of atoms in our system 
    occupations = 'smearing'
    smearing = 'cold'
    /
    &ELECTRONS
    conv_thr =   3.6000000000d-09 # convergence criteria for self-consistent field calculation 
    electron_maxstep = 80 # maximum number of steps of SCF loop
    mixing_beta =   4.0000000000d-01 # value for mixing the old electronic density with the new one. Like the "training rate" in ML.
    /
    ATOMIC_SPECIES # specify the types of atoms and the corresponding pseudopotential
    C      12.011 C.pbesol-n-kjpaw_psl.1.0.0.UPF
    O      15.9994 O.pbesol-n-kjpaw_psl.0.1.UPF
    Pt     195.08 pt_pbesol_v1.4.uspp.F.UPF
    ATOMIC_POSITIONS crystal # the geometric coordinates of the system, really important!
    Pt           0.5000000000       0.5000000000       0.3750000000 
    Pt          -0.0000000000      -0.0000000000       0.3750000000 
    Pt           0.5000000000      -0.0000000000       0.3750000000 
    Pt          -0.0000000000       0.5000000000       0.3750000000 
    Pt           0.1666700000       0.1666700000       0.4583300000 
    Pt           0.6666700000       0.6666700000       0.4583300000 
    Pt           0.1666700000       0.6666700000       0.4583300000 
    Pt           0.6666700000       0.1666700000       0.4583300000 
    Pt           0.8333300000       0.8333300000       0.5416700000 
    Pt           0.3333300000       0.3333300000       0.5416700000 
    Pt           0.8333300000       0.3333300000       0.5416700000 
    Pt           0.3333300000       0.8333300000       0.5416700000 
    Pt           0.5000000000       0.5000000000       0.6250000000 
    Pt          -0.0000000000       0.0000000000       0.6250000000 
    Pt           0.5000000000       0.0000000000       0.6250000000 
    Pt          -0.0000000000       0.5000000000       0.6250000000 
    C            0.5000000000       0.5000000000       0.6685200000 
    O            0.5000000000       0.5000000000       0.7120400000 
    K_POINTS automatic # The k-point mesh for the system.
    7 7 2 0 0 0
    CELL_PARAMETERS angstrom
        5.6285700000       0.0000000000       0.0000000000
        2.8142850000       4.8744846070       0.0000000000
        0.0000000000       0.0000000000      27.5742000000

Then you can use :code:`pw.x -i INP_PWSCF > OUT_PWSCF` to execute and get the energy of your structure.

**VASP** 
