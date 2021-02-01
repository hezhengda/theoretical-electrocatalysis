How to get the charge and magnetic moment on each atom?
=========================================================

It has already been shown in (1) :ref:`How to calculate the energy and do geometric relaxation on a chemical system?` and (2) :ref:`How to calculate the DOS and PDOS for the system?` how to get the energy and (projected) density of states, which can be very useful in explaining the experimental trends or do mechanistic analysis. But sometimes we want to have more information about the system, for example, for magnetic system, we would like to know the distribution of magnetic moments inside the material, and we also want to know the exact charge on different atoms. For doing this we need more input parameters to finely controlled the DFT code.

**Quantum Espresso**

In Quantum Espresso, we can do this by adding (1) U parameter and (2) spin polarized simulation, which means we need to add the following parameters to our :code:`INP_PWSCF` file mentioned in :ref:`How to calculate the energy and do geometric relaxation on a chemical system?`

.. code-block:: bash

    # for DFT+U settings
    lda_plus_u = .true.
    hubbard_u(1) = 5.0

    # for spin-polarization settings 
    nspin = 2
    tot_magnetization = #some number 
    starting_magnetization(1) = 0.1
    starting_ns_eigenvalue(1, 1, 1) = 1.0 # this is for finely tuning the initial magnetization

    # if you want to constrain the magnetic moment 
    &ELECTRONS 
    mixing_fixed_ns = 10 # In 10 SCF steps, the magnetic moment will be the same as mentioned in starting_ns_eigenvalue.

