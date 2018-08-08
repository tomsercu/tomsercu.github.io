---
title:  "Technical debt in data science and ML research. A case for sloppy code. Sometimes."
category: blog
tags: [perspective, code, machine-learning]
---
* uol toc
{:toc}

I have been thinking for a while about the code we write for ML research and data science,
specifically the kind of code that's not part of some "main codebase":
think code snippets or jupyter notebooks to investigate something weird going on during neural network training,
to explore a new data set,
or to do a one-off analysis of a model (which you may repeat for a couple of different models),
etc.


# Technical debt
Is a concept introduced by Ward Cunningham in [^1] and expanded upon in [^2].

[^1]: <http://c2.com/doc/oopsla92.html>
[^2]: <http://wiki.c2.com/?WardExplainsDebtMetaphor>

Directly quoting the relevant section:

> Another, more serious pitfall is the failure to consolidate. Although immature code may work fine and be completely acceptable to the customer, excess quantities will make a program unmasterable, leading to extreme specialization of programmers and finally an inflexible product. Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite. Objects make the cost of this transaction tolerable. The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object- oriented or otherwise. [^1]

The problem with the usual way to treat technical debt, is the (implicit) assumption that code is part of a long-lived codebase, and that poorly structured code will have lasting consequences.

# Expanding to a research workflow
There are some key ideas not quite captured in the usual treatment of technical debt.

1. Short (and unpredictable) lifetime of code.
2. Keep all the artefacts.
3. 

### Short lifetime
This is the most obvious one and, interestingly, it was captured quite accurately in the original definition quoted above.
The key phrase is 

### Keep all the artefacts
Ok, now 

# My rules of thumb


# References
