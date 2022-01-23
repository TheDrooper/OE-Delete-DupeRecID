# OE-Delete-DupeRecID
Delete OpenEdge Records with Duplicate RecIDs

When you create a new unique index in an OpenEdge database, you may get duplicate record errors when rebuilding the indices. This is due to multiple records matching the uniqueness criteria. This Python utility will read the error log and create an ABL program that can be run to delete the duplicate records. The TextIn.txt file is an example of the errors from the database log. The TextOut.txt file is the output from the utility. Rename that to a .p file (utdupeglaccts.p) and run it against the database.
