#after installing, inside an existing environment, with 'pip install cellector'
from cellector.io import create_from_suite2p
suite2p_dir = 'D:/Data/2P/suite2p/suite2p' #the directory containing the folders of various planes
roi_processor = create_from_suite2p(suite2p_dir)
#if using the GUI
from cellector.gui import SelectionGUI
gui = SelectionGUI(roi_processor)
#save stuff from the GUI


#alternatively, once you know the settings will be the same across multiple experiments, automate batch processing
from cellector.io import propgate_criteria
from cellector.manager import CellectorManager
# Copy criteria from suite2p_dir to all the other directories
other_directories = [Path(r"C:\Path\to\other\suite2p"), Path(r"C:\Path\to\another\suite2"), ...] # as many as you like
success, failure = propagate_criteria(suite2p_dir, *other_directories)
for directory in other_directories:
    # Make an roi_processor for each session(directory), this will compute features and save the data
    roi_processor = create_from_suite2p(directory) # or whichever method you used to create the roi_processor
    
    # Make a manager instance
    manager = CellectorManager.make_from_roi_processor(roi_processor)
    
    # this will save the updated criteria and idx_selection to cellector directory
    # it will also save empty manual label arrays if they don't exist

    manager.save_all() 
