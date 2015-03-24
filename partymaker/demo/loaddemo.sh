#Wipe out all existing data in the database.....yeah.....don't mess around
../manage.py flush <<TRM
yes
TRM
#Load the demo data in
../manage.py shell <<TRM
execfile("setup.py")
TRM
