# Open the data files.
fileIn = open('TextIn.txt', 'r')
fileOut = open('TextOut.txt', 'w')

#Loop thru file.
for line in fileIn:

    # Get the info from the line.
    words = line.split()            # Split the line into words.
    recid = words[2]                # The third element is the RecID.
    recid = recid.replace(",", "")  # Remove the trailing comma.
    table = words[3]                # The fourth element is the table.

    # Build Progress ABL lines of code.
    ablFind = "FIND FIRST " + table + " WHERE RECID(" + table + ") = " + recid + " NO-ERROR.\n"
    ablDelete = "IF AVAILABLE(" + table + ") THEN DELETE " + table + ".\n"

    # Write the code to file.
    fileOut.write(ablFind)
    fileOut.write(ablDelete)

# Close the data files. 
fileIn.close()
fileOut.close()
