---
title: "Tom Sercu"
layout: default
order: 1
---
![Mug shot]({{ site.url }}/assets/9016_small_2.jpg)
{: .floatrightbox}

I am a co-founder and the VP of Engineering at [EvolutionaryScale](https://evolutionaryscale.ai),
a research company at the intersection of artificial intelligence and biology.
Our mission is to develop artificial intelligence (AI) to understand biology for the benefit of human health and society,
through open, safe, and responsible research, and in partnership with the scientific community.
We develop biological AI models at the frontier of scale and capabilities to enable solving
the hardest problems in the life sciences.

Before EvolutionaryScale, I was co-leading the protein team at 
Meta AI (FAIR)  in NYC, where we developed the first transformer protein language model ESM-1,
followed by ESM-1b, ESM2, ESMFold and the [ESM Atlas resource](https://esmatlas.com).
Before Meta, I was at IBM Research in the TJ Watson Research Center.
I graduated from the MS in Data Science at New York University
and hold a B.Sc./M.Sc. in Engineering Physics from Ghent University.

My past work has covered several areas of deep learning research, including
learning representations and generative models for proteins and peptides,
unsupervised learning, and semi-supervised learning with small amounts of labeled data.
I worked on Generative Adversarial Networks (GANs) and VAEs, precursors to the current "generative AI" methods.
I worked on multimodal learning: learning models across different data modalities like images, text, and speech.
And I started my research career working on deep learning approaches to acoustic modeling in speech recognition,
bringing advances from the deep learning and computer vision communities to speech recognition.


# Publications
Please see my  [google scholar](https://scholar.google.com/citations?user=FMJePIUAAAAJ) profile
since this list inevitably goes stale.

This is a selection of my most relevant and recent academic papers.
[I provide a full list here.](pubs)

{% assign postlist = site.categories["pubs"] | where: "selected",true %} 
{% include indexlist.html postlist=postlist postcategory="pubs" %}

