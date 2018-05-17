---
layout: post
title: "Say no to Slack, say yes to Matrix"
date: 2018-03-10 14:50
slug: say-no-to-slack
comments: true
---

Of all proprietary chatting systems, Slack has always seemed one of the worst to me. Not only it’s
a closed proprietary system with no sane clients, open source or not, but it not just one walled garden,
as Facebook or WhatsApp are, but a constellation of walled gardens, isolated from each other. To be able
to participate in multiple Slack communities, the user has to create multiple accounts and keep multiple
chat windows open all the time. Federation? Self-hosting? Owning your data? All of those are not a thing
in Slack. Until recently, it was possible to at least keep the logs of all conversations locally by connecting
to the chat using IRC or XMPP if the gateway was enabled.

Now, with [Slack shutting down gateways](https://www.theregister.co.uk/2018/03/09/slack_cuts_ties_to_irc_and_xmpp/) not only
you cannot keep the logs on your computer, you also cannot use a client of your choice to connect to Slack. They also began
[changing the bots API](https://api.slack.com/changelog/2017-09-the-one-about-usernames) which was likely the reason
the [Matrix-to-Slack gateway didn’t work properly at times](https://github.com/matrix-org/matrix-appservice-slack/issues/65).
The issue has since resolved itself, but Slack doesn’t give any guarantees the gateway will continue working, and obviously
they aren’t really interested in keeping it working.

So, following [Gunnar Wolf’s advice](http://gwolf.org/node/4119/) (consider also reading [this article by Megan Squire](https://link.springer.com/chapter/10.1007/978-3-319-57735-7_1)), I recommend you stop using Slack. If you prefer an isolated
chat system with features Slack provides, and you can self-host, consider [Mattermost](https://about.mattermost.com/) or
[Rocket.Chat](https://rocket.chat/). Both seem to provide more or less the same features as Slack, but don’t lock you in, and
you can choose to either use their paid cloud offering, or run it on your own server. We’ve been using Mattermost at Collabora
since July last year, and while it’s not perfect, it’s not a bad piece of software.

If you woulde prefer a system you can federate, you may be interested to have a look at [Matrix](https://matrix.org/). Matrix is
an open decentralised protocol and ecosystem, which architecturally looks similar to XMPP, but uses different technologies and
offers a richer and more modern baseline, including VoIP, end-to-end encryption, decentralised history and content storage, easy
bot integration and more. The web client for Matrix, [Riot](https://riot.im/) is comparable to Slack, but unlike Slack, there are
[more clients](https://matrix.org/docs/projects/try-matrix-now.html) you can use, including Weechat, libpurple, a bunch of Qt-based
clients and, importantly, Riot for Android and iOS.

You don’t have to self-host a Matrix homeserver, since Matrix.org runs one you can use, but it’s quite easy to run one if you decide
to, and you don’t even have to migrate your existing chats — you just join them from accounts on your own homeserver, and that’s it!

To help you with the decision to move from Slack to Matrix, you should know that
since Matrix has a Slack gateway, you can gradually migrate your colleagues to the new infrastructure, by joining the Slack and Matrix chats
together, and dropping the gateway only when everyone moves from Slack.

Repeating Gunnar, *say no to predatory tactics. Say no to Embrace, Extend and Extinguish. Say no to Slack.*
