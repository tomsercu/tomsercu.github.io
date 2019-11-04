---
title: "Sobolev Descent"
author: "Youssef Mroueh, Tom Sercu, Anant Raj"
journal: "AISTATS"
year: 2019
arxiv: "1805.12062"
shortname: mroueh2018sobolev
thumbnail: /assets/paper_thumbs/mroueh2018sobolev.png
excerpt: ""
abstract: >
    We study a simplification of GAN training: the problem of transporting
    particles from a source to a target distribution. Starting from the Sobolev GAN
    critic, part of the gradient regularized GAN family, we show a strong relation
    with Optimal Transport (OT). Specifically with the less popular dynamic
    formulation of OT that finds a path of distributions from source to target
    minimizing a ``kinetic energy''. We introduce Sobolev descent that constructs
    similar paths by following gradient flows of a critic function in a kernel
    space or parametrized by a neural network. In the kernel version, we show
    convergence to the target distribution in the MMD sense. We show in theory and
    experiments that regularization has an important role in favoring smooth
    transitions between distributions, avoiding large gradients from the critic.
    This analysis in a simplified particle setting provides insight in paths to
    equilibrium in GANs.
selected: false
category: pubs
---
