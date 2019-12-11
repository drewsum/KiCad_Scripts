# import kicad pcbnew package
import  pcbnew

# import current board
board = pcbnew.GetBoard()

# grab modules from board object and store in dictionary
modules = board.GetModules()


# loop through all modules
for module in modules:
    reference = module.GetReference()
    
    if  reference[0] != 'U' and reference[0] != 'J' and reference[0] != 'P':
        module.Reference().SetVisible(False)

board.BuildConnectivity()
board.SetModified()
pcbnew.Refresh()

print "Finished"