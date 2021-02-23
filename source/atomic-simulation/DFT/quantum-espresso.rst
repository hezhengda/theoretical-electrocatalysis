Quantum Espresso 
===================

PWSCF (Regular Package)
---------------------------

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

If we want to use DFT+U and spin polarization, there are several parameters that we need to add to the input file.

.. code-block:: bash

    # for DFT+U settings
    lda_plus_u = .true.
    hubbard_u(1) = 5.0

    # for spin-polarization settings 
    nspin = 2
    tot_magnetization = #some number 
    starting_magnetization(1) = 0.1
    starting_ns_eigenvalue(1, 1, 1) = 1.0 # this is for finely tuning the initial magnetization, the first number is the index of the orbital (e.g. for d band it ranges from 1 to 5), the second number is the index of spin (1 or 2), the third number is the index of the atom (see that in ATOMIC SPECIES in the input file).

    # if you want to constrain the magnetic moment 
    &ELECTRONS 
    mixing_fixed_ns = 10 # In 10 SCF steps, the magnetic moment will be the same as mentioned in starting_ns_eigenvalue.

PHonon Package (ph.x)
---------------------------

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

DOS (dos.x) and PDOS (projwfc.x)
--------------------------------------

In Quantum Espresso, the procedure for calculating DOS or PDOS has 4 steps:

**Step 1**: Do the geometric optimization of the structure, you can see that in :ref:`How to calculate the energy and do geometric relaxation on a chemical system?`

**Step 2**: Do the SCF calculation (replace the :code:`calculation` from :code:`relax/vc-relax` to :code:`scf`)

**Step 3**: Keep the output file and do the NSCF calculation (replace the :code:`calculation` from :code:`scf` to :code:`nscf`)

**Step 4**: In the same directory, create a file named :code:`INP_PROJWFC`, the content is shown in below:

.. code-block:: bash

    &PROJWFC
    DeltaE = 0.01
    ngauss = 0  
    degauss = 0.015
    Emin = -40
    Emax = 40

Then you can use :code:`projwfc.x` to execute it: :code:`projwfc.x -i INP_PROJWFC > OUT_PROJWFC`. For calculating DOS, you can use :code:`dos.x`, the input parameters can be seen in `this link <https://www.quantum-espresso.org/Doc/INPUT_DOS.html>`_ 

After that, you can use :code:`pp.x` to do the post-process procedure, or you can use python or other softwares to do the plotting and further analysis.
    