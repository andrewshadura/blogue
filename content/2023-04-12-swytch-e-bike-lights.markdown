---
layout: post
title: Connecting lights to a Swytch e-bike kit
date: 2023-04-12 15:09:46 CET
comments: true
slug: swytch-e-bike-lights
image: /images/posts/2023-04/favorit-front.jpg
---

Last year I purchased an e-bike upgrade kit for my mother in law. We decided to install it on a bicycle she originally bought back in the 80s, which I fixed and refurbished a couple of years ago and used until September 2022 when I bought myself a Dutch Cortina U4.

When I used this bicycle, I installed a lightweight Shutter Precision dynamo hub and compatible lights, XLC at the front, Büchel at the back. Unfortunately, since Swytch is a front wheel with a built-in electric motor, these lights don’t have a dynamo to connect to anymore, and Swytch doesn’t have a dedicated connector for lights. I tried asking the manufacturer for more documentation or schematics, but they refused to do so.

Luckily, a Canadian member of the Pedelecs forum managed to [reverse-engineer the Swytch connector pinouts](https://www.pedelecs.co.uk/forum/threads/should-we-bail-on-the-new-swytch-conversion-kit.43298/#post-650290), which gave me an idea on how to proceed. Unfortunately, that meant that I had to replace both lights, and by trial and error I found specific models that worked. Before the Axa lights, I also tried Büchel’s Tivoli e-bike light, but it didn’t work because the voltage was too low:

{% figure img-responsive /images/thumbnails/posts/2023-04/büchel_thumbnail_wide.jpg "Büchel Tivoli light that didn’t work" "" %}

Once I knew what to do, the rest was super easy 🙂

So, here we go:

1. Get a 3-pin (yellow) **female** connector with a cable, e.g. [off AliExpress](https://www.aliexpress.com/item/4001091169417.html). Only two wires will be used, the white one is +4.2V (4-point-2, not 42!), the black one is earth. This will go into the throttle port. If you actually have a throttle, you need some sort of Y-splitter, but I don’t, so this was not an issue for me. (However, I bought both sides (M and F), just to be sure.)
   {% figure img-responsive /images/thumbnails/posts/2023-04/swytch-3pin-cable-ali_thumbnail_wide.jpg "Cable for the throttle port" "" %}


2. Purchase an [Axa 606 E6-48 front light](https://www.axasecurity.com/bike-security/en-gb/products/lights/7/92915396SC/axa-606-e6-48). The 606 comes in two versions, for dynamos and e-bikes, use the one for e-bikes; despite being officially rated as 6—48V, these lights work quite well off 4.2V too.
   {% figure img-responsive /images/thumbnails/posts/2023-04/axa-606-light_thumbnail_wide.jpg "Axa 606 E6-48 light" "" %}

3. Purchase an [Axa Spark Steady rear light](https://www.axasecurity.com/bike-security/en-gb/products/lights/7/93954895SC/axa-spark-steady-50-80mm). This light works with both AC and DC (just like the 606, the official rating is 6—48V), and works off 4.2V without an issue.
   {% figure img-responsive /images/thumbnails/posts/2023-04/axa-spark_thumbnail_wide.jpg "Axa Spark light" "" %}

4. Wire lights up. I used tiny wire terminals to join the wires, but I’m sure there are better options too. Insulate them well, make sure the red wire from the throttle connector is insulated too. I used a bunch of shrink tubes and black insulation tape. Since the voltage is not wildly different from what the dynamo hub produced (although AC, not DC), I was able to reuse the cable I had already routed to the rear carrier.

5. Lights go on automatically as soon as you touch the power button on the battery pack, and stay on until the battery pack is switched off completely. I was considering adding a handlebar switch, but since I lost the only one I had, I had to do without.

{% figure img-responsive /images/thumbnails/posts/2023-04/favorit-front_thumbnail_wide.jpg "Front light" "" %}
{% figure img-responsive /images/thumbnails/posts/2023-04/favorit-rear_thumbnail_wide.jpg "Rear light" "" %}

The side effect of using the Axa Spark at the rear is that it has a capacitor inside and keeps going for a couple more minutes after the battery pack is off — I haven’t decided whether that’s a benefit or a drawback 😄

**This post has been amended on 2023-08-18.** Previously, it incorrectly stated a cable with a male connector is necessary. However, it is the cable leading from Swytch that is male, and the matching part connecting to the lights has to be female.
