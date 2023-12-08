# cmpe131_team7_project
- Emma Dunbach (@edunbach): Split View, Add Images, Add Audio Files
- Nathan Largo (@nLargo): Create New Folder, Sort Notes, Search Notes, Voice Dictation
- Priya Nahal (@PriyaNahal): Save Notes, Delete Notes, Save Login Information
- Vinh Huynh (@vinhhuynh09) (Team Lead): Login, Create Account, Create New Note, Logout, Multilingual Support

# Ethical Implications:
Some ethical considerations our team made prior to building the notes app was primarily based around security. In a societal context, users will not want others to be able to read their notes without permission because they could have written sensitive/personal material (ie. a diary). Our app also has the capabilities to support multiple languages as we try to integrate this new note-taking method on a global scale. Furthermore, we carefully considered any and all environmental impacts--one of which that an app could relieve is the overuse of paper materials. Though using a notes app will not completely resolve any environmental problem, the hope is that there will be enough users that prefer an app over paper and pencils to eliminate deforrestation for the purpose of merely taking a quick note. Finally, a note-taking app should be economically sustainable. As engineers, we have to raise the concern that there may be a plethora of individuals who lack funds for a device with note-taking capabilities. That being said, those who already own a device with said capabilities will not have to pay for writing utensils and paper ever again. In summary, our note-taking app considers many ethical situations, yet it focuses on the issues of security, the environment, global integration, and even economics that are at stake with traditional pen and paper note-taking.

# Required Libraries:
To run this app you will need the following libraries:
1. Flask
2. SQL Alchemy
3. Flask Login
4. wtforms

These can be install using these commands:
$ install flask
$ install flask-sqlalchemy
$ install flask-login
$ install flask-wtf

# How to Run the App:
One all the files have been downloaded from the GitHub repository, enter this in the terminal to run the program:
$ python3 run.py

# How to Use the App:
Once the app begins running, click on the link that pops up that should be: http://127.0.0.1:5000

You will first be displayed with the login page and an option to create an account if you do not have an account.

Once you create an account or login in, you have all access to the notes app.

# Some of the available features include:
1. New to the application? You can create an account and begin writing notes!
2. Have something on your mind that you want to jot down? You can create a new note! A fresh page will be available for you to type in. Please note that the note cannot include ENTER key. The note must be entered as a paragraph.
3. Done for the moment and want to not lose what is in your current note? You can save save your notes! This way, you can have access to it again in the future.
4. Want to multitask on the application? Split screen view is available allowing you to view and edit two different notes at the same time for convenience!
5. Want to view your notes in a certain order? You can sort your notes via date edited, date create, and alphabetically making it easier to look for certain notes!
6. Looking for a certain note you cannot find? You can simply type the title of the note to search for it! 
7. Want to add something other than text? You can add images and audio files to your notes!
8. Too lazy to type to enter text into your notes? You can use voice dictation by simply speaking and it will be transcribed to text in your notes!
9. Want to get rid of a note you no longer need? You can delete certain notes!
10. Want to organize your notes? You can create folders to organize which notes are stored where!
11. Done for the day? You can logout and log back in the next time!
