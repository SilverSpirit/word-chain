Word Chain <img src="https://github.com/SilverSpirit/word-chain/blob/master/res/logo.png" height="24" width="24">
==========
A simple vocabulary building game!
The aim of the game is to chain together as long a word as possible without completing it. Words of length four or higher from the standard list of Scrabble words are valid. You lose if you complete a word.

For each turn, you play a letter that gets added to the word. If you are "challenged", you must play a full word prefixed with the current set of letters. Similarly, if you suspect the other player is bluffing, you may issue a challenge as well. If the challenged player is able to play a valid word then they win, otherwise the challenger wins.

<img align="right" width="467" height="304" src="res/word-chain-crop.gif">

E.g. 1
- You play Y
- Computer plays E
- You play A
- Computer plays R and loses

E.g. 2
- Computer plays W
- You play A
- Computer plays T
- You challenge the computer
- Computer responds with WATCH and wins.

Usage
------
Requires Python 3. Simply run main.py
