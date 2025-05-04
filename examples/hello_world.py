"""
hello_world.py

This example shows how to make a bot that joins all the rooms in the lobby,
and messages "Hello, world!" to all rooms.
"""


from talkomatic import Bot, RoomType # import the Bot, RoomType class from the talkomatic package


bot = Bot() # create a new Bot instance

# with this decorator, the function will be called when the bot finishes connecting to the server
@bot.on_connect
async def on_connect() -> None:
    # we find the first non-full public room, we join it, and say "Hello, world!"
    for room in bot.rooms:
        if not room.is_full and room.room_type == RoomType.PUBLIC:
            await bot.join_room(room)
            return
    print("We didn't find any non-full rooms to join. :(") # :(
    await bot.disconnect()

@bot.on_room_join
async def on_room_join(*args) -> None: # we can put *args because we don't care about the arguments here
    await bot.send_message("Hello, world!") # when we have joined a room, we send the message!

# we're ready to go! let's run the bot with a username and location
bot.run("Hello", "world!")
# this'll keep running until you halt the program with ctrl+c!
