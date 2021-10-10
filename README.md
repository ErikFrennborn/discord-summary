# Discord summary

A tool for for getting and summary of your discord conversations, it will stat on who writes what.
This is just a toy project but you might get some use from it. As such it's not optimist so it's a bit slow.

## Installation/usage

Requires python >= 3.9 and [discord-chat-exporter-cli](https://github.com/Tyrrrz/DiscordChatExporter)

1. Pull that repo.
2. Set environment variable `DISCORD_TOKEN` to your discord token.
3. Get the id of the DM or server channel.
4. Call `python3 main.py <Channel id>`, could recommend redirecting the output to a file.

## Example

This an example the output

```
Total number of messages: 7371

Number of messages:
<user1> 50% (3694)
<user2> 50% (3677)

Number of words:
<user2> 51% (19068)
<user1> 49% (18630)

Number of links:
<user1> 68% (174)
<user2> 32% (82)

Number of edits:
<user1> 98% (87)
<user2> 2% (2)

Number of attachments:
<user1> 54% (110)
<user2> 46% (93)

Number of unique words:
<user1> 55% (4100)
<user2> 45% (3366)

Number of letters:
<user2> 51% (77120)
<user1> 49% (75081)

Average words length:
<user1> 4.03 letter/word
<user2> 4.04 letter/word

First mover (first message per day)
<user1> 77% (503)
<user2> 23% (148)

Most active date 2019-11-02 with 108 messages

Average first message time 15:8

Average message time 16:42

Words spread, who uses what words most:
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| <user1>  | 0.9     | 0.5     | 0.2      | 0.0     | -0.2       | -0.5     | -0.9     | <user2>   |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| sup?     | u       | reading | mission  | outside | me?        | btw?     | nah      | hahaha    |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| :/       | Well    | quite   | much,    | 66      | quick      | 20       | ah       | im        |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| Yeah,    | Alright | friend  | forward  | war     | shops      | own      | gotta    | lmao      |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| FCB      | nw      | crash   | error    | date    | buy        | so?      | practice | okay      |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| Alright, | min     | break   | early    | 128     | understand | were     | its      | ive       |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| Nw       | someone | day?    | Which    | 176     | sadly      | he's     | man      | oh        |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| Btw      | ?       | offline | page     | hand?   | watching   | weekend  | nothing  | i've      |
|----------|---------|---------|----------|---------|------------|----------|----------|-----------|
| h        | Have    | go?     | Still    | called  | old        | internet | bass     | probs     |
|__________|_________|_________|__________|_________|____________|__________|__________|___________|

50 most common words:
Growing right then down
a, to, the, you, I, that, it, and, yo, in,
for, just, be, of, on, my, i, is, have, some,
I'm, lol, so, was, not, but, do, good, got, with,
yeah, call, haha, Started, lasted, minutes., sorry, if, will, me,
can, up, at, no, are, man, we, this, like, about,


```

## Contribution

If you want contribute it would most welcome, please a pull request to master and I will look at it as soon as I can. Please explain what and why you did and keep consistent code style. Thanks in advance.

Somethings that can be improved, if you want some pointers:

- Improved speed by not iterate through all message for each query.
- Make it work on entire servers.
- Add more interest queries.
