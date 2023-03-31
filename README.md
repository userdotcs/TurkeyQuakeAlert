Retrieves data from Kandilli Observatory And Earthquake Research Institute. It has a simple structure. You can use it by throwing it into the project folder.

## Commands
Use "KandilliGetter" to access earthquake information:
```
from TurkeyQuakeAlert import KandilliGetter

getter = KandilliGetter()
```

Use "refresh" to refresh quake list:
```
from TurkeyQuakeAlert import KandilliGetter
import time

getter = KandilliGetter()

while True:
    
    # Commands

    getter.refresh()
    time.sleep(1)
```

Use "save_lastquake_to_json" to save lastquake infos as .json file:
```
from TurkeyQuakeAlert import KandilliGetter

getter = KandilliGetter()

getter.save_lastquake_to_json()
```

Use "save_quake_to_json_at" to save a specific index:
```
from TurkeyQuakeAlert import KandilliGetter

getter = KandilliGetter()

getter.save_quake_to_json_at(6)
```

Earthquake file should be like this:
```
{
   "Date": "2023/03/15",
   "Time": "06:27:07",
   "Magnitude": 4.3,
   "Location": "Cyprus Region",
   "Depth": 5
}
```