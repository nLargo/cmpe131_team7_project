## Functional Requirements
1. Notes app should allow user to set notes sorting.
2. Notes app should allow user to create new folder.
3. Notes app should allow user to pin notes.
4. Notes app should allow user to type with voice dication.
5. Notes app should allow user to save login information.
6. Notes app should allow user to save notes.
7. Notes app should allow user to delete notes.
8. User will be able to view multiple notes in split-screen mode.
9. User will be able to log out of their account using a logout button.
10. User will be able to add photos from their photo library into the note page.
11. User will be able to add audio files that are playable inside the body of the notes page.
12. Notes app should allow user to create an account.
13. Notes app should allow user to log into their account.
14. Notes app should allow users to create notes.

[1-4, 9-11](images/ui-home-page-1.png)
[5](images/ui-save-login.heic)
[6](images/ui-notifications.heic)
[7](images/ui-search-example.png)
[7, 8, 14](images/ui-home-page-2.png)
[12, 13](images/ui-login-page.png)

## Non-functional Requirements
1. Notes app should save file within 30 seconds.
2. Notes app should include multilingual support.

## Use Cases - Nathan Largo (@nLargo)
### 1) Set notes sorting
- **Pre-condition:** The user must be logged in and on the notes page.
- **Trigger:** The user clicks the ‘Sort By’ dropdown button.
- **Primary Sequence:**
1. a) The site displays a dropdown menu with the sort options, “Date Edited” (default), “Date Created”, and “Title”. b) Beside each option, is an ascending/descending order toggle button.
2. User selects a sort option.
3. The dropdown menu closes.
4. Site sorts the notes according to the user’s selection.
- **Primary Postconditions:** The user’s notes are ordered according to their selection.
- **Alternate Sequence I:**
2. User toggles the ascending/descending order button beside the current sort option.
3. The dropdown menu closes.
4. Site sorts the notes according to the user’s selection.
- **Alternate Sequence II:**
2. User toggles the ascending/descending order button beside a sort option that isn’t currently selected.
3. Site auto-selects the sort option beside the toggled button.
4. The dropdown menu closes.
5. Site sorts the notes according to the user’s selection.

### 2) Create new folder
- **Pre-condition:** The user must be logged in and have at least 1 note/folder.
- **Trigger:** The user clicks "New Folder" while selecting 1 or more notes/folders.
- **Primary Sequence:**
1. The site prompts the user with a textbox to name the new folder.
2. User types and enters a name.
3. a) Site creates a folder with the given name. b) Site displays the folder in the sidebar list.
4. Site moves the selection into the new folder.
5. Site opens the new folder, displaying the selected notes within.
- **Primary Postconditions:** The selected notes have been moved into a new folder.
- **Alternate Sequence:**
2. User does not type anything and clicks enter.
3. a) Site creates a folder with the default name "New Folder". b) Site displays the folder in the sidebar list.
4. Site moves the selection into the new folder.
5. Site opens the new folder, displaying the selected notes within.

### 3) Pin notes
- **Pre-condition:** The user must be logged in and have at least 1 note.
- **Trigger:** The user clicks "Pin" while selecting 1 or more notes.
- **Primary Sequence:**
1. The site designates a 'pinned' section at the top of the list of notes.
2. Site moves the selected note to the pinned section.
3. Site displays a pin icon on the note to indicate it's pinned.
- **Primary Postconditions:** The selected note is pinned to the upper portion of the list.
- **Alternate Sequence:**
1. The pinned section already exists and has pinned notes already.
2. a) The site moves the selected note to the pinned section.b) Site sorts the pinned section in accordance with the folder's sorting.
3. Site displays a pin icon on the note to indicate it's pinned.

### 4) Type with voice dictation
- **Pre-condition:** The user must be logged in and have a note open and editable.
- **Trigger:** The user clicks the 'voice dication' button.
- **Primary Sequence:**
	1. The site indicates that it is listening and listening for speech.
	2. User speaks.
	3. The site transcribes the speech in real time.
	4. The user clicks the voice dictation button again.
	5. The site indicates that listening is now off and stops listening.
- **Primary Postconditions:** The user's speech has been transcribed in real-time to the current note.
- **Alternate Sequence:**
4. The user does not click the voice dictation button again.
5. After 3 minutes of transcribing, the site stops listening and indicates that listening is now off.
6. The site checks if the user is still there, prompting the user to click the voice dictation button again to continue speech-to-text. 
 
## Use Cases - Priya Nahal (@PriyaNahal)
### 5) Save login information
- **Pre-condition:** User enters valid login information.
- **Trigger:** User clicks on the "Login" icon.
- **Primary Sequence:**
1. A pop-up asks whether the user wants to save their login information or not.
2. User selects "Yes" if they do want their information saved.
3. Application will save the user's login information.
- **Primary Postconditions:** User is able to use the app and remain signed in.
- **Alternate Sequence:**
1. A pop-up asks whether the user wants to save their login information or not.
2. User selects "No" if they do not want their information saved.

	**a)** Application will not save the user's login information.

### 6) Save notes
- **Pre-condition:** User creates a note.
- **Trigger:** User hovers over to the save icon. 
- **Primary Sequence:**
1. User clicks the save button.
2. User adds a title and has text in the note.
3. Note is saved in the application.

