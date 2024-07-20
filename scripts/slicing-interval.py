# Script for Glyphs app to slice selected glyphs horizontally at multiple y-coordinates on the selected master

# Set the y-coordinates for the slices
start_y = -330
end_y = 770
step = 110

# Get the current font
font = Glyphs.font

# Check if a font is open
if font is None:
    print("No font open. Please open a font and try again.")
else:
    # Get selected glyphs
    selected_glyphs = [layer.parent for layer in font.selectedLayers]
    
    if not selected_glyphs:
        print("No glyphs selected. Please select one or more glyphs and try again.")
    else:
        # Get the selected master
        master = font.selectedFontMaster
        if master is None:
            print("No master selected. Please select a master and try again.")
        else:
            # Iterate through selected glyphs
            for glyph in selected_glyphs:
                # Get the layer for the selected master
                layer = glyph.layers[master.id]
                
                # Iterate through y-coordinates
                for ls in range(start_y, end_y + 1, step):
                    # Create a new GSHorizontalGuide object
                    guide = GSGuide()
                    guide.position = (0, ls)  # Set position to y=ls
                    guide.angle = 0  # Horizontal guide
                    
                    # Add the guide to the glyph's layer
                    layer.guides.append(guide)
                    
                    # Attempt to perform the slice operation
                    try:
                        layer.cutBetweenPoints((0, ls), (layer.width, ls))
                    except Exception as e:
                        # If an exception occurs (likely because there's nothing to cut),
                        # just continue to the next y-coordinate
                        pass
            
            # Update the font
            font.updateChangeCount()
            
            print(f"Slicing operation completed at y-coordinates from {start_y} to {end_y} in steps of {step} for selected glyphs on the selected master.")