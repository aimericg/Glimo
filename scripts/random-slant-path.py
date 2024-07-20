import random
from math import tan, radians

# Function to apply random slant to a path
def random_slant_path(path):
    angle = random.uniform(-15, 15)
    slant = tan(radians(angle))
    path.applyTransform((1, 0, slant, 1, 0, 0))

# Main script
font = Glyphs.font
selectedLayers = font.selectedLayers
currentMaster = font.selectedFontMaster

for layer in selectedLayers:
    if layer.associatedMasterId == currentMaster.id:
        glyph = layer.parent
        glyph.beginUndo()  # Begin undo grouping
        
        for path in layer.paths:
            random_slant_path(path)
        
        glyph.endUndo()  # End undo grouping

font.currentTab.forceRedraw()
print(f"Random slant applied to selected glyphs in the '{currentMaster.name}' master.")