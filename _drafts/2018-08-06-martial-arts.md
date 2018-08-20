---
title:  "Bias-Trainability trade off in Martial Arts as a constrained optimization problem."
category: blog
tags: [perspective, machine-learning, sports]
---

I started training Judo / Brazilian Jiu-Jitsu about a year ago,
and realized the different branches of sport Martial Arts (combat sports) 
represent a variation of the Bias-Variance trade-off, which I will call the *Bias-Trainability trade-off*.
I may or may not come to some conclusion which is relevant for self-play RL and ML in general.

# The rules make the sport
One of the most important differentiators between different sport martial arts are the rules:
what defines a Knock Out (KO) or KO substitute, how you get score (in case the fight doesn't end with KO),
what is not allowed in terms of attacks (in order for it to be a sport),
and some rules how stalling is avoided (to make sure there is actually something happening).

For example in Taekwondo, which has a [quite artificial ruleset](https://www.youtube.com/watch?v=7-iIq3ikA3M),
it's all about kicking for points: straight torso kick (2pt), rotating torso kick (3pt), head kick (3pt), rotating head kick (4pt).
Punching in the torso isn't worth much (1pt) and punching the head is a total no-no.
Penalties are awarded for most other stuff you can think of like anything below the waist,
grabbing or pushing your opponent, being on the ground, etc.

Boxing has a simple ruleset, only closed fist punches above the waist are allowed,
and a win is usually defined by KO, though there is a jury based scoring system and
technical KO (for example giving up by the boxer or his/her team).
So: no kicks, no grabs, no pushing.

Judo and Brazilian jiu-jitsu (BJJ) have a very different ruleset, where no kicks or punches are allowed and 
most of the game is about grabbing onto your opponent and throwing or submitting them.
In Judo, ippon is a KO substitute: a perfect throw where your opponent lands flat in their back.
If no ippon, then the match would continue on the ground with grappling, and another KO substitute
here is a submission (typically a joint lock or chokehold), where the opponent has to tap (give up).
In BJJ, no KO is awarded for perfect throws, only for submissions - causing the sport to develop mostly
ground grappling.
Freestyle wrestling has a ruleset [similar to Judo](https://en.wikipedia.org/wiki/Freestyle_wrestling#Victory_conditions),
where KO is defined by a perfect fall, somewhat similar to a throw and short pin in Judo.

Since BJJ developed as a subset from Judo, and Judo developed as a subset of Jujutsu (which includes some
striking, kicking, and short weapons), we could wonder what advantage BJJ could possibly have over its ancestors?
We'll come back to that question later.


<!--
TODO add wrestling and oldskool Jiu Jitsu?
-->


# Generalization - MMA
Each of these sports exist and are interesting of their own right, totally independent of whether or not they are 
useful in a real self-defense / martial situation.
However if you spend all that time training a sport martial art, it is kind of nice to know that
it is useful if you ever got into a self-defense situation.
So let us define generalization as
*usefulness of a sport martial art in a self-defense situation, where the sport rules do not apply*.

Probably the best way to measure generalization is to look at MMA (Mixed Martial Arts),
which has almost no rules and was conceived as a way to pitch the different sport martial arts against each other
to see which comes out on top.

# Martial arts = self-play RL.
<!--We can understand martial arts disciplines as optimizing a motor control policy under a ruleset.-->
Martial arts is very close to an RL agent training with self-play.
Athletes are optimizing their skills or "policy" (and even their body) to maximize reward (winning against other athletes).
Instead of your classical RL methods to optimize the agent though,
the optimization is executed by schools of athletes, and is complex but probably very good.
It checks all fancy boxes: curriculum learning, evolutionary search strategies (successful athletes get copied by others),
feedback from teachers to students in a dojo, etc.
So I think it is fair to assume the optimization of the policy is as good as we can expect it to be.
This means we can **look at martial arts and learn about self-play RL agents where optimization is not a bottleneck**.

# Bias-Trainability trade off
{% comment %} ?BIAS=?? the constraints on the viable policies introduced by the ruleset. {% endcomment %}
Let us now define the bias of a martial art as **the difference between an optimal strategy under the ruleset and the optimal strategy without rules**.
This is very similar to the bias in a supervised classification problem: a classfier with restrictive assumptions
allows for an optimal classifier that is biased away from the true optimal classifier.
In martial arts this bias is very significant: techniques and strategies from one sport martial art
usually do not at all apply to another, or they would be very ineffective.
The bias also manifests as each sport looking completely different from each other because of its rules.

The bias-trainability trade off is the observation that
**martial arts with more bias (more restrictive rulesets) can allow for better training, achieving better generalization.**

This is surprisingly similar to the bias variance trade off in supervised classification, although the cause is subtly different.
* In bias-variance trade off (supervised classifiers), the poor performance of low-bias classifiers is caused
by the finite training sample classifier being way off the optimal classifier, due to the flexibility of the hypothesis class.
* In bias-trainability trade off (martial arts), the poor performance of low-bias martial arts is caused
by **impossibility to train at full force**.
Specifically, a no-rule street fight situation typically ends with significant injury.
Even training for MMA doesn't happen at full force; the actual tournaments are typically the only moment
MMA fighters go at that level, again because some injury is the norm here.

# Observations from history
* Taekwondo, kung fu, aikido: basically useless
* Simpler ruleset striking sport (boxing, kick boxing, muay thai) were the default styles
* Surprisingly BJJ had significant wins (UFC 1,2,4).
* Currently: cross training; i.e. switching rulesets
    - "switching" on longer timescales, on short timescales techniques from either one of the disciplines is dominant.

Originally

# Conclusions for RL
* Trainability: 
    - by limitation of injury, not possible to train techniques at full pressure.
    - In RL agent: computational, longer games, more experience within the same computational budget / play time.
    - Robotics: damage by overactuation.
* Higher bias, more constrained environment or ruleset can lead to better generalization - it's not just a losing game.
   More constrained rulesets allow the development of complex techniques (complex policy) which can be optimized
   so well that they become viable when the constrained ruleset falls away.
* 
