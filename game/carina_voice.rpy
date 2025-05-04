# Carina Voice Integration Module

init python:
    # Global flag to toggle voice playback
    config.has_voice = True
    enable_carina_voice = True
    
    # Fallback function in case the audio mapping file is not found
    if not 'carina_voice_lines' in globals():
        # This will be overwritten by audio_mapping.rpy if it exists
        carina_voice_lines = {}
        
        def play_carina_voice(line):
            pass  # No-op if mapping doesn't exist

# Callback to automatically play voice when Carina speaks
init python:
    def voice_callback(event, interact=True, **kwargs):
        if event == "say" and kwargs.get("who") == c and enable_carina_voice:
            what = kwargs.get("what", "")
            if 'carina_voice_lines' in globals() and what in carina_voice_lines:
                renpy.sound.play(carina_voice_lines[what], channel="voice")
    
    # Register the callback with RenPy's config
    config.speaking_attribute = "speaking"
    
    # Use say_sustain_callbacks which is a valid config variable in RenPy 8.3.7
    if not hasattr(config, "say_sustain_callbacks"):
        config.say_sustain_callbacks = []
    
    # Add our callback
    config.say_sustain_callbacks.append(lambda who, what: 
        voice_callback("say", who=who, what=what) if who == c else None)

# Screen for voice settings
screen voice_settings():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300
        
        vbox:
            spacing 20
            xalign 0.5
            
            label "Voice Settings" xalign 0.5
            
            vbox:
                xalign 0.5
                spacing 10
                
                # Toggle for Carina's voice
                textbutton "Carina's Voice: [enable_carina_voice and 'On' or 'Off']" action ToggleVariable("enable_carina_voice")
                
                # Voice volume control
                text "Voice Volume" xalign 0.5
                bar value Preference("voice volume")
            
            hbox:
                xalign 0.5
                spacing 30
                
                textbutton "Close" action Return()

# Hot key to open voice settings (press 'v')
screen voice_hotkey():
    key "v" action ShowMenu("voice_settings")

# Initialize and register the hotkey screen
init python:
    config.overlay_screens.append("voice_hotkey") 