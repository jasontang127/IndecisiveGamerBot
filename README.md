IndecisiveGamerBot
====== 

This project is a basic Discord bot used for a small group of indecisive friends. A variation of this program is also being used for the Parkour and Freerunning Club at UMD's Discord server, dubbed IndecisiveMonkeBot.

### How it works
* Coded in Python and uses the discord package to read user messages
* Hosted on an AWS Virtual Machine to run 24/7 (or as long as possible)
* Currently, I am the only one able to invite the bot to servers

### Features
Given certain text commands, the bot can:
* ^decide: decides on a random item from a pre-populated list of items, in this case games
* ^pick(a,b,c, ...): decides on a random item from the given inputs, separated by commas
* ^random(a,b): selects a random number between a and b (or 0 and a if b is not provided)
* ^order(a,b,c, ...): returns a random ordering of the given items, separated by commas
* ^help: lists out all commands
