import random

import discord

token = "OTk1ODYyNjc3Mzc5MzcxMDE5.GZUWyV.aLcKMQO5gvclvf6iHKyQ4TCIwmxEFdYUi0toiA"

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})');

    if message.author == client.user:
        return
    elif user_message.lower() == "^decide":
        num = random.randrange(0, 5, 1)
        games = ["League of Legussy", "Valussy", "Fall Gussy", "Overcussy(2)", "Unrussy",
                 "nothing; be productivussy"]
        await message.channel.send(f"Foolish indecisive gamers, you will be playing " + games[num] + "!!!")
        return
    elif user_message.lower()[0:5] == "^pick":
        choices = user_message.lower()[5:].strip().split(",")
        num = random.randrange(0, len(choices), 1)
        await message.channel.send(
            f"Foolish slightly decisive gamers, you will be playing " + choices[num].strip() + "!!!")
        return
    elif user_message.lower()[0:6] == "^order":
        choices = user_message.lower()[6:].strip().split(",")
        messageStr = ""
        while len(choices) > 0:
            num = random.randrange(0, len(choices), 1)
            messageStr += str(choices[num]) + ", "
            choices.pop(num)
        await message.channel.send(
            f"Foolish indecisive gamers, here is your random order of items: " + messageStr.strip(', ') + "!!!")
        return
    elif user_message.lower()[0:7] == "^random":
        bounds = user_message.lower()[7:].strip().split(",")
        messageStr = "Your indecisive random number is: "
        if len(bounds) == 1:
            messageStr += str(random.randrange(0, int(bounds[0])) + 1) + "ussy"
        elif len(bounds) > 2:
            messageStr = "No indecisive random number for you because you're foolish and put in too many parameters";
        else:
            messageStr += str(random.randrange(int(bounds[0]), int(bounds[1]))) + "ussy"
        await message.channel.send(messageStr)
        return;
    elif user_message.lower() == "^help":
        await message.channel.send(
            f"Foolish indecisive gamers, here are my commandussys:\n- ^decide: Selects from a set list of games\n- ^pick (a, b, c): Selects from given parameters (separate with commas)\n- ^random (a,b): Selects a random number between a and b (or 0 and a if b not given)'\n- ^order (a,b,c): Returns a random ordering of given items (separate with commas)")
        return;


client.run(token);
