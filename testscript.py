import sqlalchemy
import psycopg2
import pandas as pd, numpy as np
import reverse_geocoder as rgc

def home_location_city(arr):
    nli = []
    for i in arr:
        #li = rgc.search((i['lat'], i['lng']))
        li = [{'lat': '18.54225','lon': '73.13493','name': 'Nagothana','admin1': 'Maharashtra','admin2': 'Raigarh','cc': 'IN'}]
        dist_name = li[0]['admin2']
        city = li[0]['name']

        conn = psycopg2.connect(host="dc.kom", port=5432, database="db", user="",
                                password="")
        cur = conn.cursor()
        city_id = cur.execute("select id from apptraffic_city where name='{}'".format(dist_name))
        print(city_id)
        query = "select city, admin2, hour, cluster_grp, home_work, cent_lat, cent_long from apptraffic_all_cities2 where admin2='{}'".format(
            dist_name)
        clus_df = pd.read_sql_query(query, engine)

        dd_home = clus_df[clus_df['home_work'] == 'home location']
        dd_city = dd_home[dd_home['city'] == city]
        lat = []
        lon = []
        count = []
        interval = []
        density = []
        for i in sorted(dd_city.cluster_grp.unique()):
            x = dd_city[dd_city['cluster_grp'] == i]

            lat.append(x.cent_lat.iloc[0])
            lon.append(x.cent_long.iloc[0])
            count.append(len(x))
            interval.append(x.hour.iloc[0])
            density.append(len(x) / len(dd_city))
        xdf = pd.DataFrame({'lat': lat, 'lng': lon, 'density': density, 'count': count, 'interval': interval})
        result = xdf.to_dict(orient="records")

        nli.append({'name': ", ".join([city, dist_name]), 'locations': result})
        print(nli)
    return nli
