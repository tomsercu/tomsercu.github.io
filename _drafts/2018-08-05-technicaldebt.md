---
title:  "Technical debt in computational research. A case for sloppy code. Sometimes."
category: blog
tags: [perspective, code, machine-learning]
---
I have been thinking for a while about the code we write for machine learning research and data science,
which often is code that's not part of some "big codebase".
Think about starting off exploring a new idea, or analyzing a new dataset.
For this kind of code, we end up continuously trading off between getting stuff done while writing bad code,
or writing "proper"/clean code but getting nowhere.
I will use the metaphor of "technical debt" to quantify what is the optimal decision.

* uol toc
{:toc}

# Trade-off: examples
Here are some examples from my life, but I think many similar choices will exist in every scientific or engineering
discipline which running some form of computational experiments or simulations based on code.
My scripting language is python but mentally swap it out for your favorite Julia/R/Matlab/etc.
* Exploring a new dataset with some plotting and viewing statistics. Do everything on the command line, in a jupyter notebook,
    or write some general purpose functions? What if you know this dataset will be updated next week and you'll want to do it
    all over?
* Dataset preparation: do it ad hoc with a bunch of bash commands? Collect those in a bash script? Write a python script to do it all in one go?
* Configuring a small experimental setup: set up command line args parser? Just 3 command line args in a fixed order? Or just put a bunch of variables on top? 
* When lightly changing your code to try a new idea: what do you properly configure, what do you just hardcode?
* Keeping a single flat python file or break it down into modules?
* Just access those global variables or properly pass everything as function arguments?
* Everything plain functions or define some classes?

In a big long-lived project, the optimal choices are clear: do it the "proper" way.
I'd argue that in computational research it's rarely that clean-cut: the uncertainty about whether and how often we'll reuse the code
changes what is the optimal choice.
Let's formalize this a bit.
<!--These decisions are made when starting a "new project" where we're uncertain about how much we'll reuse the code.-->

# Technical debt
Is a concept introduced by Ward Cunningham in [^1] and expanded upon in [^2].

[^1]: <http://c2.com/doc/oopsla92.html>
[^2]: <http://wiki.c2.com/?WardExplainsDebtMetaphor>

Directly quoting the relevant section (bold is mine):

> Another, more serious pitfall is the failure to consolidate. Although immature code may work fine and be completely acceptable to the customer, excess quantities will make a program unmasterable, leading to extreme specialization of programmers and finally an inflexible product. Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite. Objects make the cost of this transaction tolerable. The danger occurs when the debt is not repaid. **Every minute spent on not-quite-right code counts as interest on that debt**. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object- oriented or otherwise. [^1]

Ok so I think this metaphor is quite apt, even though it's phrased here for production (long-lived) code to be shipped to some customer.
The main argument is how important it is to refactor sloppy code, and just don't write it in the first place if you don't have to.

The bold part, and specifically the idea of "*every minute spent*" is the crux to generalize to research code.
The problem for us computational researchers is: we really don't know ahead of time
how much time we'll be spending on any given idea, or piece of code.
It is in the very nature of our work to have start-stop pieces of code that won't be touched more than once or twice.

So I want to think a bit more formally about how much debt (or code sloppiness) we optimally are willing to accumulate on a given project,
taking into account how much interest we'll have to pay.
After all, a loan on which you don't have to pay any interest and which you don't even have to pay back, is just free money.

# Assessing a project for allowable sloppiness
I think the main axis to score a project are:
* Duration: will this project live for one day? A week? Many years?
    - And let's make this probabilistic: how much time will you spend minimally (if first experiments fail and something else becomes more important)?
    Excpected (if you see the result you're expecting)? Maximally - don't account for this case, cause you'll want to start fast, then refactor heavily.
* Length. If your codebase is under a 100 lines of code, you can probably build a full mental picture of it in
    a matter of minutes. So sloppiness is much more ok here.
    Since debt is mostly about the mental overhead for the programmers working on bad code, you don't go into debt much if you can easily keep the whole codebase in mind.
* Repetition with variation: thinking ahead of time which variations you're likely to do will point you to the parts of your codebase that have to be better organized.
    Same model on 3 datasets? Dataloading has to be super clean.
    Two model variations you'll always want to compare during development & debugging? Make sure you have a clean and simple way to switch between the two.
    Reversely, if you don't foresee a certain variation happening anytime soon, don't code it up. Just don't. At most put a placeholder that raises an exception.

I realize I haven't really elaborated much on the importance of sloppiness.

# The importance of sloppiness


# My rules of thumb
* Keep all the artefacts. This could become its own blogpost, but whatever I do, however sloppy I allow my code to be:
    every experiment is its own directory where the exact codebase, run command, and output is stored together.
    Always organize your workflow like this.
* If a team is working on the codebase, two notches up in cleanliness.
    But allow yourself an easy way to experiment outside of the main codebase as to not stifle any new ideas.
* Making deliberate decisions and using priority lists / todo lists.
    This helps to clearly decide when a project or line of experimentation will become bigger and should be switched to the next level of cleanliness: time for a big refactoring.
* 


# References
