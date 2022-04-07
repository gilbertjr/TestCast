import discord, platform, socket, random
from discord.ext import commands

import os

bot_token = os.environ['bot_token']

bot = commands.Bot(command_prefix='cast.')

users = []

valueList = []

Client = commands.Bot(commands.when_mentioned_or('...'))


@Client.command(pass_context=True)
async def ping_ms(ctx):
    t = await Client.say('Pong!')
    ms = (t.timestamp - ctx.message.timestamp).total_seconds() * 1000
    await Client.edit_message(t,
                              new_content='Pong! Took: {}ms'.format(int(ms)))


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


print(extract_ip())


@bot.command()
async def commands(ctx):
    await ctx.send(
        "Commands are:\nmyping (W.I.P)\nsimping\ncommunity\nnope\nreminder\nping\nroll\npull\nnewpull"
    )


@bot.command()
async def myping(ctx):
    await ctx.send(ping_ms)


@bot.command()
async def simping(ctx):
    await ctx.send('~~**You naughty Wackers Bonkers**~~')


@bot.command()
async def community(ctx):
    await ctx.send('*Ha! Gaaaaayyyyyy!*')


@bot.command()
async def nope(ctx):
    await ctx.send('**Please treat each other with respect! Thanks!**')


@bot.command()
async def reminder(ctx):
    await ctx.send(
        'Here in the Server we will work with collaboration, equity, and also respect amongst others. This is a server to help, not to be messed with on.'
    )


@bot.command()
async def roll(ctx, arg):
    await ctx.send('rolling.. {0}'.format(rollCall(arg)))


@bot.command()
async def pull(ctx, arg=3):
    pullResult = 'pulling {0} times..  result: {1}'.format(arg, pull(arg))
    result = '{0} {1}'.format(arg, pullResult)
    await ctx.send(result)


@bot.command()
async def newpull(ctx, arg=3):
    pullResult = 'pulling {0} times..  result: {1}'.format(arg, pullValue(arg))
    result = '{0} {1}'.format(arg, pullResult)
    await ctx.send(result)


@bot.command()
async def pullList(ctx):
    value = '{0}'.format(rollList())
    await ctx.send(value)


@bot.command()
async def addvalue(ctx):
    valueList.append(ctx)
    await ctx.send(ctx)


@bot.command()
async def replytome(ctx):
    await ctx.reply('k')


@bot.command()
async def whoami(ctx):
    # gets User object from users list by id field
    p1 = getUser(ctx.author)
    # Returns id field of User
    await ctx.reply(p1.id)


@bot.command()
async def mynameis(ctx, arg):
    # gets User object from users list by id field
    p1 = getUser(ctx.author)
    print(ctx.message.content)
    # Create field 'name' and sets value
    p1.name = arg
    # Updates User object in users list
    setUser(p1)
    # Returns name from User object
    await ctx.reply('hi ' + p1.name)


@bot.command()
async def whatismyname(ctx):
    p1 = getUser(ctx.author)
    await ctx.reply('your name is ' + p1.name)


@bot.command()
async def getmypoints(ctx):
    user = getUser(ctx.author)
    await ctx.reply('you have ' + str(user.points) + ' points')


@bot.command()
async def setmypoints(ctx, arg):
    user = getUser(ctx.author)
    user.points = int(arg)
    setUser(user)
    await ctx.reply('your points have been set to ' + str(user.points))


@bot.command()
async def addmypoints(ctx, arg):
    user = getUser(ctx.author)
    currentPoints = user.points
    user.points = currentPoints + int(arg)
    setUser(user)
    await ctx.reply('we added ' + arg + ' points to your ' +
                    str(currentPoints) + '. your updated points value is ' +
                    str(user.points))


@bot.command()
async def evaluatepull(ctx, arg):
    evaluated = evaluateresults(arg)
    await ctx.reply("i've evaluated your responce {0}".format(evaluated))


def evaluateresults(results):
    print(results)
    if results == "❤️ ❤️ ❤️":
        return int(10)
    return int(0)

    # TODO: evalutate results of new pull


@bot.command()
async def getmyindex(ctx):
    user = getUser(ctx.author)
    # index = findUserIndex(user)
    await ctx.reply('index:' + str(user.index))


def findUser(id):
    # Find user in list by id
    for i in users:
        # Looping through all items in Users list
        if i.id == id:
            # If this User id equals the id i'm looking for, return this User
            return i
    # Return None if I get this far. It means we didn't find the User
    return None


def getUser(id):
    # Look for the user in the existing Users list.
    user = findUser(id)
    if user is not None:
        # This means: If we did find the user, then return the User
        return user
    else:
        # Otherwise create new user..
        user = User(id, len(users))
        # and add to users list
        users.append(user)
        return user


def setUser(user):
    # Updates the User object at the location where it should exist
    users[user.index] = user


def rollCall(num):
    return random.randint(0, int(num))


def rollList():
    enumList = ['❤️', '♠', '♣️', '♦️', '🎮', '+']
    minRoll = 0
    maxRoll = len(enumList) - 1
    val = 'starting roll. min:{0} max:{1} '.format(minRoll, maxRoll)
    randRoll = random.randint(minRoll, maxRoll)
    val = val + ' random roll returned {0} '.format(randRoll)
    randValue = enumList[randRoll]
    val = val + ' picked value: {0}'.format(randValue)
    print(val)
    return randValue


# Allows us to define a User to create multiple Users with the same properties
class User:
    def __init__(self, id, index):
        self.id = id
        self.index = index


def pull(num):
    numInt = int(num)
    values = ''
    # Takes in how many times to roll.
    # while x
    # values += ' ' + str(rollCall(10)
    # else:
    # return values
    if numInt == 1:
        # TODO: Find out why we can't reach here with `cast.pull 1`
        roll = rollCall(10)
        values = 'here:{0}'.format(roll)
    if numInt == 1:
        value1 = rollCall(10)
        value2 = rollCall(10)
        values = '{0} {1}'.format(value1, value2)

    else:
        value1 = rollCall(10)
        value2 = rollCall(10)
        value3 = rollCall(10)

        values = '{0} {1} {2}'.format(value1, value2, value3)
    # Return values
    return values


def pullValue(num):
    numInt = int(num)
    values = ''
    # Takes in how many times to roll.
    # while x
    # values += ' ' + str(rollCall(10)
    # else:
    # return values
    if numInt == 1:
        # TODO: Find out why we can't reach here with `cast pull 1`
        roll = rollList()
        values = 'here:{0}'.format(roll)
    if numInt == 2:
        value1 = rollList()
        value2 = rollList()
        values = '{0} {1}'.format(value1, value2)
    else:
        value1 = rollList()
        value2 = rollList()
        value3 = rollList()

        values = '{0} {1} {2}'.format(value1, value2, value3)
    # Return values
    return values


print('starting...')
bot.run(bot_token)

# TODO: Slot machine
# 1. Pull three results - ✔️
# 2. Add an enum for results (ex: Hearts, Spades, Club, Diamond) - ✔️
# 3. Add the enum to be returned on pull.
# 4. Add probability to each enum element. Check out random.choices()
# 5. Points system
