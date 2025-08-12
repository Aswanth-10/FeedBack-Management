# Built-in Questions Feature

## Overview

The Built-in Questions feature provides pre-defined question templates for different form types in the feedback management system. This feature helps users quickly create forms with relevant questions based on the form type they select.

## Features

### 1. **Form Type-Specific Questions**
Each form type comes with carefully crafted built-in questions:

- **General Feedback** (2 questions)
  - Overall experience rating
  - Additional comments/suggestions

- **Customer Satisfaction** (5 questions)
  - Service satisfaction rating
  - Net Promoter Score (1-10 rating)
  - What they liked most
  - Areas for improvement
  - Would use service again (Yes/No)

- **Employee Feedback** (5 questions)
  - Role satisfaction rating
  - Work-life balance rating
  - Feeling valued by manager (Yes/No)
  - Work motivation factors (multiple choice)
  - Workplace improvement suggestions

- **Product Feedback** (5 questions)
  - Overall product rating
  - Ease of use rating
  - Most valuable features (checkboxes)
  - Problems encountered
  - Would recommend to others (Yes/No)

- **Service Feedback** (5 questions)
  - Service quality rating
  - Team responsiveness rating
  - Staff professionalism rating
  - Most impressive service aspect (multiple choice)
  - Service improvement suggestions

### 2. **Automatic Loading**
- When creating a new form, built-in questions for "General Feedback" are automatically loaded
- Users can see the number of available built-in questions for each form type in the dropdown

### 3. **Smart Form Type Switching**
- When changing form types, users are prompted to confirm if they want to replace current questions
- If no questions exist, built-in questions are loaded automatically
- If questions exist, users can choose to keep current questions or load built-in ones

### 4. **Manual Loading**
- "Load Built-in Questions" button available in both Create and Edit forms
- Can be used at any time to replace current questions with built-in ones
- Confirmation dialog prevents accidental question loss

## User Interface

### Form Creation Page
1. **Form Type Dropdown**: Shows form types with question counts
   - "General Feedback (2 built-in questions)"
   - "Customer Satisfaction (5 built-in questions)"
   - etc.

2. **Questions Section Header**:
   - "Load Built-in Questions" button always visible
   - Allows users to load questions at any time

3. **Empty State**:
   - When no questions exist, shows two options:
     - "Load Built-in Questions"
     - "Add Custom Question"

4. **Enhanced Question Management**:
   - **Insert Questions Anywhere**: "Add Question Here" buttons between existing questions
   - **Position Selector**: Dropdown to move questions to specific positions
   - **Quick Actions**: Up/Down arrows, Duplicate, and Delete buttons
   - **Visual Feedback**: Clear question numbering and enhanced styling

### Form Editing Page
- Same interface as creation page
- Built-in questions can be loaded to replace existing questions
- Confirmation dialog protects against accidental data loss
- All question management features available during editing

## Enhanced Question Management Features

### 1. **Flexible Question Insertion**
- **Add Between Questions**: Click "Add Question Here" buttons that appear between existing questions
- **Add at End**: "Add Question at End" button at the bottom of the question list
- **Smart Positioning**: Questions automatically renumber when inserted

### 2. **Advanced Question Reordering**
- **Up/Down Arrows**: Move questions one position up or down
- **Position Dropdown**: Jump directly to any position in the list
- **Drag-and-Drop Style**: Visual feedback during reordering
- **Auto-Renumbering**: Question numbers update automatically

### 3. **Question Actions**
- **Duplicate**: Copy any question with "(Copy)" suffix
- **Delete**: Remove questions with confirmation
- **Move to Position**: Select exact position from dropdown
- **Tooltips**: Helpful hints for each action button

### 4. **Visual Enhancements**
- **Better Spacing**: Improved layout with proper spacing between questions
- **Action Buttons**: Color-coded buttons (blue for duplicate, red for delete)
- **Hover Effects**: Interactive feedback on all controls
- **Disabled States**: Clear indication when actions aren't available

