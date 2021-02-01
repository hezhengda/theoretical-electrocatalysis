How to calculate the DOS and PDOS for the system?
=================================================

The DOS and PDOS can help us understand the electronic structure of the material or specific atom. These information can be very helpful in understanding the activity of certain reactions among different catalysts and also analyze the bonding between atoms. 

**Quantum Espresso**

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

**VASP** 

In VASP it is really easy, just add :code:`LORBIT=11` in your :code:`INCAR`