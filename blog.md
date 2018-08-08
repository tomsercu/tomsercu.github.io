---
title: "Blog"
permalink: /blog/
order: 2
---
I sometimes have the intention to write out some thoughts in a blog, but am rarely following through with it.
Blog posts may be of variable length and quality.

# Blog posts
{% for post in site.posts %}
- {{ post.date | date: "%Y-%m-%d" }}
  {: .post-meta }

   [{{ post.title }}]({{ post.url | prepend: site.baseurl }})
    {: .post-link }

    {: .post-excerpt }
    > &nbsp; {{ post.excerpt | remove: '<p>' | remove: '</p>' }}
    
{% endfor %}

