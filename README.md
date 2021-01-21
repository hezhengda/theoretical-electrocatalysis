# theoretical-electrocatalysis
In this repository, we will summarise the procedure of theoretical simulation in electrocatalytic system, it will be a huge task, but it will be interesting to do in the lowdown.

## Official website of this project
https://theoretical-electrocatalysis.readthedocs.io/en/latest/

## The purpose of this project
In theoretical electrocatalysis, there are many procedures and methodologies in order to get the information about certain systems, but these methods are not well-documented, and it is not easy for beginners to quickly learn these procedures, and often in literature they are not stated fully. So this project is established in order to solve this problem.

In this project, we will summarize all the most important procedures for getting the potential energy profiles, the activation energies, the different ways to do electronic structure analysis, and make them like a book from computer science, usually titled (The cookbook series). It could be useful for the beginners to learn how to do those simulations, and what is good about this project is that we will have some "sample" scripts, not the "extremely elementary" scripts from the tutorial session in the website of the software, but real-life examples of certain systems (could from the paper we have found on the internet.)

If you want to collaborate in the project, you can fork, and join me (maybe later I can change the "me" to "us").

## The structure of this cookbook
I would like it to be "recipe-like", where you have clear steps for doing specific tasks. And below each steps, we will introduce some technical issues by using the "**toggle**" feature ([sphinx-toggle](https://sphinx-togglebutton.readthedocs.io/en/latest/)), although the user interface is not the prettiest, but it will do the job (for now). And the nice thing about this tool is that we can nest the "toggle", so we can put all the information in one page without getting the page too crowded.

An example is shown below:

```
.. note:: **Step 1**: Build the structure for your system.
   :class: dropdown, toggle-shown

   This is the test.

**Step 1**: Build the structure for your system.

.. toggle::

   This is an important toggle.

**Step 2**: Prepare the input file.

.. toggle::

   I think I can add more things in here.

   .. note::

      Maybe I can also add some notes in here.
```

## Proposed procedure that we are going to cover in this project 

### How to build structures for the simulation?
It is really important to learn how to construct different types of materials or chemical systems, because this is the starting point for all the simulation. So we must pay great attention to this question.

### DFT 

* Calculating the potential energy profile of certain mechanism on certain surface (DFT + Vibrational Frequency Analysis)
* Calculating the activation energy of certain elementary step on certain surface (NEB / CI-NEB)
* Doing the electronic structure analysis (DOS/PDOS, Charge/Population analysis, Wavefunction Analysis)

