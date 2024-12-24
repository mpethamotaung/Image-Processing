# Image Processing README

This Django application handles image file uploads. Uploaded images are stored in an SQLite database. The center-most pixel of each image is extracted and displayed along with its details.

## 🔬 Features
1. Upload images with validation
2. Extract the center-most pixel of uploaded images
3. Access a gallery of uploaded images
4. View image details, including hex values, by clicking on the image
5. CRUD functionality (excluding update)
6. Navigate to all endpoints and scroll between any pages
7. Error handling for large images
8. Error handling for non-image file uploads

## 📚 Technologies Used
* Python
* Django
* HTML
* CSS

## ⚙ Getting Started
1. Clone the repository
2. Create a virtual environment and install the requirements from `requirements.txt`
3. Open the repository directory in the command line and run:
   ```sh
   python manage.py runserver

Changes made:
- Improved the grammar and clarity of the descriptions.
- Organized the features list.
- Corrected typos and formatting issues.
- Added syntax highlighting for the command.
