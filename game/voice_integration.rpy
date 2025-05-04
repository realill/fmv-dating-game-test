# Voice Integration file to link audio_mapping.rpy with the game

# Add the carina_responses directory to Ren'Py's searchpath
init python:
    import os
    
    # Get the game directory
    game_dir = config.gamedir
    
    # Get the parent directory (project directory)
    project_dir = os.path.dirname(game_dir)
    
    # Construct the path to the audio mapping file
    audio_dir = os.path.join(project_dir, "..", "audio", "carina_responses")
    
    # Add to search path if it exists
    if os.path.exists(audio_dir):
        config.searchpath.append(audio_dir)
    
    # Alternative approach: copy the mapping directly
    mapping_file = os.path.join(audio_dir, "audio_mapping.rpy")
    if os.path.exists(mapping_file):
        try:
            with open(mapping_file, 'r') as f:
                mapping_content = f.read()
                
            # Extract the carina_voice_lines dictionary
            import re
            pattern = r'carina_voice_lines\s*=\s*\{(.*?)\}'
            match = re.search(pattern, mapping_content, re.DOTALL)
            
            if match:
                # Create the dictionary
                exec("carina_voice_lines = {" + match.group(1) + "}")
                
                # Fix the paths if needed
                fixed_paths = {}
                for text, path in carina_voice_lines.items():
                    # Ensure the path is absolute
                    if not os.path.isabs(path):
                        fixed_path = os.path.join(project_dir, "..", path)
                    else:
                        fixed_path = path
                    
                    fixed_paths[text] = fixed_path
                
                # Replace the dictionary
                carina_voice_lines = fixed_paths
                
                # Notify success
                renpy.notify("Loaded Carina's voice lines successfully!")
        except Exception as e:
            renpy.notify(f"Error loading voice mapping: {e}")
            
    # Add a debug function to be called from the console for troubleshooting
    def debug_voice_lines():
        if 'carina_voice_lines' in globals():
            for text, path in carina_voice_lines.items():
                print(f"Line: {text}")
                print(f"Path: {path}")
                print("----")
            print(f"Total lines: {len(carina_voice_lines)}")
        else:
            print("No voice lines loaded")

# Note: We don't need to add any hooks here as carina_voice.rpy already handles that 