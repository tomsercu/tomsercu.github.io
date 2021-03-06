---
title:  "Bias-Trainability tradeoff in Martial Arts: a model for RL."
category: blog
tags: [perspective, machine-learning, sports]
tweet: "https://twitter.com/TomSercu/status/1038938428652617728"
---

I started training Judo / Brazilian Jiu-Jitsu about a year ago.
Different styles of sport martial arts (combat sports) generalize better or worse to real self-defense situations,
with an interesting and counter intuitive relation to the constraints on the sport: more constrained grappling sports like BJJ
can generalize better.
I will call this the *Bias-Trainability tradeoff*, in analogy to the Bias-Variance tradeoff in supervised machine learning.
This tradeoff can be relevant to Reinforcement Learning (RL):
athletes are RL agents whose optimization is so good it's probably not the bottleneck.
So we can look at martial arts to learn how changing the rules/environment/reward influences the optimal policy.

# The rules make the sport
One of the most important differentiators between different sport martial arts are the rules:
what defines a Knock Out (KO) or KO substitute, how you get score (in case the fight doesn't end with KO),
what is not allowed in terms of attacks (in order for it to be a sport),
and some rules how stalling is avoided (to make sure there is actually something interesting to watch).

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
Martial arts is very close to an RL agent trained with self-play, afaik 
[invented by my IBM colleague Gerry Tesauro](https://www.ibm.com/developerworks/library/cc-reinforcement-learning-train-software-agent/index.html) in 1992,
and also a pillar of the [OpenAI research agenda](https://blog.openai.com/competitive-self-play).
Athletes are optimizing their skills (motoric control or "policy"), and even their bodies, to maximize reward: winning against other athletes.
Instead of your classical RL methods to optimize the agent though,
the optimization is executed by schools of athletes, and is complex but probably very good.
It checks all fancy boxes: curriculum learning, evolutionary search strategies (successful athletes get copied by others),
hierarchical RL (you learn individual techniques first, then how to string them together),
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
The bias also manifests as each sport looking completely different from the others.

Now the bias-variance tradeoff in supervised classification is the observation that a lower-bias classifier typically
has higher variance: it is more sensitive to fluctuations in the training set, leading to overfitting and thus bad generalization.
Now do we have an equivalent in martial arts / self-play RL?
I'd argue that there is a bias-trainability tradeoff:
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
So how do all those martial arts styles measure up against each other?
That's the question that was driving early MMA competitions like UFC 1 and PRIDE FC.
In broad strokes, most people expected striking sports like boxing, kick boxing and variations to be dominant.
Surprisingly, BJJ athletes saw very significant wins in those early tournaments, using almost exclusively pure BJJ techniques
(specifically Royce Gracie winning in UFC 1,2, and 4).
This was very unexpected - he was not trained in using any kind of kicking or punching - only the "soft" BJJ rules!
In contrast, some more "spectacular" martial arts like karate, kung fu, and taekwondo were basically useless on the MMA mat.
I'd argue this confirms the bias-trainability trade-off hypothesis:
the techniques and systems that were developed under a very constrained ruleset, but therefore trained under real pressure,
hold up against open rules tournaments and thus generalize to real martial / self-defense situations.

Currently the norm is cross-training: athletes from grappling backgrounds train also in striking sports, and vice versa.
Maybe this is like multi-task RL, where training in different but related tasks can help performance in either 
(1) the original objective task, (2) generalization to new tasks (new ruleset).
Heh maybe I'll keep that idea for another post ;)

# Conclusions for RL
* Look at 1-on-1 competitive sports as a model for RL self-play, where we can assume the learning/optimization is not the bottleneck.
* Higher bias, more constrained environment or ruleset can lead to better generalization - it's not just a losing game.
   More constrained rulesets allow the development of complex techniques (complex policy) which can be optimized
   so well that they generalize: the complex techniques become viable when the constrained ruleset falls away.
* The concept of trainability could be extended!
    - In combat sports: by limitation of injury, it is not possible to train all techniques at full resistance.
    - In RL agent: more general environment/reward setups could be computationally much more expensive,
        harder to optimize, imply longer traces with sparser reward signal.
        More constrained environment/reward setup can provide more experience within the same computational budget.
    - In robotics some constraints on the policy or reward are typically necessary to avoid damage to the robot.
* Part of the high bias ruleset is introducing a proxy KO in combat sports: instead of actually needing to knock your opponent out,
    a soft alternative is introduced (submissions: chokes or joint locks).
    This suggests designing proxy rewards for RL agents which are easier to achieve and don't drive the agent into the untrainable regime.
