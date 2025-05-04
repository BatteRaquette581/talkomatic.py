"""
parrot.py

This example shows how to make a bot repeating what the other users say.
"""


from talkomatic import Bot # import the Bot class from the talkomatic package


bot = Bot() # create a new Bot instance

# with this decorator, the function will be called when the bot finishes connecting to the server
@bot.on_connect
async def on_connect() -> None:
    # we find the first non-full room, and we join it
    for room in bot.rooms:
        if not room.is_full:
            await bot.join_room(room)
            break
    print("We didn't find any non-full rooms to join. :(") # :(
    await bot.disconnect()

# this function will execute when:
@bot.on_room_join     # - when the bot joins a room
@bot.on_user_message  # - when a user sends a message
@bot.on_user_join     # - when a user joins the room
@bot.on_user_leave    # - when a user leaves the room
async def send_parrot_message(*args) -> None: # we use *args here since we don't care about the arguments
    bot_message = "" # this variable will store a string of the message the bot will send
    for member in bot.current_room.users: # for each user in the bot's current room (including the bot itself)
        if member == bot.user: # if the user is the bot itself, we skip it
            continue
        member_message = bot.get_user_message(member) # we get the member's message
        bot_message += f"{member.username}: {member_message.strip()}\n" # we add the member's message to the bot's message
    
    await bot.send_message(bot_message) # we send the bot's message!

# we're ready to go! let's run the bot with a username and location
bot.run("Parrot", "Bot")
