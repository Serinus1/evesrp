#!/usr/bin/env python
from evesrp import app, db
import config
from evesrp import models
from evesrp.auth import models, testauth, bravecore

app.config.from_object(config.Development)
db.create_all()
