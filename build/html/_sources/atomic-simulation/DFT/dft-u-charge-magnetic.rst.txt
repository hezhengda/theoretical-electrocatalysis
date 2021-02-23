How to get the charge and magnetic moment on each atom?
=========================================================

It has already been shown in (1) :ref:`How to calculate the energy and do geometric relaxation on a chemical system?` and (2) :ref:`How to calculate the DOS and PDOS for the system?` how to get the energy and (projected) density of states, which can be very useful in explaining the experimental trends or do mechanistic analysis. But sometimes we want to have more information about the system, for example, for magnetic system, we would like to know the distribution of magnetic moments inside the material, and we also want to know the exact charge on different atoms. For doing this we need more input parameters to finely controlled the DFT code.

Several ways to converge the simulation 
-----------------------------------------

In this section, I will discuss several practical experience in doing difficult simulations (e.g. with spin polarization and DFT+U method, and also with uncertain structures):

* Usually we want to calculate more complicated simulation from a converged structure. For example, if we want to calculate the DFT+U and spin polarized simulation, then first we can do geometric optimization on the structure (with plain DFT), then add the U parameter and spin configuration and do further simulations.
* 

