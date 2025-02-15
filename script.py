#!python3

import sys


print(sys.version)

'''
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
# Regular Imports

import os, sys, math, datetime, time # Regular Imports

# Import - Standard library (pandas, Revit API, Forms from RevitPythonShell, pyRevit for UI)
import pandas as pd
from Autodesk.Revit.DB import *
# FilteredElementCollector, BuiltInCategory, Transaction, FamilyManager, ExternalDefinitionCreationOptions, SharedParameterElement

from Autodesk.Revit.UI import *
# TaskDialog

from Autodesk.Revit.ApplicationServices import Application
from Autodesk.Revit.Attributes import TransactionMode, RegenerationOption
# from RevitPythonShell import Forms

# pyRevit
from pyrevit import revit, forms, script # type: ignore # import pyRevit modules.

# Custom Imports
# from Snippets._selection import get_selected_elements # lib import
# from Snippets._convert import convert_internal_to_m # lib import


__title__ = "AddScheduleParams" # Name of the button displayed in Revit UI
__doc__ = """
Version = 1.0
Date = 14.02.2025
_____________________________________________________________________
Description:
Adds shared parameters to the family based upon the design data required to appear in slected schedules.
_____________________________________________________________________
How-to:
-> Coming soon
_____________________________________________________________________
Last update:
- [14.02.2025] - 1.0 BETA
_____________________________________________________________________
Author: Joel Christopher""" # Button Description shown in Revit UI

# EXTRA: You can remove them.
__author__ = "Joel Christopher" # Script's Author
#__helpurl__ = "https://github.com/baptistelechat/pyrevit-with-vscode" # Link that can be opened with F1 when hovered over the tool in Revit UI.
__min_revit_ver__ = 2023 # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
__max_revit_ver__ = 2025 # Limit your Scripts to certain Revit versions if it's not compatible due to RevitAPI Changes.
# __highlight__ = "new" # Button will have an orange dot + Description in Revit UI ("new" | "updated"
# __context__ = [ "selection", "active-section-view"] # Make it available only if Active view is Section and something is Selected
# __context__     = ["Walls", "Floors", "Roofs"] # Make your button available only when certain categories are selected. Or Revit/View Types.

# 🔗 For extra bundle metadata: https://pyrevitlabs.notion.site/Bundle-Metadata-9fa4911c14fa49c48e715421400f1427
# 🔗 For extra bundle context: https://pyrevitlabs.notion.site/Bundle-Context-630fa1f3611f4ee0aa15d290275e7ef3


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================
doc   = __revit__.ActiveUIDocument.Document # type: ignore # Document class from RevitAPI that represents project. Used to Create, Delete, Modify and Query elements from the project.
uidoc = __revit__.ActiveUIDocument # type: ignore # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app   = __revit__.Application # type: ignore # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings.
rvt_year = int(app.VersionNumber) # Get current revit version.
PATH_SCRIPT = os.path.dirname(__file__) # Absolute path to the folder where script is placed.

# GLOBAL VARIABLES
# - Place global variables here.
logger = script.get_logger()

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ==================================================
# - Place local functions here. If you might use any functions in other scripts, consider placing it in the lib folder.

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ==================================================
# - Place local classes here. If you might use any classes in other scripts, consider placing it in the lib folder.

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
# ==================================================
# For input display: https://pyrevitlabs.notion.site/Effective-Input-ea95e95282a24ba9b154ef88f4f8d056
# For output display: https://pyrevitlabs.notion.site/Effective-Output-43baf34d2ca247ada8e040bcb86613a2
# For data visualization: https://pyrevitlabs.notion.site/Visualizing-Data-fd778a0b67354ff581aa340619b87803

if __name__ == '__main__':
    # START CODE HERE

    # AVOID  placing Transaction inside of your loops! It will drastically reduce performance of your script.
    t = Transaction(doc,__title__) # type: ignore # Transactions are context-like objects that guard any changes made to a Revit model.

    # You need to use t.Start() and t.Commit() to make changes to a Project.
    t.Start() # <- Transaction Start

    #- CHANGES TO REVIT PROJECT HERE
    

    t.Commit() # <- Transaction End

    # Notify user that script is complete.
    logger.success(':chequered_flag: Script is finished.')
    print('-' * 50)
    print(':page_facing_up: Template has been developed by Baptiste LECHAT and inspired by Erik FRITS.')






# Import/load data from excel file
    # Store all worksheet names in a set

# Create multiselect list box to select schedules that apply to the family
    # Populate with the worksheet names from the set

# User selects element(s)

# Call function to open list box for selection of schedules

# User selects schedules

# Iterate over the selected schedules
    # If the current index selected schedule exists in the worksheet name set
        # Extract the SP_Names, SP_Groups, BIPGS, SP_Inst, SP_Categories for the selected schedules
    # Else,
        # Throw a warning message to the user that the worksheet name was not found in the excel file

# Iterate over the extracted shared parameters
    # If the current index SP_Categories matches the family category of the selected element(s),
        # Store the SP in a list for adding to the family
    # Else,
        # Store the SP in a list of excluded parameters

# Option 1: Iterate over each selected family
    # Check if the family already contains the required parameters
    # If parameters are missing:
        # Open the family (only if necessary)
        # Start a single transaction for all modifications
        # Add shared parameters to the family
        # If parameters were added, reload the family into the project
        # Confirm override only if changes were made
        # Close the family

# Option 2 (LESS EFFICIENT): Iterate over each family that was selected
    # Open the family
    # Add the SPs to the family from the variable that stores the SPs to be added to the family
    # Load the family back into the main project without saving the family
    # Confirm override of the existing family in the main project
    # Close the family

# If the SPs that were not added to the family is not empty
    # Throw a warning message to the user that the SP is not applicable to the selected element(s) and was not added to the family

'''