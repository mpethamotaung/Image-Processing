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
* Javascript
* Figma

## ⚙ Getting Started
1. Fork the repository.
2. Create a virtual environment (pyenv, virtualenv, anaconda, etc) using recommended 'python 3.12.8'
  **Anaconda**
   Create an environment
     ```sh
     conda create --name <my-env>

3. Install the requirements from `requirements.txt` in your virtual environment.
   
   ```sh
   pip install -r /path/to/requirements.txt
4. Open the repository directory '(local_instance)/image-processing/pixelsproject/' in the command line (in your IDE of choice) and run:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
5. The default development server address is:  'http://127.0.0.1:8000/'
6. Navigate to 'upload image' in the navbar and upload image(s)
7. I've included a pics folder for your convenience 'app_test_images' or you can use your images to test the app.
   
   **Note:** These pics are licensible 
   
> If you have any issues, please check the technical documentation: https://github.com/mpethamotaung/Image-Processing/blob/main/Pixel%20Project%20(Techical%20Documentation)%20v1.0.docx

## 🔎 Changes made:
- Improved the grammar and clarity of the descriptions.
- Organized the features list.
- Corrected typos and formatting issues.
- Added syntax highlighting for the command.

```
Image-Processing
├─ demo
│  ├─ Pixel Extractor 1.0.mp4
│  ├─ Pixel Extractor 2.0.mp4
│  ├─ Pixel Extractor 3.0.mp4
│  └─ Pixel Extractor 4.0.mp4
├─ LICENSE
├─ Pixel Project (Techical Documentation) v1.0.docx
├─ PixelsProject
│  ├─ db.sqlite3
│  ├─ manage.py
│  ├─ media
│  │  └─ uploads
│  │     ├─ 5-7-2020-6-13-23-pm.png
│  │     ├─ 5-7-2020-6-13-23-pm_O8LPHzu.png
│  │     ├─ 5-7-2020-6-13-23-pm_ynMQOpa.png
│  │     ├─ 6630c5c05d445045bf6bfd74_fireship.webp
│  │     ├─ 76e5d55d0c8c6ec65135b42a2c5cbd98.jpg
│  │     ├─ 79393c76508a709952f421002f189218.jpg
│  │     ├─ barnaby-K78ECC0F1YI-unsplash.jpg
│  │     ├─ barnaby-K78ECC0F1YI-unsplash_69RVsfV.jpg
│  │     ├─ bumblebee_wide-43b22617e34292ad8cbdc79931fe099677c7802b.jpeg
│  │     ├─ c7-scaled.webp
│  │     ├─ chopped-green-salad-with-herby-chilli-dressing-0bc8e57.jpg
│  │     ├─ dusty-rose.jpg
│  │     ├─ emanuel-haas-P0ck7wsVAag-unsplash.jpg
│  │     ├─ fiery_lava_acrylic_fluid_art_painting_1.webp
│  │     ├─ gluten-free-diet-teaser.jpg
│  │     ├─ gratisography-augmented-reality-800x525.jpg
│  │     ├─ gratisography-cool-cat-800x525.jpg
│  │     ├─ hq720.jpg
│  │     ├─ hq720_a2ytppD.jpg
│  │     ├─ hq720_SpmcX7H.jpg
│  │     ├─ IMG_0076.JPG
│  │     ├─ IMG_0140.JPG
│  │     ├─ IMG_0513.GIF
│  │     ├─ IMG_0538.JPG
│  │     ├─ IMG_0541.JPG
│  │     ├─ IMG_0915.JPG
│  │     ├─ IMG_1056.JPG
│  │     ├─ IMG_1323.JPG
│  │     ├─ IMG_1404.JPG
│  │     ├─ IMG_1434.JPG
│  │     ├─ IMG_1649.GIF
│  │     ├─ IMG_2202.PNG
│  │     ├─ IMG_2204.PNG
│  │     ├─ IMG_7251.JPG
│  │     ├─ IMG_8252.PNG
│  │     ├─ IMG_E2175.JPG
│  │     ├─ istockphoto-1295441478-612x612.jpg
│  │     ├─ istockphoto-1330787372-612x612.jpg
│  │     ├─ lab_tube.jpg
│  │     ├─ logan-weaver-lgnwvr-qdOedgUJq94-unsplash.jpg
│  │     ├─ marten-bjork-aTt_rNa3gmM-unsplash.jpg
│  │     ├─ maxresdefault.jpg
│  │     ├─ maxresdefault_Ia9o1Ru.jpg
│  │     ├─ maxresdefault_vnelw43.jpg
│  │     ├─ Mpetha_Linkedin.jpeg
│  │     ├─ OILZ2600.JPG
│  │     ├─ pexels-katja-79053-592077.jpg
│  │     ├─ pexels-katja-79053-592077_TtKITvc.jpg
│  │     ├─ pexels-tkirkgoz-15278251.jpg
│  │     ├─ pexels-tkirkgoz-18804037.jpg
│  │     ├─ pexels-wyxina-tresse-311038210-19724457.jpg
│  │     ├─ SampleJPGImage_10mbmb.jpg
│  │     ├─ Screenshot_2020-08-01_at_16.18.00.png
│  │     ├─ Screenshot_2020-11-18_at_18.01.10.png
│  │     ├─ Screenshot_2020-11-18_at_18_a7Km39B.01.10.png
│  │     ├─ Screenshot_2024-03-21_205952.png
│  │     ├─ Screenshot_2024-05-01_203626.png
│  │     ├─ Screenshot_2024-11-28_174708.png
│  │     ├─ Screenshot_2024-11-28_174708_jCduHul.png
│  │     ├─ Screenshot_2024-11-28_174708_nCzLraK.png
│  │     ├─ Screenshot_2024-11-28_174708_QqxcK97.png
│  │     ├─ Screenshot_2024-11-28_174708_YzVWniZ.png
│  │     ├─ What-Does-Instagram-User-Mean_compressed.png
│  │     ├─ yellow-rose-4251915_640.jpg
│  │     └─ yellow-rose-4251915_640_PTkSFMT.jpg
│  ├─ pixels
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-312.pyc
│  │  │     └─ __init__.cpython-312.pyc
│  │  ├─ models.py
│  │  ├─ static
│  │  │  ├─ init
│  │  │  └─ pixels
│  │  │     ├─ css
│  │  │     │  └─ styles.css
│  │  │     ├─ images
│  │  │     │  ├─ app_test_images
│  │  │     │  │  ├─ barnaby-K78ECC0F1YI-unsplash.jpg
│  │  │     │  │  ├─ chopped-green-salad-with-herby-chilli-dressing-0bc8e57.jpg
│  │  │     │  │  ├─ dusty-rose.jpg
│  │  │     │  │  ├─ emanuel-haas-P0ck7wsVAag-unsplash.jpg
│  │  │     │  │  ├─ gluten-free-diet-teaser.jpg
│  │  │     │  │  ├─ gratisography-augmented-reality-800x525.jpg
│  │  │     │  │  ├─ gratisography-cool-cat-800x525.jpg
│  │  │     │  │  ├─ hq720.jpg
│  │  │     │  │  ├─ istockphoto-1295441478-612x612.jpg
│  │  │     │  │  ├─ istockphoto-1330787372-612x612.jpg
│  │  │     │  │  ├─ logan-weaver-lgnwvr-qdOedgUJq94-unsplash.jpg
│  │  │     │  │  ├─ marten-bjork-aTt_rNa3gmM-unsplash.jpg
│  │  │     │  │  ├─ pexels-tkirkgoz-15278251.jpg
│  │  │     │  │  ├─ pexels-tkirkgoz-18804037.jpg
│  │  │     │  │  ├─ pexels-wyxina-tresse-311038210-19724457.jpg
│  │  │     │  │  └─ yellow-rose-4251915_640.jpg
│  │  │     │  ├─ favicon_io
│  │  │     │  │  ├─ android-chrome-192x192.png
│  │  │     │  │  ├─ android-chrome-512x512.png
│  │  │     │  │  ├─ apple-touch-icon.png
│  │  │     │  │  ├─ favicon-16x16.png
│  │  │     │  │  ├─ favicon-32x32.png
│  │  │     │  │  ├─ favicon.ico
│  │  │     │  │  └─ site.webmanifest
│  │  │     │  └─ logo.png
│  │  │     ├─ init
│  │  │     └─ js
│  │  │        └─ script.js
│  │  ├─ templates
│  │  │  ├─ base.html
│  │  │  ├─ init
│  │  │  └─ pixels
│  │  │     ├─ confirm_delete.html
│  │  │     ├─ image_details.html
│  │  │     ├─ image_list.html
│  │  │     ├─ init
│  │  │     ├─ upload_image.html
│  │  │     └─ upload_success.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ utils.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-312.pyc
│  │     ├─ apps.cpython-312.pyc
│  │     ├─ forms.cpython-312.pyc
│  │     ├─ models.cpython-312.pyc
│  │     ├─ tests.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ utils.cpython-312.pyc
│  │     ├─ views.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ PixelsProject
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ settings.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ wsgi.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  └─ requirements.txt
├─ README.md
├─ requirements.txt
├─ todo.txt
├─ ~$xel Project (Techical Documentation) v1.0.docx
├─ ~WRL0005.tmp
├─ ~WRL2244.tmp
└─ ~WRL3588.tmp

```
