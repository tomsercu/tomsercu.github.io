---
title: "Tom Sercu"
layout: default
order: 1
---
![Mug shot]({{ site.url }}/assets/9016_small_2.jpg)
{: .floatrightbox}

I am a Research Engineer and Tech Lead Manager for the protein team at Facebook AI Research in NYC.
With the protein team, we are working to make an impact on structural biology
using state of the art methods from Artificial Intelligence.

My past research has covered several areas of machine learning / deep learning, including
learning representations and generative models for proteins and peptides,
unsupervised and semi-supervised learning with either no or very small amounts of labeled data.
I worked on Generative Adversarial Networks (GANs), specifically on finding a better distance metric
between the data distribution and the generated distribution, which leads to fast and stable training.
I worked on multimodal learning: learning representations across different data modalities like images, text, and speech.
And I started my research career working on deep learning approaches to acoustic modeling in speech recognition,
bringing advances from the deep learning and computer vision communities to speech recognition.

Before facebook, I was at IBM Research AI, in the T.J. Watson Research Center.
I graduated from the MS in Data Science at New York University's Courant Institute of Mathematical Sciences
and have a B.Sc./M.Sc. in Engineering Physics from Ghent University.

# Selected Publications
For an always-up-to-date list, see [google scholar](https://scholar.google.com/citations?user=FMJePIUAAAAJ).

{% assign postlist = site.categories["pubs"] | where: "selected",true %} 
{% include indexlist.html postlist=postlist postcategory="pubs" %}

[See more](pubs)

# Recent Talks
{% assign postlist = site.categories["talks"] | slice: 0,3 %} 
{% include indexlist.html postlist=postlist postcategory="talks" %}

[See more (full talks index)](talks)

# From my time at NYU
While at NYU, I worked as a Teaching Assistant for two courses, making the following lab material:

* [Torch tutorials](https://github.com/tomsercu/torchtutorial) and 
    [Assignment 4]({{ "/assets/A4.pdf" | absolute_url }}) (+ [solution]({{ "/assets/A4_solutions.pdf" | absolute_url }}))
    for Yann LeCun's [Deep Learning Course](http://cilvr.cs.nyu.edu/doku.php?id=courses:deeplearning2015:start) (Spring 2015).
* Course DS-GA-1007 Programming for Data Science [lab website](https://cims.nyu.edu/~ts2387/dsga1007.html) (Fall 2014).


