Working in open source: part 1
##############################

:date: 2018-06-15T16:08+02:00

Three years ago on this day I joined Collabora_ to work on free software full-time. It still feels a bit like yesterday, despite so much time passing since then. In this post, I’m going to reconstruct the events of that year.

Back in 2015, I worked for Alcatel-Lucent, who had a branch in Bratislava. I can’t say I didn’t like my job — quite contrary, I found it quite exciting: I worked with mobile technologies such as 3G and LTE, I had really knowledgeable and smart colleagues, and it was the first ‘real’ job (not counting the small business my father and I ran) where using Linux for development was not only not frowned upon, but was a mandatory part of the standard workflow, and running it on your workstation was common too, even though not official.

However, after working for Alcatel-Lucent for a year, I found I don’t like some of the things about this job. We developed proprietary software for the routers and gateways the company produced, and despite the fact we used quite a lot of open source libraries and free software tools, we very rarely contributed anything back, and if this happened at all, it usually happened unofficially and not on the company’s time. Each time I tried to suggest we need to upstream our local changes so that we don’t have to maintain three different patchsets for different upstream versions ourselves, I was told I know nothing about how the business works, and that doing that would give up the control on the code, and we can’t do that. At the same time, we had no issue incorporating permissively-licensed free software code. The more I worked at Alcatel-Lucent, the more I felt I am just getting useless knowledge of a proprietary product I will never be able to reuse once and if I leave the company. At some point, in a discussion at work someone said that doing software development (including my free software work) even on my free time may constitute a conflict of interests, and the company may be unhappy about it. Add to that that despite relatively flexible hours, working from home was almost never allowed, as was working from other offices of the company.

These were the major reasons I quit my job at Alcatel-Lucent, and my last day was 10 April 2018. Luckily, we reached an agreement that I will still get my normal pay while on the notice period despite not actually going to the office or doing any work, which allowed me to enjoy two months of working on my hobby projects while not having to worry about money.

To be honest, I don’t want to seem like I quit my job just because it was all proprietary software, and I did plan to live from donations or something, it wasn’t quite like that. While still working for Alcatel-Lucent, I was offered a job which was developing real-time software running *inside* the Linux kernel. While I have declined this job offer, mostly because it was a small company with less than a dozen employees, and I would need to take over the responsibility for a huge piece of code — which was, in fact, also proprietary, this job offer taught me this thing: there were jobs out there where my knowledge of Linux was of an actual use, even in the city I lived in. The other thing I learnt was this: there were remote Linux jobs too, but I needed to become self-employed to be able to take them, since my immigration status at the moment didn’t allow me to be employed abroad.

.. figure:: /images/posts/business-license.jpg
   :class: img-responsive
   :alt: Picture of the business license. Text in Slovak: ‘Osvedčenie o živnostenskom opravnení. Andrei Shadura’.

   The business license I received within a few days of quitting my job


Feeling free as a bird, having the business registered, I’ve spent two months hacking, relaxing, travelling to places in Slovakia and Ukraine, and thinking about how am I going to earn money when my two months vacation ends.

.. figure:: /images/posts/trencin.jpg
   :class: img-responsive
   :alt: A street in Trenčín; the castle can be seen above the building’s roof.

   In Trenčín

The obvious idea was to consult, but that wouldn’t guarantee me constant income. I could consult on Debian or Linux in general, or on version control systems — in 2015 I was an active member of the `Kallithea project`_ and I believed I could help companies migrate from CVS and Subversion to Mercurial and Git hosted internally on Kallithea. (I’ve actually also got a job offer from Unity Technologies to hack on Kallithea and related tools, but I had to decline it since it would require moving to Copenhagen, which I wasn’t ready for, despite liking the place when I visited them in May 2015.)

Another obvious idea was working for Red Hat, but knowing how slow their HR department was, I didn’t put too much hope into it. Besides, when I contacted them, they said they need to get an approval for me to work for them remotely and as a self-employed, lowering my chances on getting a job there without having to relocate to Brno or elsewhere.

At some point, reading Debian Planet, I found `a blog post by Simon McVittie`_ on polkit, in which he mentioned Collabora. Soon, I applied, had my interviews and a job offer.

*To be continued later…*

.. _Collabora: https://www.collabora.com/
.. _`Kallithea project`: https://kallithea-scm.org/
.. _`a blog post by Simon McVittie`: http://smcv.pseudorandom.co.uk/2015/why_polkit/
