# bbc_kata2_minesweeper

The challenge is via https://codingdojo.org/kata/Minesweeper/ and is based on the classic Windows game.

Given a board spec like this:


    *...
    ....
    .*..
    ....

where `*` represents a mine, and `.` a safe, empty space, you should return a grid of the same size, with each space listing how many bombs it is next to, like this:


    *100
    2210
    1*10
    1110

As you can see, the valid characters are `*` for a mine, and the numbers `0`..`8` listing the number of adjacent mines.  Adjacency works in all 8 directions, so:


    ***
    *.*
    ***

would return


    ***
    *8*
    ***


Notes
- You MAY pass in the grid size with the input, or calculate it based on the size of the input.
- You MAY supply a command-line tool that reads the board specs from input and prints the results to output.
    - e.g. you don’t have to do this, and can simply implement a pure function if you prefer.
    - If you do input/output, you MAY want to follow the spec in the codingdojo link above, which allows for multiple grids in the same input stream.


Thoughts
- This problem may be harder than the Roman Numerals one, if you don’t have time to solve the whole problem, what’s the smallest feature you can get to work?
- As well as classic TDD, might Approvals Testing be a useful testing methodology for this kind of problem?
- Can you do this in an Object Oriented style?
- Or a Functional Programming one?
- How does the style chosen affect how you model the grid (or vice versa?)
- Can you solve the problem with just Regular Expressions / Unix commands?
