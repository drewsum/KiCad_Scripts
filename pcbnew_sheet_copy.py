# This script copies the arrangement of parts (without traces/floods) from the start_sheet page, with num_sheets number of copied sheets afterwards from eeschema
# The start sheet and num_sheets variables are hardcoded (for now), and an X and Y offset are applied to each copied part on the sheets following the start sheet

# To use this, arrange the parts for the first sheet (the sheet to be copied) how you want. This script will then find all copies of the parts on later sheets in the schematic,
# and move them to a location copied from the starting sheet with the X and Y offset added. It will do this for num_sheets number of sheets FOLLOWING the start sheet

# For this to work properly, copies of parts on all sheets must have the same last two digits in the reference designator
# To ensure this happens correctly, copy the parts from sheet to sheet perfectly in eeschema to ensure all the reference designator endings match, or do it manually
# The script is based around reference designators that are formatted as: Uxx01, where xx is the sheet number. This correlates to the annotation setting of "page numbers * 100"
# or something like that. This script supports parts with REFDES headers (the 'U' in the above example) up to two characters long, and assumes the page number can be either 1
# or 2 digits in length. So the script can support the following "forms" of reference designators, where the 'x' digits are the sheet number:
#   Uxx01
#   TPx10
#   Rx99
#   SWxx01
#   SWx99

# I knew what this all meant over winter break 2018-2019

# import kicad pcbnew package
import  pcbnew

# hardcoded starting sheet
start_sheet = 9

# Hardcoded number of copie sheets
# This should be the number of sequential copyable sheets in addition to the start sheet
# If you have 8 of the same sheet and the start sheet is 2, num_sheets should be 7
num_sheets = 9

# X,y dimension location offsets per copy in millimeters
x_offset_per_copy = -13
y_offset_per_copy = 0

# Grid scaling, per some website about this stuff
SCALE = 1000000.0

# redefine offset based on scale
x_offset_per_copy = x_offset_per_copy * SCALE
y_offset_per_copy = y_offset_per_copy * SCALE

# Print start debug message
print "Starting sheet set to: ", str(start_sheet)
print "Number of sequential sheets set to: ", str(num_sheets)

# import current board
board = pcbnew.GetBoard()

# grab modules from board object and store in dictionary
modules = board.GetModules()

# List of modules in the start sheet
start_sheet_modules = list()

# list of sequential sheet modules
copy_sheet_modules = list()

# loop through all modules
for module in modules:
    reference = module.GetReference()
    # if sheet is one digit
    if len(reference) == 4:
        if reference[1].isdigit():
            sheet_num =  int(reference[1:2])
            if sheet_num == start_sheet:
                start_sheet_modules.append(reference)
                current_module_center = module.GetPosition()
                sheet_index = 1
                while sheet_index <= num_sheets:
                    copy_reference = reference[0] + str(sheet_num + sheet_index) + reference[2:]
                    copy_module = board.FindModuleByReference(copy_reference)
                    copy_sheet_modules.append(copy_module.GetReference())
                    copy_module_center_x = current_module_center.x + sheet_index * x_offset_per_copy
                    copy_module_center_y = current_module_center.y + sheet_index * y_offset_per_copy
                    copy_module_center = pcbnew.wxPoint(copy_module_center_x,copy_module_center_y)
                    copy_module.SetPosition(copy_module_center)
                    copy_module.SetLayer(module.GetLayer())
                    if module.IsFlipped():
                        copy_module.Flip(copy_module_center)
                    copy_module.SetOrientationDegrees(module.GetOrientationDegrees())
                    copy_module.Reference().SetVisible(module.Reference().IsVisible())
                    copy_module.SetModified()
                    sheet_index += 1
        elif reference[2].isdigit():
            sheet_num = int(reference[2:3])
            if sheet_num == start_sheet:
                start_sheet_modules.append(reference)
                current_module_center = module.GetPosition()
                sheet_index = 1                
                while sheet_index <= num_sheets:
                    copy_reference = reference[0] + str(sheet_num + sheet_index) + reference[2:]
                    copy_module = board.FindModuleByReference(copy_reference)
                    copy_sheet_modules.append(copy_module.GetReference())
                    copy_module_center_x = current_module_center.x + sheet_index * x_offset_per_copy
                    copy_module_center_y = current_module_center.y + sheet_index * y_offset_per_copy
                    copy_module_center = pcbnew.wxPoint(copy_module_center_x,copy_module_center_y)
                    copy_module.SetPosition(copy_module_center)
                    copy_module.SetLayer(module.GetLayer())
                    if module.IsFlipped():
                        copy_module.Flip(copy_module_center)
                    copy_module.SetOrientationDegrees(module.GetOrientationDegrees())
                    copy_module.Reference().SetVisible(module.Reference().IsVisible())
                    copy_module.SetModified()
                    sheet_index += 1
    # Else if the sheet is two digits
    elif len(reference) == 5:
        if reference[1].isdigit():
            sheet_num = int(reference[1:3])
            if sheet_num == start_sheet:
                start_sheet_modules.append(reference)
                current_module_center = module.GetPosition()
                sheet_index = 1                
                while sheet_index <= num_sheets:
                    copy_reference = reference[0] + str(sheet_num + sheet_index) + reference[3:]
                    copy_module = board.FindModuleByReference(copy_reference)
                    copy_sheet_modules.append(copy_module.GetReference())
                    copy_module_center_x = current_module_center.x + sheet_index * x_offset_per_copy
                    copy_module_center_y = current_module_center.y + sheet_index * y_offset_per_copy
                    copy_module_center = pcbnew.wxPoint(copy_module_center_x,copy_module_center_y)
                    copy_module.SetPosition(copy_module_center)
                    copy_module.SetLayer(module.GetLayer())
                    if module.IsFlipped():
                        copy_module.Flip(copy_module_center)
                    copy_module.SetOrientationDegrees(module.GetOrientationDegrees())
                    copy_module.Reference().SetVisible(module.Reference().IsVisible())
                    copy_module.SetModified()
                    sheet_index += 1
        elif reference[2].isdigit():
            sheet_num = int(reference[2:4])
            if sheet_num == start_sheet:
                start_sheet_modules.append(reference)
                current_module_center = module.GetPosition()
                sheet_index = 1                
                while sheet_index <= num_sheets:
                    copy_reference = reference[0] + str(sheet_num + sheet_index) + reference[2:]
                    copy_module = board.FindModuleByReference(copy_reference)
                    copy_sheet_modules.append(copy_module.GetReference())
                    copy_module_center_x = current_module_center.x + sheet_index * x_offset_per_copy
                    copy_module_center_y = current_module_center.y + sheet_index * y_offset_per_copy
                    copy_module_center = pcbnew.wxPoint(copy_module_center_x,copy_module_center_y)
                    copy_module.SetPosition(copy_module_center)
                    copy_module.SetLayer(module.GetLayer())
                    if module.IsFlipped():
                        copy_module.Flip(copy_module_center)
                    copy_module.SetOrientationDegrees(module.GetOrientationDegrees())
                    copy_module.Reference().SetVisible(module.Reference().IsVisible())
                    copy_module.SetModified()
                    sheet_index += 1

print("Start sheet modules: " + str(len(start_sheet_modules)))
print("Copy sheet modules: " + str(len(copy_sheet_modules)))

board.BuildConnectivity()
board.SetModified()
pcbnew.Refresh()

print "Finished"
