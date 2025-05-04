"""
create_room.py

This example shows how to make a bot that creates its own room,
and then joins it.
"""


from talkomatic import Bot # import the Bot class from the talkomatic package
from talkomatic.dataclasses.room import RoomType, RoomLayoutType 
# we import the RoomType and RoomLayoutType objects to describe the room privacy type, and layout type


bot = Bot() # create a new Bot instance

# with this decorator, the function will be called when the bot finishes connecting to the server
@bot.on_connect
async def on_connect() -> None:
    # we create a room with the name "My awesome room!", it's public, and it's a horizontal layout
    await bot.create_room("My awesome room!", RoomType.PUBLIC, RoomLayoutType.HORIZONTAL)
    # when the room is created, the on_room_creation event will be called

@bot.on_room_creation
async def on_room_creation(room_id: int) -> None:
    # our awesome room has been created, so we'll join it!
    await bot.join_room(room_id)

@bot.on_room_join
async def on_room_join(*args) -> None: # we can put *args because we don't care about the arguments here
    # we joined our awesome room, and it'd be a good idea to greet our fellow users!
    await bot.send_message("""Welcome to my awesome room!

This is an automated message from a bot for the talkomatic.py library!
To the developer of the bot, remember that you can press Ctrl+C in the
terminal to disconnect your bot. :catjam:""")

# we're ready to go! let's run the bot with a username and location
bot.run("My Room", "Bot")
# this'll keep running until you halt the program with ctrl+c!
