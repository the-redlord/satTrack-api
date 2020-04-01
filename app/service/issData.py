from skyfield.api import Topos, load

ts = load.timescale()


def getData():
    satellites = load.tle_file('https://www.celestrak.com/NORAD/elements/stations.txt')
    sat = satellites[0]
    print('Loaded', sat)
    t = ts.now()
    geocentric = sat.at(t)
    subpoint = geocentric.subpoint()
    return ({'name':str(sat.name),'number':str(sat.model.satnum),'Latitude': str(subpoint.latitude),
        'Longitude': str(subpoint.longitude),
        'Elevation-m': str(round(subpoint.elevation.m)),
        'Inclination-rad':str(sat.model.inclo)
    })
    # print('Latitude:', subpoint.latitude)
    # print('Longitude:', subpoint.longitude)
    # print('Elevation (m):', int(subpoint.elevation.m))