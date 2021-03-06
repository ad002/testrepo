
#just start your shell, move to desktop and creat a local repository with "mkdir" command
# mkdir <directoryname>

#then create a file with "touch" command
# touch <filename>.txt/.py 


#If you don't want to create repos via shell start here:
#Move to your directory via "cd" command
#cd /home/pi/Desktop

#then creat a hidden git-log file with "git init" command 
#git init 

#Now you can check the status of your working files via "git status" command 
#git status

#Now it's time to create a new branch. Think of it like creating a "local checkpoint" like "save as". 
#git branch <branch-name>

#-> More commonly used is creating a checkpoint in form of commits
#Once you've worked on your files it's time to commit them. Via "git commit -m <"your message"> command
#But first, you have to stage them via "git add" command. This will mark any changes you've made
#git add <files>
#If you're fine with the changes, commit them via: 
#git commit -m "this is my first commit"

#Now you can create a repo on GitHub (manually). 
#and then, you can push your files to that repo (once commited) 
#git remote add origin https://github.com/ad002/testrepo.git
#git push -u origin master

#if you get like an "error: src refspec master does not match any."
#Just recheck whether you've committed before! 
#git commit -m "this is my commit"
#git push -u origin master



#The original folder is now referred to as your working direcoty as opposed to the 
#repository (the .git) folder that tracks your changes. You WORK in the WORKING dir. Simple!

#Now you can either download an existing GitHub Repo. 


