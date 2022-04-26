# Capstone Project Mathematical Maestros

## Table of Contents

- [Capstone Project Mathematical Maestros](#capstone-project-mathematical-maestros)
  * [Project Description](#project-description)
  * [Demo](#demo)
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Recommended Instructions](#recommended-instructions)
  * [Methodology](#methodology)
  * [Reflection](#reflection)
  * [Future Work](#future-work)
  * [Using the API's endpoints](#using-the-api-s-endpoints)
  * [References](#references)

## Project Description

The Mathematical Maestros’ Team presents a Machine Learning-driven web application for showcasing and evaluating computer generated music. Our Maestro can compose an original, single-instrument song in less than a minute. A fully featured user system allows our users to rate songs, providing an essential evaluation metric for our team to continue to enhance the Maestro’s capabilities.

## Demo

<p align="center">
    <img src="Docs/screenshots/mock.gif">
</p>

## Getting Started

This project is tested on an Ubuntu system, results with other Linux distributions may vary. This project is optimized for use with NVIDIA cuDNN. To read more about cuDNN visit [here](https://developer.nvidia.com/cudnn).

### Prerequisites

- Python 3.8
- npm
- FluidSynth
- Redis

### Recommended Install
```
# Navigate to flask-server
$ cd flask-server

# Create Virtual Environment
$ python -m venv venv

# Activate Virtual Environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create DB
$ python
>> from models import db
>> db.create_all()
>> exit()

# Run Server (http://127.0.0.1:5000)
python app.py

# Navigate to react-front-end
$ cd ../react-front-end/

# Install more dependencies
$ npm install 

# Run Frontend (http://127.0.0.1:3000)
$ npm start
```

## Methodology

Through Python we developed a RESTful API via the Flask microframework to power our backend. Flask allowed us to interface with an SQLite database for storing and retrieving user, song, and song rating records. Additionally, Flask facilitated communication with TensorFlow - Keras, our library of choice for building neural network models. M.I.T.’s Music21 toolkit proved essential for parsing MIDI song files. JavaScript’s React framework allowed us to develop an aesthetic UI for our frontend. All communications between front and backend are passed through JSON. This separation of front and backend systems accelerated our development process as both systems could be developed and tested independently. 

## Reflection 

Our neural network models produce convincing, single-instrument songs of various genres.  Some tracks have been afflicted by an occasional odd note and abrupt ending. Consequently, we are pleased with our results but acknowledge room for improvement. We partially attribute the success of our neural network models to the adl-piano-midi dataset. This dataset allows us to source MIDI song files across a variety of genres that have been crucial in training our neural network models. 

## Future Work

The Mathematical Maestros project has provided a solid foundation for future work to expand on. Our rating system’s implementation enables us to passively collect key data as users utilize our web application. This data can then be refined to provide an evaluation metric for our neural network models. Due to the nature of generative systems mirroring human creativity, we believe this subjective approach to evaluation is critical for the fine-tuning of these neural network models. In addition to the single-instrument songs currently produced, future work could focus on introducing more complex, multi-instrument songs. 

## Using the API's endpoints

- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/users/session**
    - Identify the current user 
- POST&nbsp;&nbsp;&nbsp;&nbsp;**/api/users**
    - Register user  
- POST&nbsp;&nbsp;&nbsp;&nbsp;**/api/users/session**
    - Sign in user 
- DELETE&nbsp;&nbsp;&nbsp;&nbsp;**/api/users/session**
    - Logout user
- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/play/:id**
    - Play song with id equal to :id  
- POST&nbsp;&nbsp;&nbsp;&nbsp;**/api/song**
    - Creates a new song of specified genre
- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/song**
    - Returns all songs in database
- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/:id**
    - Returns song at specified id
- PUT&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/:id**
    - Updates song at specified id
- DELETE&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/:id**
    - Removes song from database at specified id
- POST&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/rating**
    - Calculates a new average rating for song 
- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/rating**
    - Returns all ratings in database  
- GET&nbsp;&nbsp;&nbsp;&nbsp;**/api/song/rating/:id**
    - Returns the average rating of song with id equal to :id

## References 

Ferreira, L. N., Lelis, L. H. S., & Whitehead, J. (2020) Computer-Generated Music for Tabletop Role-	Playing Games. doi:10.48550/ARXIV.2008.07009

Skúli, S. (2017, December 9). How to generate music using a LSTM neural network in Keras. Medium. Retrieved April 12, 2022, from https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5 
