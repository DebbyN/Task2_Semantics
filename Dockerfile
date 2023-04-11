#Dockerfile
#L3T12_Task2 Symantic Similarities

#Load different python interpreter
FROM pypy:latest

#Working directory for image 
WORKDIR /app

#Copies the requirements.txt from the computer where created to the image
COPY requirements.txt requirements.txt

# Installs the requirements specified in the requirements file
RUN pip3 install -r requirements.txt

#Copy all files from local directory
COPY . /app

#Run the code
#Using the advanced language mode to choose a movie
CMD python watch_next.py


