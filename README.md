# Image Processing README

 Django application that handles file uploads (images). The images are uploaded by the user and stored in an SQLite db. The center most pixel of each image is extracted then displayed along with the image. User can view list of uploaded images along with their individual center most pixels (hex value).

 ## 🔬 Features
    1. Upload Image with Image Validation
    2. Extract Center-most pixel of uploaded image
    3. User access gallery(uploaded) images
    4. User access image details by clicking on the image, hex value
    5. CRUD functionality (except for update)
    6. User able to navigate to all endpoints, and be able to scroll from/to any page from/to any page
    7. Error handling for large images
    8. Error handling for non-image file uploads

## 📚 Technologies Used:
    *Python
    *Django
    *HTML
    *CSS

## ⚙ Getting Started:
    1. Clone the repository
    2. Create a virtual environement and install the requirements.txt
    3. Open repository directory in cmd and run
        -python manage.py runserver
    4. Upload image files to extract center most hex values

## Contributors:
    * [Mpetha Sthembiso Motaung] <mpethamotaung@gmail.com>