- **Primary Postconditions:** User views the home page with all the saved notes shown.
- **Alternate Sequence:** 
1. User clicks the save button.
2. User enters a title.
3. Note is not saved because there was no text.

### 7) Delete notes
- **Pre-condition:** User saves a note. 
- **Trigger:** User hovers over the delete icon. 
- **Primary Sequence:**
1. User clicks on the delete note icon.
2. User selects note that they want to delete.
3. Application deletes the note.

- **Primary Postconditions:** User is directed to the home page.  
- **Alternate Sequence:** 
1. There are no existing notes to delete or user doesn't create a new note.
  
	**a)** User has to create new files. 

## Use Cases - Emma Dunbach (@edunbach)
### 8) Split View
- Summary: user will be able to navigate between multiple, pre-existing notes with the option to view multiple at the at the same time
- Actors: User and Note App
- Pre-Condition: User must be logged in with one note page already open and another note file already saved
- Trigger: User clicks on another file from the side bar
- Primary Sequence:
	1. Notes app prompts user to choose to view full screen or split screen
	2. User chooses to split screen view
	3. Notes app automatically opens the selected file next to the open file
- Alternative Sequence: 
	1. User chooses to view notes in full screen view
	2. Notes app opens selected file in full screen
	3. Previously open file is idling in background
- Post Conditions: 
	1. User is able to view multiple notes in split screen mode
	2. User views newly selected note file in full screen mode

### 9) Log Out
- Summary: User will be able to log out of their account using a logout button
- Actors: User, note app
- Pre-Conditions: User must be logged in 
- Trigger: User clicks on logout icon in window
- Primary Sequence: 
	1. Notes app opens a window asking if the user would like to save the current file(s)
	2. User saves the file
	3. Notes app shows logout screen
 	4. Notes app will have a button to go back to login page
- Alternative Sequence:
	1. User does not save the file
	2. Notes app asks user if they wish to proceed
	3. Notes app shows logout screen
	4. Notes app will have a button to go back to login page
- Post Conditions: 
	1. User's account will be logged out
 	2. User can log in and log out as many times as they please

### 10) Add Photos
- Summary: User will be able to import photos into the open note page
- Pre-Condition: User must be logged in and have photos on the device
- Trigger: User selects the photo button 
- Primary Sequence: 
	1. Notes app opens photo album from the device
	2. User selects photo from personal photo library
	3. Notes app imports the photo into the note file with options to resize and move within the page
 - Alternative Sequence: 
	1. User chooses to cancel insert photo option
	2. Notes app will close user's photo album
- Post Conditions: 
	1. Notes app shows User's photos that were imported into the specified note file
	2. Photos can be resized and moveable

### 11) Add Audio
- Summary: User will be able to import audio files into the selected note
- Pre-Condition: User must be logged in and have mp3 files on the device
- Trigger: User selects button to add audio file
- Primary Sequence:
	1. Notes app opens files in device
	2. User selects audio file to import
	3. Notes app will insert file into the body of the note page
	4. Audio file will have the option to play inside the note page
- Alternative Sequence: 
	1. User decides not to insert file
	2. User cancels insert function
	3. Notes app will close out the user's file page
- Post Conditions:
	1. User will have audio file within the body of the note page
	2. Audio file will be playable
  

## Use Cases - Vinh Huynh (@vinhhuynh09)
### 12) Create Account
- **Pre-condition:** User launches the notes application.
- **Trigger:** User clicks the "Create Account" icon if they do not have an account.
- **Primary Sequence:**
1. Application displays a pop-up that asks for the user's first name, last name, email/username, and password.
2. User enters these following information.
3. User clicks on the "Create Account" icon.

- **Primary Postconditions:** Application logs the user into their new account and has access to the application.
- **Alternate Sequence:**
1. Application displays a pop-up that asks for the user's first name, last name, email/username, and password.
2. User decides not to create an account.
	a. User clicks on the "X" icon to exit the pop-up.

### 13) Login Account
- **Pre-condition:** User launches the notes application.
- **Trigger:** User hovers over the username text bar on the login page and clicks on it.
- **Primary Sequence:**
1. User types their username.
2. User hovers over the password text bar and clicks on it.
3. User types their password.
4. User clicks the "LOGIN" icon.
5. Application successfully logs the user into their account if correct information is entered.

- **Primary Postconditions:** User can begin to use the application.
- **Alternate Sequence:**
1. User types their username.
2. User hovers over the password text bar and clicks on it.
3. User types their password.
4. User clicks the "LOGIN" icon.
5. Application prompts user that invalid information is entered and cannot log user in.

### 14) Create Notes
- **Pre-condition:** User loads all their existing notes.
- **Trigger:** User clicks on the icon “+” icon to create a new note.
- **Primary Sequence:**
1. Application displays a pop-up that asks the user for the name of the note.
2. User enters the name of the note.
3. User clicks “OK”.

- **Primary Postconditions:** Application creates the new note and can be viewed.
- **Alternate Sequence:**
1. Application displays a pop-up that asks the user for the name of the note.
2. User decides to not create a new note.
3. User clicks “CANCEL”.
