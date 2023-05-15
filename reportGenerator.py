# -*- coding: utf-8 -*-
"""
    This script is a REPORT GENERATOR. It uses a low-level of 
    DYNAMIC CODING. This means that this script can generate a report
    containing selected data from ANY "FLAT" FILE provided that:
        (a) The file can be read using Panda's read_csv function
        (b) The file contains data than can be used to create a "clean"
            DataFrame object.
"""
# Import the Pandas library; thislibrary is used throughout, so imported here
import pandas as pd


"""
    In INTERPRETED (SCRIPT) LANGUAGES, functions must be fully defined
    BEFORE they are used. 
    
    Function definitions should be organized based on some sort of system.
    It is common to order them either (a) in the order called or 
    (b) alphabetically. Other systems could also be used, as long as the 
    organization is clear.
    
    It is also important to DOCUMENT each function with respect to inputs,
    outputs, and general processing methods. This sort of documentation 
    makes the reuse and repurposing of functions much easier.
"""

def createFrame( ) -> pd.DataFrame:
    """
    Parameters
    ----------
     None

    Returns
    -------
    dataFrame : Pandas DataFrame
        A DataFrame object containing the parsed data from an input
        file identified by the user
    
    Process
    -------
    1. Prompt the user for a file name and a separator value.
    2. Call Pandas read_csv, passing the file name and separator value.
    3. Return the newly instantiated & loaded DataFrame object to the caller.

    """
    print( "Select File and File Format for Reporting" )
    # Prompt for filename
    fileName = input( "Enter the name of the input file with extension: \n" )
    # Prompt for separator value
    separator = input( "Enter the separator character(s): \n" )
    
    # If no separator was entered, assume comma
    if ( len(separator) == 0 ):
        separator = ','
    # end selection
    
    # Mirror input back to user
    print( "The file you have selected for reporting is: \t%s" %
            fileName )
    print( "You have indicated that the separator is: \t%s" %
           separator )
    
    # READ the file and INSTANTIATE a DataFrame object
    outFrame = pd.read_csv( fileName, 
                            sep = separator )
    
    # RETURN the DataFrame object to the CALLER
    return outFrame
# END OF FUNCTION createFrame


def selectColumns( inFrame: pd.DataFrame ) -> list:
    """
    Parameters
    ----------
    inFrame : pd.DataFrame
        DESCRIPTION.

    Returns
    -------
    list
        List object containing user-selected column labels
    
    Process
    -------
    1. Retrieve column labels from DataFrame passed into Function
    2. Display column labels and prompt user for selection
    3. Mirror selection to user
    4. "Parse" selection using Regular Expression into List of column labels
    5. Return List of column labels to caller

    """
    print( )
    print( "Select columns for reporting." )
    
    # Retrieve List of column labels from the passed DataFrame object
    colList = inFrame.columns
    
    # Provide the labels to user so user may select desired column(s)
    print( "These are the available column labels: " )
    print( colList )
    
    # Prompt the user to select desired column(s)
    print( "Type in the names of the columns that should appear in the report." )
    selection =                                                               \
      input( "Please separate names with commas:\n" )
    
    # Mirror input to user
    print( )
    print( "The following columns will appear in this order: " )
    print( selection )
    
    """
        The following is a slightly enhanced way to "parse" the user-typed 
        list of column labels
    """
    # Import the Regular Expression engine/package; it is ONLY used in here
    import re
    
    # "Split" the input String based on a RegEx for a variety of separators
    regEx = ", |,|\n"  # Separators: comma + space, comma, new line
    outList = re.split( regEx,
                        selection )
    
    # Return List of column labels to caller
    return outList
# END OF FUNCTION selectColumns


def generateReport( inFrame: pd.DataFrame,
                    inList:  list ):
    """
    Parameters
    ----------
    inFrame : pd.DataFrame
        DESCRIPTION.
    inList : list
        DESCRIPTION.

    Returns
    -------
    None.
    
    Process
    -------
    1. Calls the loc method on the passed DataFrame object to create a view
        a. Limits row selection to the first 100 rows of data
        b. Passes List of columns labels to slice columns
    2. Removes row and column limitations w/in a defined context
    3. Print the contets of the view created in step 1 w/in scoped context

    """
    print( )
    print( "Generating your report." )
    print( "\n\n" )
    print( "\t\tRequested Report, 100 Rows of Data" )
    
    # We will keep the 100 row limit here for convenience.
    # It would be BETTER to ASK the user about how many rows, though...
    rptView = inFrame.loc[ :99 , inList ]
    
    with pd.option_context( 'display.max_rows', None,
                            'display.max_columns', None ):
        print( rptView )
    # end CONTEXT
# END FUNCTION generateReport


"""
    Now that we have defined all the functions we will use, 
    we can write the script to EXECUTE those functions
"""

# Call the function to CREATE the DataFrame
myFrame = createFrame( )

# Call the function to SELECT COLUMNS
myCols = selectColumns( myFrame )

#Call the function to PRINT the REPORT (to the console)
generateReport( myFrame,
                myCols )



