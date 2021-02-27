#!/usr/bin/env python
# coding: utf-8

# In[7]:


import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# In[2]:


engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

Base.prepare(engine, reflect = True)


# In[4]:


Measurement = Base.classes.measurement
Station = Base.classes.station


# In[8]:


session = Session(engine)


# In[ ]:


app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API >br/>"
        f"Available Routes <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8 ,23) - dt.timedelta(days = 365)
    precipitation = session.query(Measurement.date, Measurement.prcp).        filter(Measurement.date >= prev.year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    


# In[ ]:





# In[ ]:





# In[ ]:




