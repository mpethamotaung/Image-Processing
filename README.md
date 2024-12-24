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
1. Clone the repository.
2. Create a virtual environment using recommended 'python 3.12.8' I have not tested it on any other Python version.
3. Install the requirements from `requirements.txt` in your virtual environment.
4. Open the repository directory in the command line and run:
   ```sh
   python manage.py runserver
5. I've included a pics folder for your convenience 'app_test_images' or you can use your images to test the app.
> If you have any issue, please check the technical documentation: https://github.com/mpethamotaung/Image-Processing/blob/main/Pixel%20Project%20(Techical%20Documentation)%20v1.0.docx

Changes made:
- Improved the grammar and clarity of the descriptions.
- Organized the features list.
- Corrected typos and formatting issues.
- Added syntax highlighting for the command.
