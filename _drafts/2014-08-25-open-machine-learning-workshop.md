---
layout: post
title:  "Open Machine Learning Workshop in NYC, August 2014"
date:   2014-08-25 21:05:14
categories: machine-learning
---

Last friday, August 22, I attended the Open Machine Learning Workshop hosted by John Langford, Alekh Agarwal and Alina Beygelzimer at Microsof Research in NYC. 
In this post I want to summarize some of the main topics that were covered.
The first half of the workshop were presentations from the lead developers of major open source machine learning projects: Liblinear, Vowpal Wabbit, Torch, Theano + Pylearn, Shogun, and Stan.
After the lunch break Léon Bottou moderated a panel discussion with the authors.

In this post I want to summarize what each presenter talked about, and the panel discussion.

CJ Lin is the lead developer of **LIBLINEAR**, one of the most widely used linear SVM packages (for example wrapped in the LinearSVC classifier from scikit-learn).
The purpose of liblinear is simply to provide a fast implementation of linear SVMs for general purpose.
Lin talked about the current selection of solvers used in LIBLINEAR.

Vowpal Wabbit is a speed-focused online learning package developed by John Langford at MS Research.
The 
