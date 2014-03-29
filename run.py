#!/usr/bin/env python
from evesrp import app
from evesrp.killmail import CRESTMail, ZKillmail, SQLShipNameMixin,\
        EveMDShipNameMixin
import sqlite3

import config

SQLShipNameMixin.driver = sqlite3
SQLShipNameMixin.connect_args = 'rubicon.sqlite'

class SQLZKillmail(ZKillmail, SQLShipNameMixin): pass

class EMDZKillmail(ZKillmail, EveMDShipNameMixin):
    def __init__(self, **kwargs):
        super(EMDZKillmail, self).__init__(user_agent='Paxswill', **kwargs)

app.config.from_object(config.Development)
app.config['USER_AGENT_EMAIL'] = 'paxswill@paxswill.com'
app.config['KILLMAIL_SOURCES'] = [CRESTMail, EMDZKillmail]

if __name__ == '__main__':
    app.run()
