## Functional Requirements <should be 1 sentence that describes requirement>
1. Set notes sorting
2. Create new folder
3. Pin notes
4. Type with voice dication
5. Save login information
6. Allow notifications
7. Search notes app
8. User will be able to view multiple notes in split-screen mode
9. User will be able to send notes as a PDF via email to a specified recipient
10. User will be able to add photos from their photo library into the note page
11. User will be able to add audio files that are playable inside the body of the notes page
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. Save file
2. non-functional

<each of the 14 requirements will have a use case associated with it>
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
3. a) Site creates a folder with the given name, in the current folder that the selection exists. b) Site displays the folder in the sidebar list, visibly nested in any parent folders. 
4. Site moves the selection into the new folder. 
5. Site opens the new folder, displaying the selected notes/folders within. 
- **Primary Postconditions:** The selected notes/folders have been moved into a new folder (a subfolder). 
- **Alternate Sequence:**
2. User does not type anything and clicks enter. 
3. a) Site creates a folder with the default name "New Folder", in the current folder that the selection exists. b) Site displays the folder in the sidebar list, visibly nested in any parent folders. 
4. Site moves the selection into the new folder. 
5. Site opens the new folder, displaying the selected notes/folders within. 

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
2. a) The site moves the selected note to the pinned section. b) Site sorts the pinned section in accordance with the folder's sorting. 
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
### 1) Save login information
- **Pre-condition:** User has to have an account and the right login information.
- **Trigger:** User successfully logs in.
- **Primary Sequence:**
1. User is asked to create an account or sign in.
2. User successfully creates an account or logs in with an existing account.
3. User is prompted with a pop-up to save their information or not now.
4. User chooses an option and can now use the app.
- **Primary Postconditions:** User is able to use the app.
		              - The next time the user logs in, the information is either saved or not.
					OR
  			      User does not get to use the app because they were not able to create an account or had the incorrect login information.
			      - User has to login. 
- **Alternate Sequence:** 
2. User is not able to create an account or has the incorrect login information.
	a. Screen displays an error message, that login was not successful.
	b. User is asked to input the correct information.

### 2) Allow notifications.
- **Pre-condition:** User should have downloaded the app and logged in.
- **Trigger:** User opens the app for the first time. 
- **Primary Sequence:** 
1. User opens the notes app for the first time.
2. User logs into the notes app or creates an account.
3. User is asked if they want to save their login information.
4. User is asked if they ‘allow’ or ‘don’t allow’ the app to send notifications.
5. User selects an option.
6. User can use the notes app.
-**Primary Postconditions:** User can use the app.
			     - The user receives or doesn't receive notifications from the notes app.
				OR
    			     User can’t use the app.
			     - User has to sign in with the right login information. 
- **Alternate Sequence:** 
2. User is unable to login or sign up, so user isn’t offered the option or allow or not allow notifications. 
	a. User received an error message.
	b. User is prompted to sign in again with the correct information.

### 3) Search notes app.
- **Pre-condition:** There should be at least one file with text in the app. 
- **Trigger:** User selects the search bar. 
- **Primary Sequence:** 
1. User opens notes app.
2. User is successfully signed in.
3. User selects the search bar option.
4. User is able to type in keywords or sentences to search through the existing notes.
5. User can find any file by pressing enter after typing in the words.
- **Primary Postconditions:** User is able to find the file they searched for. 
		              - User can open the file and edit or read it.   
- **Alternate Sequence:** 
4. There are no existing notes to search through. 
	a. Search result shows no files.
	b. User has to create new files. 

### 4) Save file. 
- **Pre-condition:** The user has created a new file or is editing one.
- **Trigger:** User types content into a file. 
- **Primary Sequence:** 
1. User opens the notes app and logs in.
2. User creates a new file or opens an existing one.
3. User edits the file by adding or modifying text.
4. The text and edits done in the file are automatically saved within 1 minute.
- **Primary Postconditions:** The file is the new version with the modified content. 
			      - There is another version added to the history of the file. 
					OR
   			      The file is empty.
		              - File was not saved.
   			      - There is no file because empty files don’t get saved. 
- **Alternate Sequence:** 
3. A file has no text or content.
	a. The notes app is unable to save anything. 


## Use Cases - Emma Dunbach (@edunbach)
### 8) Split View
- Summary: user will be able to navigate between multiple, pre-existing notes with the option to view multiple at the at the same time
- Actors: User and Note App
- Pre-Condition: User must be logged in with one note page already open and another note file already saved
- Trigger: User clicks on another filefrom the side bar
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

### 9) Send Notes
- Summary: User will be able to send note files via email using an export as PDF feature 
- Actors: User, note app, recipient
- Pre-Conditions: User must be logged in 
- Primary Sequence: 
	1. Notes app suggests saving the file 
	2. User saves the file
	3. Notes app prompts the user to enter the recipient's email address
	4. Notes app will prompt the user to add a description or message
	5. Notes app will send a file with the user's name attached as well as the PDF of the note to the recipient
- Alternative Sequence:
	1. User does not save the file
	2. Notes app asks user if they wish to proceed
	3. Notes app prompts the user to enter the recipient's email address
	4. Notes app will prompt user to add description or message
	5. Notes app will send the PDF file of the note page with the user's name attached as well as the note to the recipient
- Post Conditions: 
	1. User's note file will be sent to the specified recipient via email in a PDF
	2. Any unsaved progressed will be sent to the recipient

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
## Use Cases - name (@username)

TEMPLATE FOR USE CASES
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
### 1) Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...

