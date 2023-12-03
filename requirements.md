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
11. User will be able to search for notes.
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
- **Trigger:** User checks on the "Remember Me" icon.
- **Primary Sequence:**
1. User clicks "Login".
2. Application saves user login information.
3. Next time user logs in, user selects their username under username and password will automatically be entered.
- **Primary Postconditions:** User is able to use the app and remains signed in.

### 6) Save notes
- **Pre-condition:** User creates a note.
- **Trigger:** User hovers over to the save icon. 
- **Primary Sequence:**
1. User clicks the save button.
2. User adds a title and has text in the note.
3. Note is saved in the application.

- **Primary Postconditions:** User views the home page with all the saved notes shown.

### 7) Delete notes
- **Pre-condition:** User saves a note. 
- **Trigger:** User hovers over the delete icon. 
- **Primary Sequence:**
1. User clicks on the delete note icon.
2. User selects note that they want to delete.
3. Application permanently deletes the note.
4. User will not be able to view the note on the home page.

- **Primary Postconditions:** User is directed to the home page.  
- **Alternate Sequence:** 
1. User attempts to delete a note when there is no note to delete.
2. Application does not delete any files.
3. User must create a new note before trying to delete a note.

## Use Cases - Emma Dunbach (@edunbach)
### 8) Split View
- **Pre-condition:** User must be logged in with one note page already open and another note file already saved.
- **Trigger:** User clicks on another file from the side bar.
- **Primary Sequence:**
	1. Notes app prompts user to choose to view full screen or split screen.
	2. User chooses to split screen view
	3. Notes app opens page with an identical screen on the same page.
	4. User can multitask with working on two different notes on the same page.
- **Primary Postconditions:** 
	1. User is able to view multiple notes in split screen mode OR user views newly selected note file in full screen mode.

### 9) Log Out
- **Pre-condition:** User must be logged in 
- **Trigger:** User clicks on logout icon in window
- **Primary Sequence:** 
	1. Notes app logs user out of account.
	2. User will be redirected to the login page.
	3. User will need to log in again if they want to access their notes.
- **Primary Postconditions:** 
	1. User has been logged out of their account.

### 10) Add Photos
- **Pre-condition:** User must be logged in and have photos on the device
- **Trigger:** User selects the photo button 
- **Primary Sequence:**
	1. Notes app opens a collection of various photos that can be added to the note.
	2. User selects photo they want to add.
	3. Notes app imports the photo into the note file.
 	4. The selected photo is displayed in the note and can be saved.
 - **Alternate Sequence:** 
	1. User chooses to cancel insert photo option
	2. Notes app will close the photo album.
- **Primary Postconditions:** 
	1. User's note displays photos that were imported into the specified note file.

### 11) Search Notes
- **Pre-condition:** User must be logged in and have existing notes.
- **Trigger:** User hovers over to the search bar and clicks it.
- **Primary Sequence:**
	1. User types the title of the note they are looking for.
	2. Application sorts through notes based on the characters entered.
	3. Application displays a list of note titles that match the characters entered.
	4. User clicks on the note they want to view.
- **Alternate Sequence:** 
	1. User types the title of the note they are looking for.
	2. Application sorts through notes based on the characters entered.
	3. Application cannot find any notes based on the characters entered.
	4. Application does not display any notes found.
- **Primary Postconditions:**
	1. Application displays the note user searched for OR application stays on home page.
  
## Use Cases - Vinh Huynh (@vinhhuynh09)
### 12) Create Account
- **Pre-condition:** User launches the notes application.
- **Trigger:** User clicks the "Create Account" icon if they do not have an account.
- **Primary Sequence:**
1. Application displays a create account page.
2. Application asks for user's name, email, username, password, and confirm password.
3. User enters these following information.
4. User clicks on the "Create Account" icon.
- **Primary Postconditions:** Application logs the user into their new account and has access to the application.
- **Alternate Sequence:**
1. User enters an invalid email or the passwords entered do not match.
2. Application will prompt the user that email is not valid and/or passwords do not match.
3. User will not be able to successfully create an account until information is entered correctly.

### 13) Login Account
- **Pre-condition:** User launches the notes application.
- **Trigger:** User hovers over the username text bar on the login page and clicks on it.
- **Primary Sequence:**
1. User types their username.
2. User hovers over the password text bar and clicks on it.
3. User types their password.
4. User clicks the "LOGIN" icon.
5. Application validates that username and password entered are correct.
6. Application successfully logs the user into their account.
- **Primary Postconditions:** User gets redicted to the home page.
- **Alternate Sequence:**
1. User enters invalid username and/or password.
2. Application prompts user that the wrong username and/or password has been invalid and does not log user in.

### 14) Create Notes
- **Pre-condition:** User loads all their existing notes.
- **Trigger:** User clicks on the icon “+” icon to create a new note.
- **Primary Sequence:**
1. Application displays a new empty note.
2. User enters the title of the note.
3. User enters information in the note.
- **Primary Postconditions:** Application creates the new note and can be viewed.
