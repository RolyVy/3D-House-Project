# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:58:26 2021

@author: Vincent Rolin
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show
from rasterio.plot import show_hist
from shapely.geometry import Polygon, mapping
from rasterio.mask import mask
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import geopandas as gpd

from matplotlib.colors import ListedColormap
import matplotlib.colors as colors

import requests
import json

import plotly.graph_objects as go


print('What is your address? Please enter the folowing informations and get your 3D house model :')


city_postcode=input('Postcode : ')
streetname=input('Streetname (in dutch please) : ')
house_number= input('The house number :')

#using the address input data, to get the coordinates and the polygon of the house

r = requests.get("https://api.basisregisters.vlaanderen.be/v1/adresmatch", params={"postcode":city_postcode, "straatnaam":streetname, "huisnummer":house_number})
json_test = json.loads(r.content)
json_test


objectId = json_test['adresMatches'][0]['adresseerbareObjecten'][0]['objectId']

house_coordinates = json_test['adresMatches'][0]['adresPositie']['point']['coordinates']
x_house_coordinates = house_coordinates[0]
y_house_coordinates = house_coordinates[1]


r = requests.get(f"https://api.basisregisters.vlaanderen.be/v1/gebouweenheden/{objectId}")
json_test_gebouwheden = json.loads(r.content)
json_test_gebouwheden

object_Id_gebouw = json_test_gebouwheden['gebouw']['objectId']

r = requests.get(f"https://api.basisregisters.vlaanderen.be/v1/gebouwen/{object_Id_gebouw }")
json_test_gebouw = json.loads(r.content)
json_test_gebouw

#Getting the polygon shapes as a type Dict
shapes = json_test_gebouw['geometriePolygoon'].get('polygon')

print(shapes)


