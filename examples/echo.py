"""
echo.py

This example shows how to create a commands with an argument that repeats
whatever the user says.
"""

from talkomatic import Bot, CommandParameter, RoomType, User
from talkomatic.commands import INFINITE_ARGS

bot = Bot()

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

user_messages = {}
async def update_user_messages():
    # we concatenate all the user messages into one message to send
    message = ""
    for user_message in user_messages.values():
        message += f"{user_message}\n"
    await bot.send_message(message)

@bot.command( # this is a decorator that turns the echo function into a command
    name = "echo", # the name of the command
    description = "This command repeats your message!", # the description of the command
    parameters = [ # the parameters of the command
        CommandParameter( # we want a parameter that takes any number of words in the message
            "message", # the name of the parameter
            "The message to repeat.", # the description of the parameter
            str, # the type of the parameter
            positional = True, # the parameter is positional
            required = True, # the parameter is required
            number_of_args = INFINITE_ARGS # the parameter can take any number of words
        )
    ]
)
async def echo(user: User, message) -> None:
    if not isinstance(message, list): # is the user sending a message in the /echo
        if user.id in user_messages: # if 
            del user_messages[user.id]
    else:
        # for each user, we store the message that'll be sent
        user_messages[user.id] = f"{user.username} / {user.location} said: {' '.join(message)}"

    # update the user messages
    await update_user_messages()

@bot.on_user_leave
async def on_user_leave(user: User) -> None:
    if user.id in user_messages: # if they're in one of our user messages dictionary
        del user_messages[user.id] # when a user leaves, we delete them from the user messages
    
    # update the user messages
    await update_user_messages()
    
# we can even make a "hidden" command that doesn't show up in the /help command
@bot.command(name = "ping", hidden = True)
async def ping(user: User) -> None:
    # we can make little easter eggs with this hidden command feature!
    await bot.send_message("Pong!")


bot.run("Echo Bot", "do /help", create_help_command = True) # we let the bot create the help command automatically
