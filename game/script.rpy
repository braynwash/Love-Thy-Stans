# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bill = Character("Bill")
define stan = Character("Stan")
define ford = Character("Ford")
define narrator = Character("Narrator")
define guest = Character("Random Guest")
define sleepy = Character("Sleepy Ghost")
define angry = Character("Angry Ghost")
define silly = Character("Silly Ghost")
define carmilla = Character("Carmilla")
define grabby = Character("Mr. Grabby Pants")

transform fade_in_from_right:
    alpha 0.0
    xpos 1.2 yalign 1.0  # start offscreen right
    linear 0.5 alpha 1.0 xpos 0.52  # slide in to slightly right of center

transform fade_in_from_left:
    alpha 0.0
    xpos -0.5 yalign 1.0   # start far left, offscreen
    linear 0.5 xpos 0.13 alpha 1.0  # slightly more to the left

transform fade_out_to_left:
    on hide:
        linear 0.5 xpos -0.5 alpha 0.0







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
    narrator "Suppressing your disgust as you swat at the abundance of arachnids, you smack away a smaller spider that drops a fancy-looking purple envelope (all these spiders to deliver a single letter? The melodrama!)"

    # RILEY NOTES - need to add the letter asset here whenever we get it, but for now it can just be dialogue. 

    narrator "Bill Cipher,"

    narrator "Recently, Carla has been expressing concern about how you and your {i}“friend”{/i} have been going out less and less. I personally find your absence to be {i}wonderful{/i}, but she somehow cares for you, and I do not wish to see her upset any longer."

    narrator "An event you {i}may{/i} remember from long ago is returning tomorrow evening in the Crawlspace, and through my connections, I was able to obtain an extra invitation in Stanfords’ name as an esteemed {i}Guest of Honor{/i} that allows for a plus one and some other {i}lucrative{/i} benefits."
    
    narrator "I appreciated his willingness to participate in my little game and feel this experience will be enjoyable for him."
    
    narrator "Given the {i}escapade{/i} that got you removed from this event all those years ago, if for some reason he brings you along, I suggest not kicking up another fuss."

    narrator "Thank Carla when you see her next. Do try not to get thrown out {i}again{/i}, I have a reputation to uphold."

    narrator "Regards, Slu."

    narrator "Ah, yes, the Cryptid Exchange, an exclusive all-you-can-want event that happens every once in a blue moon, bringing all the oddities and {i}freaks{/i} Gravity Falls has to offer together for a night of unbarred gluttony and {i}not quite{/i} lethal entertainment."

    narrator "You {i}vaguely{/i} remember the few times you went by piloting some low-tier creatures; full of buzz-kills, nothing to rave about, really. Besides, you have work to do! The portal ain't gonna build itself."

    narrator "…Then again, Sixer would be absolutely delighted to go to this type of event."
   
    narrator "You don't know if you’d rather groan or chuckle at the thought of him wide-eyed and scribbling in his little Journal. And looking back, you have been getting significantly less fresh air lately. Wouldn’t hurt to take this meat sack for a spin!"

    menu:
        "Show Ford the letter":
            narrator "Definitely NOT excited at the prospect of an adventure with Ford, thank you very much, you hustle back over to the living room with newfound energy as you wave the letter around."

            scene bg living room

            show bill excited at fade_in_from_right

            bill "Sixer, Sixer! Look what I’ve got here!"

            show ford confused at fade_in_from_left

            ford "A… letter? At this hour? How peculiar! I didn't even see you go outside."

            show bill annoyed 

            bill "Don't think about the logistics, Brainiac, we've got a game to move along. Read it! Pronto!"

            show ford neutral

            show bill happy   
    
            narrator "You watch Ford’s tired eyes light up as they scan Slu’s letter and stifle a snort as he grips the invitation tight, gazing at the piece of paper in awe. Nerd."
       
            show ford excited 

            ford "This is-! In all of my years here in Gravity Falls, I had no {i}idea{/i} they held such an event!"

            ford "This is {i}perfect!{/i} I had been hoping to return to the Crawlspace and conduct a closer study on its anomalous properties; I have a theory that-"

            show bill neutral

            bill "You let out an exaggerated yawn, effectively interrupting Ford from spiraling into a signature rant."

            show ford flustered

            ford "Ah- yes, um- thank you for showing me this, Bill."

            ford "It is quite late- we should head to bed if we wish to be well rested for tomorrow."

        "Leave the letter on the table":
            narrator "Your mind fogs after reading the letter. You’re not exactly {i}thrilled{/i}; your primary focus is to finish the portal and leave this stupid, mushy mortal flesh behind so you can get back to ruling the world."

            narrator "And if Ford sees this invitation- well, {i}his{/i} invitation- he’ll most certainly be dragging you out the second the moon rises. Best not to bring it up now. Or ever."

            narrator "Abandoning the letter, you resume your quest for cereal and trudge into you and your authors’ bedroom, ready for some shut-eye."

            scene bg bedroom

            narrator "Cozying up under a weighted blanket, you feel a wave of sleep begin to creep up on you…"

            narrator "…Right before Ford bursts into the room, waving an unfortunately familiar purple letter back and forth."

            show ford excited at fade_in_from_left

            ford "Bill, wake up! Have you read this letter? It’s addressed to you and I found it laying on the table next to one of Slu’s…spider… things…?"

            ford "I understand it wasn’t- ah, {i}addressed{/i} to me, my apologies for opening it… But, it tells of an exclusive event in the Crawlspace tomorrow evening! An event where I am the {i}guest of honor{/i}! What an opportunity!"

            ford "We should- no no, we NEED to go! You {i}must{/i} come as my plus one! {i}Imagine{/i} all the research we could accomplish!"

            narrator "You stifle a weary groan in your throat, now thoroughly awake again. It seems like you don't have much choice in going"

            narrator "Even while tired and grumpy, you find that you can’t possibly say no to Ford, however- not when his face is beaming and his eyes are on you, full of stars."

            show bill annoyed at fade_in_from_right

            bill "Alright, alright…{i}fine!{/i} We’ll go. Can I get back to sleep now?"

            show ford flustered

            ford "Yes! Of course- ah, sorry for interrupting your rest, my muse. We should sleep soon if we wish to be well rested for tomorrow."


    scene bg bedroom 

    narrator "A few minutes pass as you lie comfortably in bed; you hear Ford shuffling and fidgeting under his covers. You can {i}feel{/i} he wants to say something, and you wait for him to bring it up."

    show ford flustered at fade_in_from_left

    ford "My muse, have you ever… gone to this event before?"

    ford "There are… a {i}lot{/i} of things I still do not know about Gravity Falls. You must have seen it all a thousand times over."

    narrator "You contemplate telling your author the truth, just to see his reaction, but the sight of his forlorn expression springs into your mind, making you pause."

    show bill happy at fade_in_from_right

    bill "Pfft- nah, these kinds of “parties” are beneath me. Bunch of stiffs- never bothered with going. Trust me, Fordsy, you’re the only living being I would even consider joining at this sorta thing."

    show ford happy

    ford "…Alright, my muse. Get some rest, we have a big day tomorrow."

    # RILEY NOTE - END OF EVENT ONE 

    # RILEY NOTE - START OF EVENT 2 

    scene bg kitchen

    narrator "After a day of routine portal work, a quick phone call to Fiddleford on portal progress, and Ford's “necessary” overpacking, it was finally time to head to your most unanticipated event of the century— the Cryptid Exchange."

    show ford excited at fade_in_from_left 

    ford "My muse! I believe I’m all set. Are you ready to leave?"

    show bill annoyed at fade_in_from_right

    bill "Hold your horses, IQ- I’m coming."

    show ford flustered

    ford "Oh! One moment- almost forgot my {i}third{/i} pen! Don’t go anywhere!"

    # RILEY NOTE - MAKE IT SO FORD FADES OUT 

    hide ford with dissolve

    show bill flustered 

    narrator "You send a fond smile at Ford’s back, but school your expression as  he comes rushing back in record time, pen in hand."

    show bill neutral 

    show ford excited at fade_in_from_left

    ford "Right! Let's make haste!"

    scene bg party

    narrator "You and Ford arrive at the Cryptid Exchange with the author {i}shaking{/i} in excitement next to you. You look around and stifle a groan at the sight of an assortment of creatures noshing, dancing, drinking and partaking in an intoxicated, absolutely unregulated round of axe-throwing."
    
    narrator "Looks like a good time, but can’t possibly be safe for your mortal."

    narrator "...Flesh. Your mortal {i}flesh.{/i}"

    narrator "As your vision jumps around the festivities, you fail to notice said mortal wander off into the treeline and away from the main event."

    show bill annoyed 

    bill "Ughh, look, Sixer- most of these partygoers are either creatures from the bargain-bin or annoying, blockheaded faeries. Remember what happened the last time we got wrapped up with the fae?"

    show bill happy

    bill "Just stick close to me, yeah? I’m an expert."

    show bill confused 

    narrator "There’s silence where the space should’ve been filled with Ford’s utmost understanding and praise. You whip around, expecting him to be entranced in the scene, but Ford is nowhere to be found."

    hide bill with dissolve 

    narrator "There’s silence where the space {i}should’ve{/i} been filled with Ford’s utmost understanding and praise. You whip around, expecting him to be entranced in the scene, but Ford is nowhere to be found."

    narrator "Panic bubbles in your gut and your breath quickens as you frantically turn in numerous directions, but it settles when you notice the tail end of a brown coat across the crowd, along the trees."

    narrator "You sigh in relief and roll your eyes as you move to make your way to him across the crowd; before you take another step, someone- or {i}something-{/i} grabs your hand, pulling you further away from Ford and deeper into the party towards the Crawlspace."

    show bill upset 

    bill "Hey! What’s the big idea? Do you even know {i}who I am?!{/i}"

    narrator "A mixed group of fae folk have amassed behind you- some laughing, some idly chatting, some looking at you expectedly. A particularly stubby satyr at the front of the group has clutched your hand and makes no effort to let go, but halts at your nasty expression."

    guest "Uhh- yeah? Stanford Pines’ plus one, right?"

    show bill flustered 

    bill "{i}Stanford Pines’{/i} plus one?! This is- You can’t be serious!"

    guest "Uh- yeah, whatever man. You wanna keep wandering up here like a lost puppy or are you gonna come party down in the Crawlspace? Stanford’s already down here- he’s about to be commemorated as the Guest of Honor."

    show bill neutral

    narrator "You pause. You know beyond a shadow of a doubt you saw a brown coat drift past the trees, nowhere {i}near{/i} the Crawlspace- then again, with Ford’s track record regarding the fae, he could’ve already stumbled into the party expecting riveting conversation and instead landed into a soul-binding deal."    

    menu:
        
        "Look for Ford.":
            bill "placeholder"



        "Join the party.":
            show bill happy
            bill "Y’know what- sure, why not? I’ll come ‘party' with you."

            narrator "The group of fae folk all cheer and whoop in excitement, steering you towards the Crawlspace as they continue their idle chatter. You allow yourself to be drug deep into the underground but wrench your hand out of the satyr’s grip. "
        
            narrator "Six-fingered hands {i}only,{/i} pal."

            show bill neutral

            narrator "A distant part of yourself feels anxious about leaving Ford by himself up here- but if he’s {i}allegedly{/i} already down there, the coat was likely an illusion, a figment of your imagination, or some underhanded shapeshifting trick on you {i}specifically{/i}, obviously."

            narrator "When you find your author down here, you can make sure there’s no overindulging or {i}fraternizing{/i} or deal-making (besides your own!); the earlier you can find him the better."

            grabby "Nice, man- you’d better get down here fast. It’s the last round and the fights’ been neck and neck for the past few minutes, your friend is the {i}coolest.{/i}"

            show bill confused 

            narrator "The words make your brows furrow, and you grapple to understand what fighting has to do with {i}anything{/i} for an esteemed guest- your thoughts screech to a halt as you remember what Slu conveniently forgot to mention in her invite."        

            narrator "During the event, the “Guest of Honor” has to defend their title against a horde of challengers also gunning for that same title. It’s a brutal gauntlet that isn’t fit for a human- hearing how Ford’s held off until the last competitor puts a grin on your face."

            scene bg fighting

            narrator "As you’re ushered into the Crawlspace, you spot a make-shift fighting ring surrounded by a seemingly unending crowd of monsters, fae folk, and other oddities. You slink your way through the crowd to the front of the stage; you expect to see your author, rugged and glistening with determination."

            narrator "You see something- or {i}someone{/i}- much, much worse."

            show bill upset 

            bill "Oh you have {i}GOT{/i} to be KIDDING ME!!"

            narrator "In some cruel twist of fate (yuck it up, Ax!), standing in the middle of the fighting ring with a bruised face and raised fists, is Sixer’s worthless, no good copy- the one living being you hate more than anything else on this worthless hunk of rock- is Stanley Pines himself. "

            hide bill 

            show stan excited 

            stan "That all you got? And here I thought I was the {i}honored{/i} guest."

            hide stan with dissolve 

            narrator "You groan loudly and smack your head against the edge of the ring, eliciting some cold glares from the crowd around you. "
            
            narrator "This genuinely {i}can’t{/i} be happening right now. You died on the way here and this is your own personal hell."

            narrator "Stan must hear your groan of anguish, because he turns around just in time to make dead-eye contact with you."

            show stan confused 

            stan "What’s the matter, doll? Not enjoyin’ the show or somethin’?”"

            menu: 

                "Say nothing.":
                    show bill annoyed at fade_in_from_right

                    show stan upset at fade_in_from_left

                    narrator "You say nothing, not wanting to waste your breath on your author’s cheap copy. Stan huffs and turns back to his opponent; despite your “rejection,” he rears back with newfound confidence."

                    hide stan with dissolve

                    narrator "You watch the bumbling idiot rear back to full height and wince when Stan lands a hit square in his opponents’ jaw, effectively winning the match."

                "Leave loudly.":
                    narrator "placeholder"


    # This ends the game.
    return
