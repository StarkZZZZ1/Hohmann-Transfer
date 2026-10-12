# **TO THE MOON**
### [Video demo]()
## Overview
This is my final project for Harvard's **CS50P** course based on the Hohmann Transfer Orbit.
It is a program that runs in the CLI which takes in several inputs to calculate an ideal launch window with a resolution of one hour, i.e. can calculate up to the best hour to launch on the best day in the next 30 days from the user's inputted date. Also takes in several other parameters related to the start/end orbit height and the rocket itself.
Output also includes the required delta-v (change in velocity) & fuel required for the entire maneuver.

Inspired by the recent launch of [Artemis-II](https://en.wikipedia.org/wiki/Artemis_II) 🌙🚀 and the mobile game [Spaceflight Simulator](https://play.google.com/store/apps/details?id=com.StefMorojna.SpaceflightSimulator&hl=en_SG). All the mathematical formulas required were obtained through Google Gemini

NOTE: Several real-world factors such as atmospheric effects, solar radiation pressure and more which have been ignored for simplicity and my sanity :)

## Sections
[Hohmann Transfer Orbit](#hohmann-transfer-orbit)

[Installation](#installation)

[Usage example](#usage-example)

[Features](#features)

## Hohmann Transfer Orbit
It is almost the most efficient way to transfer your orbit from one body to another. It finds the ellipse that is tangential to your initial and final orbits. The first prograde burn is used to navigate towards the target body and a second retrograde burn is used to capture an orbit around the new body.

See more on [Hohmann Transfer](https://en.wikipedia.org/wiki/Hohmann_transfer_orbit)

## Installation
To get this project up and running on your machine, follow these steps:

#### Prerequisites
Make sure you have Python 3.10+ installed. You can check your version by typing
`python --version` or `python3 --version` in your terminal.

Make sure `git` is installed.

#### Clone the repository
Type the command below in your terminal
```
git clone https://github.com/code50/175413721.git
cd 175413721/project
```
#### Install packages
Run
`pip install -r requirements.txt`

## Usage Example
Make sure you navigate to the project folder first.
Then run,
`python project.py`

1. Enter valid inputs when being prompted then click enter after each.
2. You should see the ideal launch window time and date (in next 30 days) and several other results such as the fuel required.

**That's it**

See you on the far side!

## Features

### Universal constants

Multiple constants have been defined beforehand in `const.py`. Initialization of skyfield package is also done within to get the ephemeris data (de421.bsp). See documentation of skyfield [here](https://rhodesmill.org/skyfield/positions.html#quick-reference)

### Custom Math & Physics engine

Vector operations and every single physics equation used in the calculations have been primarily from scratch mainly to reduce the learning curve of numpy and reproducibility by hand. The `math` package has been used throughout usually just to find square roots.

### test_project File

A pytest file which can be run by typing `pytest test_project.py` in the CLI was created to ensure the correctness of different functions used in this program
