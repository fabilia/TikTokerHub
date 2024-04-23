# TikTokerHub
TikTokerHub is a prototype program designed to simulate a TikTok influencer database.

## General Info
This program is written as a part of a series of tests conducted by Purwadhika's DTI DS program.

This program is Module 1's Capstone Project.

The database consists of username, name, industry, location, following count, average views, rate (per video), and e-mail. Currently, the data is filled with dummy data. All data used in this program are fictional, any similarities from the real world data are not intentional.

A pdf explaining the flowchart of this program is also attached in this git. Feedbacks are highly appreciated.

## Features
This program will allow its users to access the current database, filter the database, add new influencer(s) into it, remove influencer(s), edit the existing data, and compare Cost per View (CPV) between influencers.

### Main Menu
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/00b3dd67-03a5-4e13-a8a0-bd4c84a957eb)

This is the main menu that will greet the user. They are welcomed with a message and they are free to enter an input from the choice given. The detail of each option are as follow:

#### 1. Show Database
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/5bde3770-71af-4dd7-b18b-a7e70da76036)

This option shows all the data available in the database.

#### 2. Filter Database
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/b38fb536-1324-49e4-8c36-4d21f0553edf)

This option will filter the entire database according to the input retreived.

#### 3. Add New Influencer
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/00ab1036-a0fb-455f-be88-d39d092e3b17)

This option will add a new influencer based on the data entered by the user.

#### 4. Remove an Influencer
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/c9890086-f9ed-4c9a-a5f4-36478d677b32)

This option will remove an influencer in the database by choosing the influencer's index number.

#### 5. Edit Influencer Data
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/e0b6faba-257b-4ef2-baeb-3027e2531b05)

This option will edit the existing data according to user input.

#### 6. Compare CPV
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/404f7b8b-a71b-409d-8d2f-e859d06f0bac)

This option will compare CPV between influencers according to user input. User can also get more info about the influencer with the highest & lowest CPV amongst the chosen influencers. Aside from that, the user can also get the mean of the chosen influencers.

#### 7. Exit Program
![image](https://github.com/fabilia/TikTokerHub/assets/67428045/5ad36f63-e2f7-441c-99d7-92c459f9ac74)

This option will exit the program.


## Dependencies and Environment Requirements
1. Requires Python 3.x
2. [tabulate](https://pypi.org/project/tabulate/)

## Guide to Run
1. Clone the repository:
`git clone https://github.com/fabilia/TikTokerHub.git`
2. Install dependencies:
`pip install tabulate`
3. Run the application:
`InfluencerHub_final.py`

## Usage
Upon running the program, a menu will show up. Follow the instructions given to get the information needed.

S. Fabilia (2024)
