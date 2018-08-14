---
title: "Regularized Kernel and Neural Sobolev Descent: Dynamic MMD Transport"
author: "Youssef Mroueh, Tom Sercu, Anant Raj"
journal: "Under Review"
year: 2018
arxiv: "1805.12062"
shortname: mroueh2018regularized
thumbnail: /assets/paper_thumbs/mroueh2018regularized.png
excerpt: ""
abstract: >
    We introduce Regularized Kernel and Neural Sobolev Descent for transporting a
    source distribution to a target distribution along smooth paths of minimum
    kinetic energy (defined by the Sobolev discrepancy), related to dynamic optimal
    transport. In the kernel version, we give a simple algorithm to perform the
    descent along gradients of the Sobolev critic, and show that it converges
    asymptotically to the target distribution in the MMD sense. In the neural
    version, we parametrize the Sobolev critic with a neural network with input
    gradient norm constrained in expectation. We show in theory and experiments
    that regularization has an important role in favoring smooth transitions
    between distributions, avoiding large discrete jumps. Our analysis could
    provide a new perspective on the impact of critic updates (early stopping) on
    the paths to equilibrium in the GAN setting.
selected: false
category: pubs
---
