# Task2_Semantics
Task to use the advance language module to select a movie similar to a favourite movie.
## Table of Contents:
1. Installation
2. The Purpose of the Application.
3. Expected Results.

## Installation
- Pull down all files and build the image from the cmd line with : 'docker build -t task2_semantics ./'
- From the cmd line run the app: 'docker run task2_semantics'
- Or pull the image from the docker hub: 'debbyn104/task2_symantics' and then run it.
- Please ensure that the movies.txt file is in the same folder as the python code.

## The Purpose of the Application.
- Second task of an assignment.
- The purpose of the app is to select the next movie from a list of descriptions for movies, compared against 
  a favourite movie's description, using the spacy advanced language module.

## Expected Results.
- The favourite movie's name and description will be displayed, followed by a list of all the movies in the text file,
  and ending with the name of the movie suggested to watch next.