## Technical Implementation

### File Structure
```
frontend/src/
├── utils/
│   └── builtInQuestions.ts     # Built-in questions data and utilities
├── pages/
│   ├── CreateForm.tsx          # Enhanced with built-in questions
│   └── EditForm.tsx            # Enhanced with built-in questions
```

### Key Functions

#### `loadBuiltInQuestions(formType: string)`
- Returns array of built-in questions for the specified form type
- Automatically sets proper ordering
- Returns empty array for unknown form types

#### `getBuiltInQuestionCount(formType: string)`
- Returns the number of built-in questions available for a form type
- Used in UI to show question counts

#### `handleFormTypeChange(newFormType: string)`
- Handles form type changes with smart question loading
- Shows confirmation dialog when questions exist
- Automatically loads built-in questions when appropriate

#### `addQuestion(insertAtIndex?: number)`
- Adds a new question at the specified position or at the end
- Automatically updates question ordering
- Creates empty question with default settings

#### `moveQuestionToPosition(fromIndex: number, toIndex: number)`
- Moves a question from one position to another
- Handles all reordering logic
- Updates question order numbers

#### `duplicateQuestion(index: number)`
- Creates a copy of the specified question
- Adds "(Copy)" suffix to the question text
- Inserts the duplicate right after the original

#### `moveQuestion(index: number, direction: 'up' | 'down')`
- Moves question one position up or down
- Handles boundary conditions
- Updates question ordering

### Question Types Used
- `rating`: 1-5 star rating
- `rating_10`: 1-10 scale rating (NPS)
- `textarea`: Long text input
- `yes_no`: Yes/No selection
- `radio`: Single choice from options
- `checkbox`: Multiple choice selection

## User Workflow

### Creating a New Form
1. Navigate to Create Form page
2. Built-in questions for "General Feedback" are automatically loaded
3. Change form type if needed (will prompt to load new built-in questions)
4. Manage questions using enhanced controls:
   - **Insert questions**: Click "Add Question Here" between existing questions
   - **Reorder questions**: Use up/down arrows or position dropdown
   - **Duplicate questions**: Click duplicate button to copy questions
   - **Edit questions**: Modify text, types, and options
   - **Delete questions**: Remove unwanted questions
5. Submit form

### Editing an Existing Form
1. Navigate to Edit Form page
2. Existing questions are loaded
3. Optionally load built-in questions using the button
4. Use all question management features:
   - Insert new questions at any position
   - Reorder existing questions
   - Duplicate useful questions
   - Modify question properties
   - Remove unnecessary questions
5. Save changes

### Advanced Question Management
1. **Inserting Questions**:
   - Click "Add Question Here" to insert between questions
   - Click "Add Question at End" to append to the list
   - New questions appear with default settings

2. **Reordering Questions**:
   - Use up/down arrow buttons for single-step moves
   - Use position dropdown for direct positioning
   - Questions automatically renumber

3. **Duplicating Questions**:
   - Click duplicate button (blue icon)
   - Copy appears immediately after original
   - Edit the copy as needed

4. **Managing Question Flow**:
   - Plan question sequence using built-in templates
   - Insert custom questions where needed
   - Reorder for logical flow
   - Remove redundant questions

## Benefits

1. **Faster Form Creation**: Pre-built questions save time
2. **Best Practices**: Questions are crafted based on industry standards
3. **Consistency**: Similar forms use similar question structures
4. **Flexibility**: Built-in questions can be modified or supplemented
5. **User-Friendly**: Clear indicators and confirmations prevent mistakes

## Customization

Users can:
- Modify any built-in question text
- Change question types
- Add/remove answer options
- Reorder questions
- Add additional custom questions
- Remove unwanted built-in questions

## Future Enhancements

Potential improvements could include:
- Admin interface to manage built-in questions
- Industry-specific question templates
- Question suggestions based on form content
- Import/export of question templates
- Multi-language support for built-in questions
