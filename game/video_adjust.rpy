# Simple Video Adjustment Module for RenPy 8.3.7

init -10 python:
    # Video display modes
    # 1: Original size
    # 2: Scaled up/down (centered)
    # 3: Scaled with position adjustments
    video_display_mode = 1  # Default to scaled mode
    
    # Default scaling factor (0.9 = slightly smaller than original)
    scale_factor = 0.9
    
    # Position offsets (use positive values to move down/right, negative to move up/left)
    y_offset = -50  # Start with a slight upward adjustment
    x_offset = 0    # Horizontal position adjustment
    
    # Function to create a movie with the correct scaling and positioning
    def adjusted_movie(filename):
        movie = Movie(play=filename, loop=True)
        
        if video_display_mode == 1:
            # Mode 1: Original size (centered)
            return Transform(movie, align=(0.5, 0.5))
        
        elif video_display_mode == 2:
            # Mode 2: Scaled up/down (centered)
            return Transform(movie, zoom=scale_factor, align=(0.5, 0.5))
        
        elif video_display_mode == 3:
            # Mode 3: Scaled with X/Y position adjustments
            t = Transform(movie)
            t.zoom = scale_factor
            t.xoffset = x_offset
            t.yoffset = y_offset
            t.align = (0.5, 0.5)
            return t
        
        else:
            # Default to scaled mode
            return Transform(movie, zoom=0.9, align=(0.5, 0.5))

# Create a preference screen to adjust video display
screen video_settings():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        
        vbox:
            spacing 20
            xalign 0.5
            
            label "Video Display Settings" xalign 0.5
            
            text "Display Mode:" xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 10
                
                textbutton "Original Size" action [SetVariable("video_display_mode", 1), Return()]
                textbutton "Scale Video" action [SetVariable("video_display_mode", 2), Return()]
                textbutton "Position Adjust" action [SetVariable("video_display_mode", 3), Return()]
            
            null height 20
            
            # Scale factor control (for modes 2 and 3)
            if video_display_mode >= 2:
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    text "Scale factor: [scale_factor]" xalign 0.5
                    
                    hbox:
                        xalign 0.5
                        spacing 10
                        textbutton "Smaller" action [SetVariable("scale_factor", max(0.5, scale_factor - 0.1)), Return()]
                        textbutton "Reset (0.9)" action [SetVariable("scale_factor", 0.9), Return()]
                        textbutton "Larger" action [SetVariable("scale_factor", min(2.0, scale_factor + 0.1)), Return()]
            
            # Position controls (for mode 3)
            if video_display_mode == 3:
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    # Vertical position
                    text "Vertical Position (Y-Offset: [y_offset])" xalign 0.5
                    
                    hbox:
                        xalign 0.5
                        spacing 10
                        textbutton "Move Up" action [SetVariable("y_offset", y_offset - 10), Return()]
                        textbutton "Center Y" action [SetVariable("y_offset", 0), Return()]
                        textbutton "Move Down" action [SetVariable("y_offset", y_offset + 10), Return()]
                    
                    # Horizontal position
                    text "Horizontal Position (X-Offset: [x_offset])" xalign 0.5
                    
                    hbox:
                        xalign 0.5
                        spacing 10
                        textbutton "Move Left" action [SetVariable("x_offset", x_offset - 10), Return()]
                        textbutton "Center X" action [SetVariable("x_offset", 0), Return()]
                        textbutton "Move Right" action [SetVariable("x_offset", x_offset + 10), Return()]
            
            null height 20
            textbutton "Close" action Return() xalign 0.5

# Hot key to open video settings (press 'v')
screen video_hotkey():
    key "v" action ShowMenu("video_settings")

# Initialize and register the hotkey screen
init python:
    config.overlay_screens.append("video_hotkey") 