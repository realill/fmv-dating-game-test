# Audio Settings Module

# Create a preference screen to adjust audio volume
screen audio_settings():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        
        vbox:
            spacing 20
            xalign 0.5
            
            label "Audio Settings" xalign 0.5
            
            # Music volume control
            vbox:
                xalign 0.5
                spacing 10
                
                text "Restaurant Ambience Volume" xalign 0.5
                
                bar value Preference("music volume")
            
            # Sound effects volume control
            vbox:
                xalign 0.5
                spacing 10
                
                text "Sound Effects Volume" xalign 0.5
                
                bar value Preference("sound volume")
            
            # Voice volume control
            vbox:
                xalign 0.5
                spacing 10
                
                text "Carina's Voice Volume" xalign 0.5
                
                bar value Preference("voice volume")
            
            hbox:
                xalign 0.5
                spacing 30
                
                textbutton "Mute" action [Preference("all mute", "toggle"), Return()]
                textbutton "Reset" action [
                    Preference("music volume", 0.7),
                    Preference("sound volume", 0.7),
                    Preference("voice volume", 1.0),
                    Return()
                ]
                textbutton "Close" action Return()

# Hot key to open audio settings (press 'a')
screen audio_hotkey():
    key "a" action ShowMenu("audio_settings")

# Initialize and register the hotkey screen
init python:
    config.overlay_screens.append("audio_hotkey") 
    
    # Set default volumes
    preferences.set_volume("music", 0.7)
    preferences.set_volume("sound", 0.7)
    preferences.set_volume("voice", 1.0) 