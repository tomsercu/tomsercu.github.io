---
title: "Advances in Very Deep Convolutional Neural Networks for LVCSR"
author: "Tom Sercu, Vaibhava Goel"
journal: "Proc Interspeech"
year: 2016
arxiv: "1604.01792"
shortname: sercu2016advances
thumbnail: /assets/paper_thumbs/sercu2016advances.png
excerpt: ""
abstract: >
    Very deep CNNs with small 3x3 kernels have recently been shown to achieve
    very strong performance as acoustic models in hybrid NN-HMM speech recognition
    systems. In this paper we investigate how to efficiently scale these models to
    larger datasets. Specifically, we address the design choice of pooling and
    padding along the time dimension which renders convolutional evaluation of
    sequences highly inefficient. We propose a new CNN design without timepadding
    and without timepooling, which is slightly suboptimal for accuracy, but has two
    significant advantages: it enables sequence training and deployment by allowing
    efficient convolutional evaluation of full utterances, and, it allows for batch
    normalization to be straightforwardly adopted to CNNs on sequence data. Through
    batch normalization, we recover the lost peformance from removing the
    time-pooling, while keeping the benefit of efficient convolutional evaluation.
    We demonstrate the performance of our models both on larger scale data than
    before, and after sequence training. Our very deep CNN model sequence trained
    on the 2000h switchboard dataset obtains 9.4 word error rate on the Hub5
    test-set, matching with a single model the performance of the 2015 IBM system
    combination, which was the previous best published result.
selected: false
category: pubs
---
