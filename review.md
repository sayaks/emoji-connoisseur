docstrings!

**backend_creator:**

You do go beyond 80 characters in some lines, mostly comments.

it's not entirely clear to me at this point how print_status is supposed to be used

`print('\n' + status_message + '...', end=' ')` why not just `end=''`?

don't comment out code when you're using vcs >:c
(at least don't commit the commented code)

ok i can understand from the way it's used how to use print_status

in add_bot_to_guilds there are several lines that are too long

the rest of the code is fairly self-explanatory when you read it, docstrings would however make it easier to understand

**db.py:**
you don't explain the SQL at all, and i'm not sure if you should assume that everyone reading this should know SQL.

**utils.py:**
it's good you have a docstring, but i'd like it if it told me why you have the function 
and how it should be used.

**cogs/meta.py:**
looks good apart from lacking documentation, which makes it hard to know what it's supposed to do
