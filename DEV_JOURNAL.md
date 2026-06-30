# Healthcare Data Analytics - Developer Journal
---
## June 28, 2026

### Project: Healthcare BMI Calculator

## Reflection

Today I realized something interesting while building my BMI calculator.

Originally, I planned on supporting both the metric and imperial BMI formulas separately. While testing, I noticed that Python's `float()` function only accepts numeric values. This became a problem because many people naturally enter their height as `5'8"` instead of simply entering `68`.

That made me stop and think about the overall user experience.

As an Asian American, I grew up seeing both measurement systems. Most Americans are comfortable with pounds and inches, while many Asian countries, including Korea, commonly use kilograms and centimeters. It made me realize that neither system is "wrong", they're simply familiar to different groups of people.

Instead of forcing every user to learn one measurement system, I think the better solution is to let users enter whichever units they are most comfortable with while standardizing the data internally.


## June 29th 
Today felt like a turning point in this project. While I originally set out to build a BMI calculator, I realized I was actually solving a much larger problem: how to accept messy human input and convert it into standardized data that the program can consistently use.

One of the biggest realizations I had was that my software design and problem-solving abilities are beginning to outpace my familiarity with Python's syntax. Throughout the day, I often knew exactly what I wanted the program to accomplish, but I struggled with expressing those ideas in Python. Interestingly, none of the problems I encountered were due to misunderstanding the algorithm itself. Instead, they came from learning how Python handles strings, variables, and data transformations. Many of these mistakes ended up being surprisingly simple, and looking back, I found myself laughing at several of them once I understood why they occurred.

Rather than repeatedly modifying my main program, I created a small testing area where I could experiment with ideas before integrating them into the project. This became one of the most valuable habits I developed today. I was able to form hypotheses, test individual concepts such as split(), replace(), and float(), and then refactor those ideas back into my parser once I understood how they worked. This process made debugging feel less frustrating and helped me focus on understanding the language instead of simply trying to make the program run.

Another important realization was recognizing the limitations of manually handling every possible user input. Initially, I found myself thinking about every variation a user could type and quickly realized that approach would not scale. Through this, I discovered that parsing and input normalization are their own areas of programming and that tools such as regular expressions (regex) exist specifically to solve these kinds of problems. While I intentionally decided not to implement regex in Version 1, I now have a clear direction for a future Version 2, where I plan to revisit this project and make the parser significantly more flexible. I also plan to learn exception handling so the program can gracefully recover from invalid input instead of terminating unexpectedly.

Perhaps the most meaningful takeaway from today was realizing that I am beginning to think more like a programmer. Instead of asking, "How do I write this line of code?" I found myself asking, "What information does this variable contain right now?" That shift in perspective helped me understand that programming is less about memorizing syntax and more about carefully managing data as it moves through a program. Looking back, today's work taught me far more than how to calculate BMI, it taught me how to break complex problems into smaller, testable pieces and build solutions one concept at a time.




---

## Raw Coding Notes

> Written while actively building this feature.
> These notes are intentionally left mostly unedited so I can see how my thinking evolved over time.

```text
The BMI formuala was created with metric system but because I am from the US I will be using a modified formula for lbs and inches

I've realized that float will only take numbers as an input and when using imperial system and for height this will be a problem.

upon further thinking I want this calculator to take cm as well. Since I am Asian American I know my family knows their height in cm as well.

Since the metric system is standardized I want to make it so that on the user end they can put any input and on our end it will convert it as the metric system while still gather data on who and how many people are using the different systems.


June 29th 
So today I came to a lot of revelations! Today I actually began tackling my new conversion and standardization. I am realizing my thought process and wants within this program is ahead of my syntax and utilization of this language. I came across a lot of syntax issues that actually made me laugh out loud when i found the solutions to. I made a test area to create theories and once i understood the concept i tried to refactor my code so that i could see if i can apply theory to practicality.
```