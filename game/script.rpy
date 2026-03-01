# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("monster")

define a = Character("alice")

define c = Character("Charlotte")

define s1 = Character("student 1")

# The game starts here.
#1920x 1080
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg school

    "it's a fairly normal day on campus"

    "like most others charlotte was messing around with her friends, alice was avoiding them, and robert was setting the lab on fire"

    show alice bored

    "alice is eating alone, much to her personal aproval"

    "no sooner did she pop the first of todays allocated chicken nuggets in her mouth than gods punishment for being alone arrived"

    show alice bored at left

    show charlotte happy at right

    c "heey sleepy~"

    c "sooo..."

    c "i know you like to spend all your time away from everyone... but you wanna go camping with us?"

    hide alice bored
    show alice suprise at left

    a "... what?"

    a "w-wha- i..."

    a "charlotte you know i-"

    c "bup bup bup! i told you to call me charlie~"

    hide alice suprise
    show alice anger at left

    a "..."
    pause 1.5
    menu optional_name:

        "call her charlotte":
            pass
        "call her charlie":
            $ c = 'Charlie'       

    a "so, [c]... camping trip?"

    if c != 'Charlie':
        "charlotte narrow's her eyes at alice, but her grin doesn't falter"

    c "yeah! since it's the last day before graduation week i got a bunch of people from our grade together for a camping trip!"

    hide alice anger
    show alice bored at left

    a "... and you're also inviting me?"

    a "why? you know i hate lots of people."

    c "well, most of them said no. BUT mostly because then you'll be there!! ;3"

    a "..."

    c "<3"

    a "*sigh*"

    a "so you think that i'll go since there will be less people?"

    c "you don't get a choice. <3"


    hide alice bored
    show alice suprise at left

    pause 1.0

    a "w-wha-"

    hide alice suprise
    show alice flirted at left

    a "right..."

    c "so, you want me to pick you up or...?"

    hide alice flirted
    show alice anger at left

    "alice turns and walks away from her, hoping she won't follow"

    scene bg room
    with fade
    pause 1.0
    "alice wakes up the next day with a groan and a headache"
    show alice anger
    a "ughhh... why is it always that nightmare."

    "alice gets up and get's dressed for a day of lazing around at home"

    scene bg kitchen
    with fade
    show alice bored
    pause 1.0
    "as alice is eating breakfast she suddenly remembers what charlotte had said yesterday"

    a "dammit..."

    a "knowing [c] she'll probably be here in about and hour"

    a "..."

    menu choice2:
        "wait for [c]?"
        "wait for [c]":
            $ f = True
        "leave early":
            $ f = False
        
    if f:
       
        "reluctantly, alice waits for [c]"

        "as expected, [c] arrives just an hour later"
        show charlotte happy at right
        show alice bored at left
        c "hey cutie! you waited for me~?"
        
        hide charlotte happy
        show charlotte nice at right

        c "that's so nice of you, my sweetie~"

        hide alice bored
        show alice flirted at left

        a "S-Sweetie! w-what are yo-"

        hide charlotte nice
        show charlotte exite at right

        c "shhh~ c'mon! we got camping to get to!"

        "alice follows the energetic flirt out to her car"

        scene black
        with fade

        pause 3.0

        scene bg camp lot
        with fade
        "they arrive at the camping grounds parking-lot"
    else:

        "alice decides to leave before [c] arrives to pester her"
        scene black
        with fade
        pause 3.0
        scene bg camp lot
        with fade
        "alice arrives at the camping grounds parking-lot"

    show alice bored at left
    if f:
        show charlotte happy

    "most of those willing to go have already arrived, seemingly waiting for [c] to arrive"

    if f == False:
        show charlotte happy 
        "[c] arrives not much later"
    else:
        s1 "looks like she got her girly-friend~"

        show alice flirted at left

        "alice feels herself light up red but charlie completely ignores the not so quiet wispering"

    c "hey everyone! ready to go camping?"

    "she grabs alices arm and strolles right between them, walking the trail towards the camping sites"

    "[c] lets go of her arm, but her hand drifts down to hold alices, keeping her close of her"
    
    if f == False:
        hide alice flirted

    show alice flirted at left

    a "c-[c]..."

    hide charlotte happy
    show charlotte nice
    c "shh."

    a "..."

    "they keep walking with the group following behind"
    scene bg forest trail
    with fade

    "they keep walking, passing multiple designated camping sites until they arive at the last one where the trail ends in a chained fence gate."

    show alice flirted at left
    show charlotte 


    a "so we're stopping he-"

    "[c] rear's up and kicks the gate, shattering the chain and nearly brakeing the gate off the bar that mounts it to the fence"
    hide alice bored
    show alice scared at left
    pause 3.0
    a "... y-you can do that??"

    c "yeah"

    hide charlotte
    show charlotte nice

    c "impressed?"
    pause 2.0






    scene bg deep forest
    with fade


    "they walk for another hour and a half, the trail slowly fading out from overgrowth."
    "right before the trail disapears completely the walk into a huge clearing in the forest"

    show alice happy at left
    show charlotte happy
    c "this looks good"

    c "EVERYONE! SPREAD OUT AND SET UP HERE!"

    "everyone walks past her into the clearing, sectioning off in groups to camp out"

    "[c] looks over at alice"

    hide charlotte happy
    show charlotte exite

    c "so~"

    hide alice happy
    show alice flirted at left

    a "NO, im not staying with you in your tent!"

    hide charlotte exite
    show charlotte

    c "fine, i'll leave you to yourself then..."

    hide charlotte
    show alice flirted

    "[c] jogs out into the clearing to start setting up a fire pit for tonight"



    scene bg campsite
    with fade

    "a few hour later everyone had set up their camping groups and were enjoying picnics around for lunch"

    "[c] was patroling the edge of the clearing, picking up firewood for some bonfire tonight"

    menu choice3:
        "..."
        "eat lunch":
            $ h = False
            "alice sits down by her tent and eats a sandwich she packed this morning"

        "help out [c]":
            $ h = True

            show alice bored at left
            show charlotte at right
            "alice walks over to [c] as she passes by"

            a "... need any help?"

            c "hm? oh, not really"
            c "but i'd definatly love the company"

            "alice trails along beside her"

            "..."
            hide charlotte
            show charlotte nice at right
            c "i'm really glad you actually did decide to come with us"

            c "it warms my heart knowing you want to spend time with me~"

            hide alice bored
            show alice flirted at left
            a "h-huh!? w-wh- i..."

            menu choice4:
                
                "deny it":
                    a "i-i didn't do it because i wanted to hang out with you!"

                    c "really? i didn't know you had other friends to hang with out here~"

                    a "..."

                    show alice anger at left

                    c "well, you're spending more time with me than them anyway so i dont care."

                "stay quiet":
                    a "..."

                    c "what? no witty comeback?"
                    
                    hide charlotte nice
                    show charlotte exite at right
                    c "i like it when you fight back, but it's nice to know you admit it~"

                    a "..."
                
        
    scene bg camp night
    with fade

    "a few hours go by with people enjoying their time outside before night falls"

    "some people have already gone to bed, but most crowd around a couple of fire pits to tell spooky storys"

    show alice happy
    show charlotte happy at right

    "[c] is telling a story but alice isn't listening much, just stareing into the firelight"

    
    if h:


        show alice flirted
        "alice straitens up when [c] puts her arm around her"
        
    "she comes back to her senses and starts listening to her story"

    c "as she cowered under the bed the lanky figure slid in through the window and dropped down right in front of her."

    c "it's iron claws slid across the wooden floorboards as it climbed to it's feet in front of her"

    c "suddenly! it grabbed onto the bed and flung it across the room!"

    c "it lunged forward catching her neck in its jaws with a snap!"
    
    "she punctuated her final word with a loud clap"

    "the second she did so though, somthing sprung from the forest, coliding with the campfire sendind burning sticks careening in every direction"

    hide alice flirted
    hide alice happy
    hide charlotte happy
    show alice suprise
    show charlotte annoyed at right

    c "JESUS! what the hell just happend!"

    "the panicked and confused screams die out quickly as everyone looks around to find out what just happend"

    hide alice suprise
    show alice scared
    hide charlotte annoyed
    show charlotte frightend at right

    "alice is the first to see it, quickly followed by [c], then everyone else"

    "half of one of their fellow campers is still sitting by the camp fire"

    "the other half sits at the edge of the fire light a indecernable thing hunched over it"

    "a viceral streak across the grass connects her two halfs"

    "the entire camp is silent save for the stomach churning sounds of the creature moving"

    show monster at left

    "the creature lurches around as it slams the half corpse into the ground repeatedly"

    "it stops as it looks up at the students again"
    
    pause 2.0
    "."
    pause 2.0
    ".."
    pause 2.0
    "..."
    pause 2.0


    m "*@#$&@*@&!#&##!!&"

    hide monster
    show monster bloody at left

    "the monster finishes it's grinding mechanical screach by biting into the corps, riping it nearly in half, and huraling it at them"

    "the sudden flying body sends everyone into a frenzy, the grass finnaly begining catching fire around the campsite from the erlier crash"

    "more of these things come out of the woodwork, rending people apart as they find prey"

    show alice scared at right
    show charlotte frightend 

    "[c] grabs alice and pulls her behind herself"
    c "alice, run!"

    "alice snaps out of her frozen shock"
    a "h-huh!? b-but what about you!?"

    hide charlotte frightend
    show charlotte engaged

    c "don't worry. i'll worm my way out of this love, just go!"

    "despite her fears alice bolts for the tree's"

    "!WARNING!
    THIS IS A QUICK TIME EVENT"
    "IT IS RECOMENDED THAT YOU SAVE HERE BEFORE CONTINUING"

    scene bg deep forest


    show alice scared
    
    menu(time=7.0, timeout="dive right"):
        "somthing crashes into the trees behind her to her southwest"
        "duck left":
            "its claws pass over her by an inch as it slams into another tree"
        "dive right":
            "the thing catchs her in the stomach as it rolls over her"
            "her legs go numb as she hit's a tree full force and all goes black"

            "the end"
            return

        
    menu(time=7.0, timeout="dive right"):
        "it bounds off a tree to her southeast"
        "duck left":
            "it sinks its teeth inbetween her ribs, twisting and tearing with rage"

            "the end"
            return

        "dive right":
            "its goes headlong into another tree"
            









    scene bg chaple


    show alice scared

    "her stumbling leads her out into another small clearing with a rotted and collapsed church inside"

    show monster bloody at left

    "when she spins around to see where the creature is she lockes eyes with it, standing at the edge of the woods"

    "it screaches at her incoherently like a bird, not dareing to enter hollowed grounds"
    hide monster bloody
    show alice scared at right
    "whith no idea what else to do alice walks up to the church and in throuth the broken door"
    
    "there's a crack as the floor boards give out and alice falls"

    scene bg underneath
    with fade

    show alice scared

    "alice pickes herself off the dusty floor and looks around"

    a "... w-what in the..."

    "alice looks up and realizes that the church is nearly ten feet up."
    
    "the only option she has left is the cold, dry tunnle forward"
    "deeper into whatever just happend"
    "the bleeding growths on the walls would suggest that this place is not foreign the those things above"
    
    menu proggress:
        
        "progress":
            pass
        "progress":
            pass
        
    "the end"
    "for now..."

    return
