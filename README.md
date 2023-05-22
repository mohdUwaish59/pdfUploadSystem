# pdfUploadSystem
This system is developed as a part of the project work to develop a Plagiarism Detection System and this will be integrated into TEIMMA app later.

# About this system
The sysem has a home page with two buttons named 'Annotator' and 'Plagiarism'. While 'plagiarism' button works and lands us on the source document and candidate document upload page, working of 'annotator' button is yet to be implemneted.

On Upload page, user can separately upload source document and candidate documents which are stored separately.   
The 'start analysing' button will take us to result.html page (after user selects an algorithm for text analysing) where result of text similarity between source and candidate documents will be presented.   

# Steps to run this project
To Run this Project, just Clone it in your system and run   
python manage.py makemigrations   
python manage.py migrate   
python manage.py runserver   
