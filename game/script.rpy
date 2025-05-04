# Dating FMV Game - Main Script

# Define characters
define c = Character("Carina", voice_tag="carina")
define player = Character("[player_name]")

# Define variables
default player_name = "Alex"
default carina_mood = 50

# Define audio
define audio.restaurant_ambience = "audio/restaurant_ambience.mp3"
# Define Carina's voice lines using existing MP3 files
define audio.carina_intro = "audio/line_001.mp3"
define audio.carina_thanks = "audio/line_002.mp3"
define audio.carina_rooftop = "audio/line_003.mp3"
define audio.carina_nervous = "audio/line_004.mp3"
define audio.carina_wine = "audio/line_005.mp3"
define audio.carina_cocktails = "audio/line_006.mp3"
define audio.carina_water = "audio/line_007.mp3"
define audio.carina_job_1 = "audio/line_008.mp3"
define audio.carina_job_2 = "audio/line_009.mp3"
define audio.carina_dates = "audio/line_010.mp3"
define audio.carina_city = "audio/line_011.mp3"
define audio.carina_enjoyed_1 = "audio/line_012.mp3"
define audio.carina_enjoyed_2 = "audio/line_013.mp3"
define audio.carina_nice = "audio/line_014.mp3"
define audio.carina_late = "audio/line_015.mp3"

# Define custom dissolve for video transitions
define video_dissolve = Dissolve(0.5)

# Initialize voice lines list for checking
init python:
    # Voice lines dictionary
    carina_voice_lines = {
        "intro": audio.carina_intro,
        "thanks": audio.carina_thanks,
        "rooftop": audio.carina_rooftop,
        "nervous": audio.carina_nervous,
        "wine": audio.carina_wine,
        "cocktails": audio.carina_cocktails,
        "water": audio.carina_water,
        "job_1": audio.carina_job_1,
        "job_2": audio.carina_job_2,
        "dates": audio.carina_dates,
        "city": audio.carina_city,
        "enjoyed_1": audio.carina_enjoyed_1,
        "enjoyed_2": audio.carina_enjoyed_2,
        "nice": audio.carina_nice,
        "late": audio.carina_late
    }
    
    # Video acceleration settings
    config.hw_video = True
    config.gl_enable = True
    
    # Simple movie function for fallback
    def simple_movie(filename):
        return Movie(play=filename, loop=True)
    
    # Function to switch videos smoothly
    def switch_video(old_video, new_video):
        if old_video:
            renpy.hide(old_video)
        renpy.with_statement(video_dissolve)
        renpy.show(new_video)

# Use the advanced video adjustment function from video_adjust.rpy
# With fallback to simple movie function if not available

# The game starts here
label start:
    # Get player name
    $ player_name = renpy.input("What's your name?", "Alex").strip()
    if player_name == "":
        $ player_name = "Alex"
    
    # Show a brief help message about video adjustment
    scene black
    
    # Start playing the restaurant ambience in the background
    play music restaurant_ambience loop fadein 3.0
    
    # Start of date scene
    with dissolve
    
    # Use a try/except block to handle potential errors with adjusted_movie
    $ movie_func = adjusted_movie if "adjusted_movie" in globals() else simple_movie
    
    show expression movie_func("videos/idle.webm") as bg with Dissolve(1.0)
    "You arrive at the rooftop restaurant in New York."
    "You spot Carina at a table near the edge."
    
    show expression movie_func("videos/speak.webm") as bg with video_dissolve
    play sound carina_intro
    c "Hi, you must be [player_name]. I'm Carina."
    
    menu:
        "How do you respond?"
        
        "You look even more beautiful than your photos.":
            $ carina_mood -= 5
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_thanks
            c "Oh... thanks, I guess."
            
        "Great to meet you, Carina. Amazing view here.":
            $ carina_mood += 10
            show expression movie_func("videos/smile.webm") as bg with video_dissolve
            play sound carina_rooftop
            c "Doesn't it? I love rooftop spots in the city."
            
        "I'm a little nervous, I've been looking forward to this.":
            $ carina_mood += 5
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_nervous
            c "That's sweet. I'm a bit nervous too."
    
    show expression movie_func("videos/idle.webm") as bg with video_dissolve
    "The waiter arrives to take your orders."
    
    menu:
        "What drink do you order?"
        
        "I'll have whatever wine you recommend.":
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_wine
            c "I know a great Cabernet they serve here."
            $ carina_mood += 5
            
        "How about cocktails? I make a mean Old Fashioned.":
            show expression movie_func("videos/smile.webm") as bg with video_dissolve
            play sound carina_cocktails
            c "Oh, you're into cocktails? I'd love to try yours sometime."
            $ carina_mood += 10
            
        "Just water for me.":
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_water
            c "That's fine. I'll have a glass of wine."
    
    show expression movie_func("videos/idle.webm") as bg with video_dissolve
    "After ordering, there's a moment of silence."
    
    menu:
        "What do you talk about?"
        
        "Tell me about your work as an art curator.":
            $ carina_mood += 15
            show expression movie_func("videos/smile.webm") as bg with video_dissolve
            play sound carina_job_1
            c "Oh, I love my job! I'm working on a photography exhibition."
            play sound carina_job_2
            c "It's challenging but so rewarding."
            
        "How many dates have you been on from the app?":
            $ carina_mood -= 10
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_dates
            c "Um, a few. I don't really keep count."
            
        "Do you ever think about living somewhere quieter?":
            $ carina_mood += 5
            show expression movie_func("videos/speak.webm") as bg with video_dissolve
            play sound carina_city
            c "Sometimes I dream about a weekend house upstate, but I'm a city girl at heart."
    
    # Final outcome
    if carina_mood >= 70:
        show expression movie_func("videos/smile.webm") as bg with video_dissolve
        play sound carina_enjoyed_1
        c "I've really enjoyed talking with you tonight."
        play sound carina_enjoyed_2
        c "Would you like to continue this at my favorite café?"
        "SUCCESS: Carina wants to extend the date!"
        
    elif carina_mood >= 40:
        show expression movie_func("videos/speak.webm") as bg with video_dissolve
        play sound carina_nice
        c "This was nice. We should do it again sometime."
        "NEUTRAL: She might be open to a second date."
        
    else:
        show expression movie_func("videos/speak.webm") as bg with video_dissolve
        play sound carina_late
        c "Well, it's getting late. I should head home."
        "FAILURE: She's not interested in a second date."
    
    # Fade out the music
    stop music fadeout 3.0
    
    hide bg with Dissolve(2.0)
    scene black
    "The End"
    
    return
