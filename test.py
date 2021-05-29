#!/usr/bin/env python
import datetime
from hud import Hud


hud = Hud('Teste de HUD')

while True:
    
    hud.print([
        ('data', datetime.datetime.now())
    ])

    hud.sleep()
