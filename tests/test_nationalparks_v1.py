# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 18:24:06 2021
@author: Bengusu Ozcan
"""

import pytest
from nationalparks_v1 import nationalparks_v1
import requests
import pandas as pd
#WARNING: In order to run the tests that require an API key, please replate API_KEY in below functions with your acquired US National Parks API key and then save the file.

def test_api_integration():
    response = requests.get("https://developer.nps.gov/api/v1/alerts?parkCode=yose&api_key=API_KEY")
    assert response.status_code == 200
    
def test_name_check():
    actual=nationalparks_v1.name_check("anything")
    assert actual=="anything"

def test_dist_calc():
    actual=nationalparks_v1.dist_calc(40.822627,-73.944870,1)
    assert actual is not None

def test_how_far():
    actual=nationalparks_v1.how_far("grand canyon",40.80509121096195,-73.96388694375622)
    assert actual == str("The distance between your loaction and Grand Canyon National Park is approximately 3348.5968802943935 km")

def test_park_desc():
    actual = nationalparks_v1.park_desc("grand canyon","API_KEY")
    assert actual == "Located in Arizona, Grand Canyon National Park encompasses 277 miles (446 km) of the Colorado River and adjacent uplands. The immense Grand Canyon is a mile (1.6 km) deep, and up to 18 miles (29 km) wide. Layered bands of colorful rock reveal millions of years of geologic history with unmatched vistas from the rim. The South Rim is open 24 hours. The North Rim is Closed for the Winter."

def test_activity_search():
    actual=nationalparks_v1.activity_search("skiing","API_KEY")
    assert actual is not None

def test_park_popularity():
    actual=nationalparks_v1.park_popularity("most",1)
    d = {'Name of the Park': ["Great Smoky Mountains"], 'Number of Visitors': [12095720]}
    assert actual is not None
    
def test_alerts():
    with pytest.raises(AssertionError):
        nationalparks_v1.alerts("laylay","API_KEY")

def test_pet_friendly():
    actual=nationalparks_v1.pet_friendly("Adams National Historical Park","API_KEY")
    assert actual == str("There are no pet restrictions in this park. You are good to go!")
    
def test_pet_restrictions():
    actual=nationalparks_v1.pet_restrictions("acadia","API_KEY")
    assert actual is not None