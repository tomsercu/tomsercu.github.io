---
title:  "Bias-Trainability tradeoff in Martial Arts as a model for self-play Reinforcement Learning."
category: blog
tags: [perspective, machine-learning, sports]
---

I started training Judo / Brazilian Jiu-Jitsu about a year ago,
and realized the different branches of sport Martial Arts (combat sports) 
represent a variation of the Bias-Variance tradeoff, which I will call the *Bias-Trainability tradeoff*.
This observation could be relevant to Reinforcement Learning (RL) since 
martial arts are closely related to self-play RL,
where we trust the optimization to be very good since it's done by humans.

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

Probably one of the best ways to measure generalization is to look at MMA (Mixed Martial Arts),
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

# Bias-Trainability tradeoff
{% comment %} ?BIAS=?? the constraints on the viable policies introduced by the ruleset. {% endcomment %}
The bias is basically the effect the rules (constraints) have on the sport.
We could define the bias of a martial art as **the difference between an optimal strategy under the ruleset and the optimal strategy without rules**.
<!--Or, the difference between a top athlete in a sport and a top fighter in no-rules competition.-->
This is very similar to the bias in a supervised classification problem: a classfier with restrictive assumptions
will have an optimal classifier that is biased away from the true optimal classifier.
In martial arts this bias is very significant: techniques and strategies from one sport martial art
usually do not at all apply to another, or they would be very ineffective.
The bias also manifests as each sport looking completely different from each other because of its rules.

Now the bias-variance tradeoff in supervised classification is the observation that a lower-bias classifier typically
has higher variance caused by fluctuations in the training set, leading to overfitting and thus bad generalization.
Now do we have an equivalent in martial arts / self-play RL?
The bias-trainability tradeoff is the observation that
**martial arts with more bias (more restrictive rulesets) can allow for better training, achieving better generalization.**

This is surprisingly similar to the bias-variance tradeoff in supervised classification, although the cause is subtly different.
* In bias-variance tradeoff (supervised classifiers), the poor performance of low-bias classifiers is caused
by the finite training sample classifier being way off the optimal classifier, due to the flexibility of the hypothesis class.
* In bias-trainability tradeoff (martial arts), the poor performance of low-bias martial arts is caused
by **impossibility to train at full resistance** because of injury.

<!--Specifically, a no-rule fight typically ends with significant injury.-->
<!--Even training for MMA doesn't happen at full force; the actual tournaments are typically the only moment-->
<!--MMA fighters go at that level, again because some injury is the norm here.-->
Looking at the way most punching and kicking based martial arts are trained, most time is spent
either punching or kicking a ball or a pad.
Weapon based martial arts will probably spend most of their time just training techniques in the air without any kind of resistance.
Karate and other sports use an artificial shadow fighting concept of just barely touching an opponent. 
Even during sparring some safeguards are put in place.
In contrast, with restrictive rulesets like BJJ or Judo, an athlete can train at full force,
with real resistance, during everyday training, without risk of injury.
It's crucial here that no punching or kicking techniques are allowed, and that KO is replaced by a softer proxy (tapping out).
This sparring against real resistance makes a huge difference for the level at which the sport can be trained and practiced.

# Observations from MMA
* Taekwondo, kung fu, aikido: basically useless
* Simpler ruleset striking sport (boxing, kick boxing, muay thai) were the default styles
* Surprisingly BJJ had significant wins (UFC 1,2,4).
* Currently: cross training; i.e. switching rulesets
    - "switching" on longer timescales, on short timescales techniques from either one of the disciplines is dominant.

So how do all those martial arts styles measure up against each other?
That's the question that was driving early MMA competitions like UFC 1 and PRIDE FC.
In broad strokes, most people expected striking sports like boxing, kick boxing and variations to be dominant.
Surprisingly, BJJ athletes saw very significant wins in those early tournaments, using almost exclusively pure BJJ techniques
(specifically Royce Gracie winning in UFC 1,2, and 4).
This was very unexpected - he was not trained in using any kind of kicking or punching - only the "soft" BJJ rules!
In contrast, some more "spectacular" martial arts like karate, kung fu, and taekwondo were basically useless on the MMA mat.
This confirms that the techniques and systems that are developed under constrained ruleset, and trained under real pressure,
hold up against open rules tournaments and thus generalize to real martial / self-defense situations.

Currently the norm is cross-training: athletes from grappling backgrounds train also in striking sports, and vice versa.
This is like multi-task RL, where training in different but related tasks can help performance in either 
(1) the original objective task, (2) generalization to new tasks (new ruleset).

# Conclusions for RL
* Look at 1-on-1 competitive sports as a model for RL self-play, where we can trust the learning/optimization is not the bottleneck.
* The concept of trainability can be extended: 
    - In combat sports: by limitation of injury, it is not possible to train all techniques at full resistance.
    - In RL agent: more general environment/reward setups could be computationally much more expensive,
        harder to optimize, imply longer traces with sparser reward signal.
        More constrained environment/reward setup can provide more experience within the same computational budget.
    - In robotics some constraints on the policy or reward are typically necessary to avoid damage to the robot.
* Higher bias, more constrained environment or ruleset can lead to better generalization - it's not just a losing game.
   More constrained rulesets allow the development of complex techniques (complex policy) which can be optimized
   so well that they generalize: the complex techniques become viable when the constrained ruleset falls away.
* Part of the high bias ruleset is introducing a proxy KO in combat sports: instead of actually needing to knock your opponent out,
    a soft alternative is introduced (submissions: chokes or joint locks).
    This suggests designing proxy rewards for RL agents which are easier to achieve and don't drive the agent into the untrainable regime.
