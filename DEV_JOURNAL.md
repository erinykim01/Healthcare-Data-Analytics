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




---

## Raw Coding Notes

> Written while actively building this feature.
> These notes are intentionally left mostly unedited so I can see how my thinking evolved over time.

```text
The BMI formuala was created with metric system but because I am from the US I will be using a modified formula for lbs and inches

I've realized that float will only take numbers as an input and when using imperial system and for height this will be a problem.

upon further thinking I want this calculator to take cm as well. Since I am Asian American I know my family knows their height in cm as well.

Since the metric system is standardized I want to make it so that on the user end they can put any input and on our end it will convert it as the metric system while still gather data on who and how many people are using the different systems.
```