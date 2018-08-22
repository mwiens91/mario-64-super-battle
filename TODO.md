# Mario 64 Super-Star Battle todo list

## Specific

+ Show how much time a player won by; for example `matt won by
  00:42:06.9`
+ Add feature to a PDF with final results (could support other formats,
  too, like Markdown, plain text, JSON)
+ Add terminal-colour-agnostic colours to highlight players with

## Less Specific

+ Add high-coverage tests for Travis CI
+ Handle ties better
+ Create a `Round` class to store round info
+ Clean up long-winded code; one idea is to pass the `MarioBattle`
  object on to `io` functions directly
+ Add a pause feature
+ Show the time elapsed while a player is making their run

## Much less specific

+ Have results persist between different Mario battles (could host info
  on a webserver, or in a file, or ...?)
