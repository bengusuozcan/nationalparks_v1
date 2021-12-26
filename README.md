**Disclaimer for the grader:**

-This part is just to add disclaimers for the sake of this project and not added in the published version of the packge.

-As confirmed with on of our TAs that it satisfies the requirements, I only used the ReadMe for the explanation of my package rather than a separate vignette file.

-My tests run successfully as in the below screenshot but I updated the test functions hiding my API key in the submitted version, so they would not run as they are now.

<img width="461" alt="my tests works" src="https://user-images.githubusercontent.com/27307541/146476306-5074d983-edc4-4769-bd36-6679ee9aec92.PNG">

Author: Bengusu Ozcan (bo2297)
Type of Project: A

# Package name: nationalparks_v1

National parks are areas that are under the protection of states or organizations with their exceptional nature or historical significance. The United States has many national parks, conserved carefully and almost always open to visitors. 

This package helps you to explore national parks and plan your next national park trip, such as looking for which parks to go for certain activities, how far a park from your location or the latest alerts in that park.

Some functions and testing will depend on US National Parks API key. You may obtain one for free via https://www.nps.gov/subjects/developer/get-started.htm

## Testing

In order to test the functions in this package, you need to pass your API key into certain functions. Please follow the below steps after installing the package
1) Go to test folder
2) Open test_nationalparks.py
3) Replace all API_KEY keywords with your obtained API key
4) Save the file
After these steps, you can run the tests by using pypi.

## Data

This package depends on 2 data files that are complied through US National Parks API. The files are saved under src / data folder. These files are not expected to be updated, but if so, you may expect an update to the package or recomplie the files yourself through US National Parks API. These two files are:
1) parks_list: CSV file that only 2 columns are needed for the package: fullName and parkCode which stands for the name of the park and the API code of the park.
2) activities: CSV file that only 2 columns are needed for the package: 

## Installation

This package is currently released only on testpy.pi. Please use following command to install:
!pip install -i https://test.pypi.org/pypi/ --extra-index-url https://pypi.org/simple nationalparks_v1

Dependencies: This package leverages poetry to install the dependencies which are as follows:

pytest = "^6.2.5"

requests = "^2.26.0"

pandas = "^1.3.5"

regex = "^2021.11.10"

geopy = "^2.2.0"

setuptools = "^59.6.0"

lxml = "^4.7.1"

Jinja2 = "^3.0.3"

## Usage

**HELPER FUNCTIONS**

**national_parks():** This function does not take any input. It works as an introductory function that introduces what the package does and which functions it has.

**name_check()**: This function does not take any input or interact with user. It is being called as a helper function by other functions. It replaces or corrects users' park name query with with the required version on US National Parks if the query matches with a unique keyword for the most popular national parks. It leverages regex and if-else statements.

**parks_list():** This function does not take any input or interact with user. It is being called as a helper function by other functions. It matches the park name the user queried for the park code required for the API search. Uses the 'parks_list.csv' file available in the data folder in the package.

**activity_list():** This function does not take any input but it interacts with the user. It returns the full list of all activities that are available to do in national parks for user to choose from. Users will be prompted to use this function whenever they enter an acitivty name name that doesn't match with US National Parks API database records.

Example:

input: activity_list()

output: Here are the activities you can search for: Arts and Culture, Astronomy, Auto and ATV, Biking, Boating, Camping, Canyoneering, Caving, Climbing, Compass and GPS, Dog Sledding, Fishing, Flying, Food, Golfing, Guided Tours, Hands-On, Hiking, Horse Trekking, Hunting and Gathering, Ice Skating, Junior Ranger Program, Living History, Museum Exhibits, Paddling, Park Film, Playground, SCUBA Diving, Shopping, Skiing, Snorkeling, Snow Play, Snowmobiling, Snowshoeing, Surfing, Swimming, Team Sports, Tubing, Water Skiing, Wildlife Watching

**parks_names():** This function does not take any input but it interacts with the user. It returns a list of national parks for the user to search for the exact name of the national park they want to query for. Users will be prompted to use this function whenever they enter a national park name that doesn't match with US National Parks API database records.

Example:

input: parks_names()

output:

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146472814-bd714a26-972e-4f92-82ac-b5d20402296e.png" align="center" height="150" width="450" ></a>

**MAIN FUNCTIONS**

**dist_calc(lat,long,n):** Returns the closest n national parks based on given latitude and longitude. Does not require an API key but requires user to provide the latitude and longitude of an exact location. It leverages geopy package 

