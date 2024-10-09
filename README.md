# Cat Feeder

## The Problem(s)

Here is the inspiration for the project. Meet Wednesday and Dusty (I'll let you figure out who is who).
*TODO: Add cat photos*

- **Dusty** is a bit of a chonk and needs to slow down her eating.
- **Wednesday** is a little underweight but also has a tendency to scarf-&-barf (overeat and throw up).

The problem that arises is twofold:

1. **Food always needs to be available**  
   Since Wednesday is underweight, I need to ensure there's always food available for her.
  
2. **Don't have too much food available**  
   Due to Wednesday's scarf-and-barf habit and Dusty being a bit too chonky, I need to limit the amount of food that's available at any given time.

## Why don’t you just buy an automatic cat feeder?

We did, but the amount of food dispensed is too much, and it's on a schedule. So, they either don’t get enough food throughout the day, or they let it pile up, which doesn’t solve the problem.

## What's the Plan?

I have a Raspberry Pi that I’m going to wire up with a servo and a scale. Here’s the basic logic for the feeder:

1. Start loop
2. Check the weight of the food
3. If the weight is less than 30g:
    - Wait 5 minutes
    - Check the weight again
    - If the weight is still less than 30g:
        - Dispense food
4. Repeat the loop

The script will run on the Raspberry Pi, continuously checking if the weight is below 30g. If it is, the program will wait 5 minutes. This delay is to ensure that the cats are out of the way and also to slow Dusty’s eating down. It checks the weight again after the delay to make sure no "funny business" is going on. Finally, it sends a signal to a servo, which dispenses food.

## What Tools Am I Using?

1. **Raspberry Pi 4** (8GB)
2. **Digital Load Cell Weight Sensor** (HX711)
3. **Miuzei 20KG Servo Motor High Torque**
4. Jumper cables and a power supply for the servo
