## <remove all of the example text and notes in < > such as this one>

## Functional Requirements <should be 1 sentence that describes requirement>
1. Set notes sorting
2. Create new folder
3. Pin notes
4. Type with voice dication
5. requirement
6. requirement
7. requirement
8. requirement
9. requirement
10. requirement
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
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
 
## Use Cases - name (@username)

## Use Cases - name (@username)

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