Example: Top 3 closest national parks to a random location in California.

input: dist_calc(37.329754, -120.020413,3)

ouptut:

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146472865-0fbb8af2-6c9d-4d8f-abe6-f0da74947825.png" align="center" height="150" width="450" ></a>

**how_far(park_name, lat, long):** Calculates the approximate euclidian distance (e.g. as a straight line between the two locations on the map) of a national park in Km based on user's latitude and longitude. Raises an error if the queried park name does not match the US National Park services' database and prompts user to check the correct park names as a list.

Example: In below example, "canyon" is not a sufficient keyword to serach for the park name, hence the user is asked for calling the park_names() to choose the exact park name for the query.

input: how_far("canyon",40.805040,-73.964873)

output:

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146472974-0c92dc64-b7d4-4a98-8256-e056c1350baa.png" align="center" height="150" width="450" ></a>

**park_desc(park_name,token):** Returns the blurb description of a national park user search for, provided by the US National Parks Services to give a snapshot of what that park is like to the user. Takes two input: park_name as the park to query for token as the valid US National Parks API key. Raises an error if the queried park name does not match the US National Park services' database and prompts user to check the correct park names as a list.

Example: In below example, name_check() helper function matches "yosemite" keyword with Yosemite National Park on US National Parks API database and returns the output.

input: park_desc("yosemite","API_KEY")

output: 'Not just a great valley, but a shrine to human foresight, the strength of granite, the power of glaciers, the persistence of life, and the tranquility of the High Sierra. First protected in 1864, Yosemite National Park is best known for its waterfalls, but within its nearly 1,200 square miles, you can find deep valleys, grand meadows, ancient giant sequoias, a vast wilderness area, and much more.'

**activity_search(activitiy, token)**: Returns a dataframe that lists all the national parks that are suitable for the activity the user searched for. Takes two input: activity_name as the park to query for token as the valid US National Parks API key. Raises an error if the activity does not match the US National Park services' database and prompts user to check the correct activity names as a list.

Example:

input: activity_search("snorkeling","API_KEY")

output:

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146473037-e76b7595-3309-418d-afc8-0ddbbeb6fc5a.png" align="center" height="150" width="450" ></a>

**park_popularity(sorting, n):** Scrapes the most up to date number of visitors information for national parks from Wikipedia and returns the n number of most and least visited national parks. Takes two input: sorting as the order of sorting and n as the number of parks to return. Raises an error if the sorting keyword does not match.

Example:

input: park_popularity("most",5)

output: 

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146474225-21854418-d7b7-4e06-80e5-36f0cdbb29b4.png" align="center" height="150" width="350" ></a>

**alerts(park_name, token)**: Returns the active alerts existing for a park on US National Park Services along with their description and the latest announcement date. Takes two input: activity_name as the park to query for token as the valid US National Parks API key. Raises an error if the park name does not match the US National Park services' database and prompts user to check the correct park names as a list.

Example:

input: alerts("grand canyon","API_KEY")

output: 

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146474271-cd190cad-06e1-41fc-b597-9237b9c49ad4.png" align="center" height="150" width="450" ></a>

**pet_friendly(park_name, token):** Informs you whether this national park is completely free of pet restrictions or guides you to another function to learn about the restrictions. Takes two input: activity_name as the park to query for token as the valid US National Parks API key. Raises an error if the park name does not match the US National Park services' database and prompts user to check the correct park names as a list.

Example: In Smoky Mountains National Park, there are no pet restrictions.

input: pet_friendly("smoky","API_KEY")

output:'There are no pet restrictions in this park. You are good to go!'

Example: In Yosemite National Park, there are pet restrictions.

input: pet_friendly("yosemite","API_KEY")

output: 'Pets are permitted in this park with certain restrictions. Please call pet_restrictions function to see what they are.'

**pet_restrictions(park_name, token)**: Provides a list of pet restrictions and locations that the restrictions apply for a specific national park. Takes two input: activity_name as the park to query for token as the valid US National Parks API key. Raises an error if the park name does not match the US National Park services' database and prompts user to check the correct park names as a list.

Example:

input: pet_restrictions("acadia","API_KEY")

output:

<a href="url"><img src="https://user-images.githubusercontent.com/27307541/146474430-f53e93dd-ad10-4e91-b53a-61bb19ffb780.png" align="center" height="150" width="450" ></a>

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`nationalparks_v1` was created by Bengusu Ozcan. It is licensed under the terms of the MIT license.

## Credits

`nationalparks_v1` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
