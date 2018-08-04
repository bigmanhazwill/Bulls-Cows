# Bulls-Cows
Creating a simple version of the old fashioned Bulls and Cows game

# How the Game Works
This is an old game for two players, often played with paper and pen. Modern version is also known as Mastermind.

First player, say Harry - chooses a secret 4-digit code (like 3241).

The second player, let it be Paul - makes several attempts to guess this code. She can offer any combinations of 4 digits - and for each attempt the Harry should give a hint if incorrect.

The hint consists of two values:

first tells how many digits are guessed correctly and are in correct positions;
second tells how many digits are guessed correctly but are in wrong positions.
For example, if the secret value is 3241 and Barbara's guess is 2673 - Alice should answer with 0-2.
And if the guess is 0847, then the hint would be 1-0.

# How to Play
Both players begin initially by giving their name.

The first player then will give their secret Key, it is then player 2's go to try and guess the key.
Guesses are made 1 at a time, and after each guess a hint is given. 

When the correct key is guessed a congratulations message is displayed telling you how many guesses it took you.
