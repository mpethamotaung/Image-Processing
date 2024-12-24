# Image Processing README

 Django application that handles file uploads (images). The images are uploaded by the user and stored in an SQLite db. The center most pixel of each image is extracted then displayed along with the image. User can view list of uploaded images along with their individual center most pixels (hex value).

 ## Requirements
    1. Setup and Project Config (must allow file uploads)
    2. Model must have 2 fields (image upload & hex charfield)
    3. Image upload processing 
        - Images uploaded through a form
        - Extract center most hex value of image
        - Store uploaded image with it's hex value pair

## 📚Technologies Used:
    *Django 

## ⚙ Getting Started:
    1. Clone the repository
    2. Create a virtual environement and install the requirements.txt
    3. Open repository directory in cmd and run
        -python manage.py runserver
    4. Upload image files to extract center most hex values

## Contributors:
    * [Mpetha Sthembiso Motaung] <mpethamotaung@gmail.com>

