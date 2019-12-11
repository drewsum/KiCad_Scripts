# KiCad_Scripts
Dumb python made to make life easier


Run scripts through the python shell built into KiCad. 

"hide_passive_refdes.py" hides all reference designators on a board besides connectors (J?/P?) and ICs (U?)

"pcbnew_sheet_copy.py" is annoying. It's used for duplicating part placement of circuits that are copied across multiple
sheets of the project schematic. In order for it to work, sheets that are duplicates MUST be sequential. Does not copy traces or floods,
just footprints locations. Start sheet, number of copies, and X/Y offsheet of each copy are specified in the script itself, not as arguments.
