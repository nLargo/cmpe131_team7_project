# cmpe131_team7_project
- Emma Dunbach (@edunbach): Split View
- Nathan Largo (@nLargo): Create New Folder, Sort Notes
- Priya Nahal (@PriyaNahal): Save Notes, Delete Notes
- Vinh Huynh (@vinhhuynh09) (Team Lead): Login, Create Account, Create New Note, Logout 

# Ethical Implications Milestone 2:
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

Please note: There currently is not button that goes to /my-notes page so you will need to manually enter that into the URL to test the requirements on that page.

Some of the available features include:
1. Creating a new note that will have a fresh blank page for you to type on.
2. Save a note after you type whatever you want in the note so you can refer to it again in the future.
3. Split screen view allowing you to view two different notes at the same time for convenience if needed.
4. Sorting notes to make it easy to look for a certain note if needed.
5. Adding images to notes if needed.
6. Deleting notes to get rid of text that is no longer needed.
7. Logout which allows you to sign out and login the next time when you are finished using the app for the time being.
