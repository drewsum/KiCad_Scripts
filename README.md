# KiCad_Scripts
Dumb python scripts for KiCad made to make life easier

Run scripts through the python shell built into KiCad. As of version 5.1.5, only pcbnew has a python shell available

"hide_passive_refdes.py" hides all reference designators on a board besides connectors (J?/P?) and ICs (U?). No arguments needed.

"pcbnew_sheet_copy.py" is annoying. It's used for duplicating part placement of circuits that are copied across multiple
sheets of the project schematic. In order for it to work, sheets that are duplicates MUST be sequential. Does not copy traces or floods,
just footprint locations and visibility of refeerence designators. Start sheet, number of copies, and X/Y offsheet of each copy are specified in the script itself, not as arguments. Very useful for board swhere the same circuit is repeated many times. Reference designators of matching components on sequential sheets must have the last two digits of their reference designators match across all sheets. To do this when annotating schematics, select the option where parts are reference by sheet number * 100
