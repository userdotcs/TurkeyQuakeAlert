import pandas as pd
import json
import errors

class KandilliGetter:
    def __init__(self):
        self.url = "http://sc3.koeri.boun.edu.tr/eqevents/events.html"
        self.quake_list = []
        self.refresh()
    
    def refresh(self):
        table = pd.read_html(self.url)[0].to_dict()
        self.quake_list.clear()
        for index in range(len(table['Mag'])):
            date = table['Zaman-Origin Time UTC'][index].split(" ")[0]
            time = table['Zaman-Origin Time UTC'][index].split(" ")[1]
            quake = {
                'Date': date,
                'Time': time,
                'Magnitude': table['Mag'][index],
                'Location': table['Yer-Region Name'][index],
                'Depth': table['Der-Depth (km)'][index]
            }
            self.quake_list.append(quake)
    
    def save_lastquake_to_json(self, path="quake.json"):
        with open(path, "w") as file:
            json.dump(self.quake_list[0], file, indent=3)

    def save_quake_to_json_at(self, index: int, path="quake.json"):
        if(index > len(self.quake_list) - 1 or index < 0):
            raise errors.IndexOutOfList(index, len(self.quake_list))
        else:
            with open(path, "w") as file:
                json.dump(self.quake_list[index], file, indent=3)