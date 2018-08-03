---
layout: default
---
I am a Research Engineer at IBM Research AI, working in the IBM T.J. Watson Research Center in Yorktown Heights, NY.
I graduated from the MS in Data Science at New York University's Courant Institute of Mathematical Sciences in May 2015.
Before that, I obtained a B.Sc. (2011) and M.Sc. (2013) in Engineering Physics from Ghent University.
I received the Francqui Foundation Fellowship from the Belgian American Educational Foundation and
a tuition scholarship from the Center for Data Science for my studies at NYU.

My research interests include
unsupervised and semi-supervised learning with either no or very small amounts of labeled data,
multimodal learning (i.e. learning representations across different data modalities like images, text, and speech),
and learning generative models of structured data.
I also worked on deep learning approaches to acoustic modeling in speech recognition,
bringing advances from the deep learning and computer vision communities to speech recognition.
Most recently I worked on Generative Adversarial Networks (GANs), specifically on finding a better distance metric
between the data distribution and the generated distribution, which leads to fast and stable training.

## Selected Publications
For a full list, see [google scholar](https://scholar.google.com/citations?user=FMJePIUAAAAJ).

TODO use some jekyll data attributes and liquid iteration, maybe add a fold-out (read more) tag.

## Blog
[The full blog index](blog)

### Latest entries:
{% for post in site.posts limit:3 %}    
- *{{ post.date | date: "%Y-%m-%d" }}*   
   **[{{ post.title }}]({{ post.url | prepend: site.baseurl }})**
{% endfor %}

## Talks
TODO List of recent talks, also truncated with fold-out. 

## Media
TODO List of recent media pubs, also truncated with fold-out. 


