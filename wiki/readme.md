# Wikify tasks

An explanation of this project and the scripts within it:
* tasks.csv: Contains a list of tasks following the taskman format
  * This list has been shortened significantly for public display
* csvTasks_to_wml.py: Takes the info from the CSV file and converts each entry into a new file, pre-formatted using the appropriate WML templates
* createRedirects.py: Serves the same purpose as "csvTasks_to_wml.py", but creates wiki redirects for each task's ID
* create_filelist.bat: Iterates through the files created by the aforementioned Python-scripts, and adds their names to a single text file

After running the scripts in the above order, the script and text file can be loaded into AutoWikiBrowser (AWB) to automate the creation of every page. If a page already exists, it can be skipped via the appropriate AWB settings.
