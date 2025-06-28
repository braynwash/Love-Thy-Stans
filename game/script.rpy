# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bill = Character("Bill")
define stan = Character("Stan")
define ford = Character("Ford")
define narrator = Character("Narrator")

transform fade_in_from_right:
    alpha 0.0
    xpos 1.2 yalign 1.0  # start offscreen right
    linear 0.5 alpha 1.0 xpos 0.52  # slide in to slightly right of center

transform fade_in_from_left:
    alpha 0.0
    xpos -0.5 yalign 1.0   # start far left, offscreen
    linear 0.5 xpos 0.13 alpha 1.0  # slightly more to the left

transform fade_out:
    linear 0.5 alpha 0.0  # fades out over 0.5 seconds
    on hide:
        alpha 0.0  




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg living room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    ford "And if I carry the… {i}then{/i} add the…"

    show bill neutral at fade_in_from_right

    narrator "You slink into the living room, yawning and stretching as you approach the one and only Stanford Pines looming over a mile-long set of numbers and complex equations."

    show bill confused 

    bill "Sixer… what time is it?"

    show ford neutral at fade_in_from_left

    narrator "Ford hums and glances at his watch, eyes widening. He shyly looks away and taps his pen against his paper."

    show ford flustered 

    ford "Ah- nearly 1 in the morning. My apologies, Bill; It seems that on the first day of his absence, we have already broken Fiddleford’s promise to even attempt to fix our sleep schedule."

    show bill happy

    narrator "Your grin widens at the reminder of Fiddleford’s trip. Something about “urgent business back home” and how he’ll be out for “the next few days…” not that you were listening."

    bill "Psh- what Specs doesn’t know won’t kill him. Science sleeps for no one, IQ."

    show ford happy

    ford "It surely doesn't, my muse."

    ford "Regardless… perhaps we should take a break."

    show ford confused 

    ford "...Right after I finish this equation."

    show bill annoyed 

    bill "Yeah, yeah. Don’t have too much fun. Just gonna grab a drink, then hit the hay."

    show bill happy

    bill "Night, Fordsy!"

    show ford happy

    ford "Goodnight, Bill"

    

    scene bg kitchen

    narrator "As you head towards the kitchen, your stomach growls. Perhaps some cereal would do the trick- this flesh suit will be out like a light with a full stomach."

    narrator "You rummage through the fridge for some milk when you hear the faintest sound of skittering."

    narrator "It’s quiet, but you’d recognize that 8-legged sound anywhere, whipping your head around to see a sizable group of Slu’s iridescent, winged spiders crawling around the kitchen floor."

    bill "Eugh-! What the-? Shoo! Beat it!"

    label start_minigame:
    $ clicked_spiders = []  # reset before minigame starts
    call screen spider_minigame

    label after_spider_game:
    narrator "minigame end"

    # RILEY NOTES - need to add the letter asset here whenever we get it, but for now it can just be dialogue. 

      

    # This ends the game.

    return
