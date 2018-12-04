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
My scripting language of choice is python but mentally swap it out for your favorite Julia/R/Matlab/etc.
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
I would argue allowing sloppiness is crucial in computational research to get ahead.
The think -> implement -> test cycle is core to our work, and therefore needs to be fast.
In this cycle the bottleneck very quickly becomes "implement".
Being able to implement a new idea quickly (and therefore sloppily) really allows us to go through new ideas, build understanding of published ideas by playing around, etc.
The uncertainty of follow-through on an idea is why you shouldn't invest too much time in clean code,
why implementation speed wins over cleanliness.
However, if an idea is worth following up on, it becomes important to refactor, or maybe just start over from scratch.

# A formula for optimal technical debt
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

* We are looking for the best decision in terms of (expected total time spent)
* Let's introduce some quantities: $$p(n)$$ is the probability we will do $$n$$ experimental runs. $$F_p(n)$$ is the CDF,
    so the probaiblity we will do $$n$$ or more experimental runs. $$F_p(1)=1$$ cause we need to do at least one run.
    Finally $$t'(n,I)$$ is the time spent to do $$n$$ runs under implementation $$I$$, which decomposes in time per run $$t(n,I)$$:
    $$t'(n,I) = \sum_{j=1}^n t(n,I)$$. So this time per run $$t(n,I)$$ depends on the how many'th run this is,
    and on the implementation $$I$$.
    For a quick and dirty implementation $$I_d$$ the trade-off is that $$t(1,I_d)$$ is small,
    but all consecutive $$t(n>1, I_d)$$ will be larger than for a cleaner implementation $$I_c$$.
    We call $$m_I$$ the max number of experimental runs we will do at which point we will decide to refactor,
    also depending on implementation $$I$$ (cleaner implementations will have higher $$m_I$$).
* The expected time spent under implementation $$I$$ is
    $$T_I = \mathbb{E}_{n\sim p}[t(n,I)]$$ and can easily be shown
    to be $$T_I = \sum_{n=1}^{m_I} F_p(n) t(n,I) + \text{future}(n>m_I)$$.
* *Assumption 1*: we will consider a dirty implementation $$I_d$$ against its proper clean implementation $$I_c$$.
    After $$m_{I_d}$$ experiments we will be done with the dirty way and refactor to the proper implementation $$I_c$$.
    We will decide whether we should go dirty first or if we should implement it the proper way immediately.
* *Assumption 2*: simple breakdown of $$t(n,I)$$: we say the time spent $$t(n,I)$$ simplify to $$t(1,I) = t^1_I$$ initial time,
    $$t(1<n<m_I,I)=t^x_I$$ time to do a new experiment with this implementation,
    and $$t(m_I,I)=t^{r}_I$$ time to refactor to the proper implementation once the limit is reached.
    Under this assumpton, $$T_I = t^1_I + p(n>1) \mathbb{E}_x t^x_I + p(n>m_I) t^r_I + \text{future}(n>m_I)$$.
    We introduced $$\mathbb{E}_x = \mathbb{E}_{n \sim p(.|n>1)}[n]$$ the expected number of experiments conditioned on
    $$n>1$$ so in the moderate success regime: we don't abandon right after the first experiment.
* *Assumption 3*: For dirty implementation $$I_d$$, refactoring to the cleaner implementation $$I_c$$ will take as much
    time as implementing it from scratch - cause let's be honest that's always the case. Your dirty implementation
    really doesn't help, and often some mess has accumulated around it which you need to clean up now.
    So $$t^r_{I_d} = t^1_{I_c}$$.
* Ok now ready for our main result: the difference $$\Delta_T$$,  the difference in $$T_I$$ between clean and dirty,
    which summarizes which wil be the shorter path. Positive $$\Delta_T$$ says go dirty.
    $$\Delta_T = (1-p(m_{I_d})) t^1_c + p(n>1) \mathbb{E}_x (t^x_c - t^x_d)$$
* A concrete example. You are writing a quick experiment script and wonder if you should just used 
    global `ALL_CAPS_VARIABLES` whenever you need them, or set up a command line parser.
    You estimate the chance of continuing past one single experiment to be 50%,
    expected number of experiments XX THIS IS TROUBLE
    and after doing 10 experiments you'll be tired of doing it the sloppy way and need to switch. 
    Now $$\Delta_T = $$.

# Take-aways
Deciding between a sloppy quick implementation versus the reference clean implementation, we have to think about:
* the estimated time cost of both implementations, 
* the difference of time cost for reusing the code for a couple more experiments
* how many times you would reuse the sloppy code before investing the effort to do the clean implementaiton
* the probabilities of (a) some success, some further experiments and (b) success, leading to long-term use
  and need for the clean implementation.

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
