import math


class LatitudeAndLongitude:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        '''
        80000: 1次メッシュ（約80km）
        10000: 2次メッシュ（約10km）
        5000: 5倍メッシュ（約5km）
        2000: 2倍メッシュ（約2km）
        1000: 3次メッシュ（約1km）
        500: 4次メッシュ（約500m）
        250: 5次メッシュ（約250m)
        200: 拡張200mメッシュ（約200m）
        125: 6次メッシュ（約125m）
        100: 拡張100mメッシュ（約100m)
        50: 拡張50mメッシュ（約50m）
        20: 拡張20mメッシュ（約20m）
        10: 拡張10mメッシュ（約10m）
        50: 拡張5mメッシュ（約5m）
        2:　拡張2mメッシュ（約2m）
        1: 拡張1mメッシュ（約1m）
        '''
        # calculated number of each digit form latitude and longitude
        # 80000: 1次メッシュ（約80km）
        self.digit_1 = int(self.latitude * (3 / 2))
        self.digit_3 = int(self.longitude - 100)
        self.code_80000 = str(self.digit_1) + str(self.digit_3)

        # 10000: 2次メッシュ（約10km）
        self.digit_5 = int((self.latitude * (3 / 2) - self.digit_1) / (1 / 8))
        self.digit_6 = int((self.longitude - int(self.longitude)) / (1 / 8))
        self.code_10000 = self.code_80000 + str(self.digit_5) + str(self.digit_6)

        # 1000: 3次メッシュ（約1km）
        self.digit_7 = int((self.latitude * (3 / 2) - self.digit_1 \
                            - self.digit_5 * (1 / 8)) / (1 / 8 / 10))
        self.digit_8 = int((self.longitude - int(self.longitude) \
                            - self.digit_6 * (1 / 8)) / (1 / 8 / 10))
        self.code_1000 = self.code_10000 + str(self.digit_7) + str(self.digit_8)

        # 2000: 2倍メッシュ（約2km）
        self.digit_7_2times = int(self.digit_7/2) * 2
        self.digit_8_2times = int(self.digit_8/2) * 2
        self.code_2000 = self.code_10000 + str(self.digit_7_2times) + str(self.digit_8_2times) + "5"

        # 5000: 5倍メッシュ（約5km）
        if self.digit_7 < 5:
            if self.digit_8 < 5:
                self.digit_7_5000 = 0
            else:
                self.digit_7_5000 = 1
        else:
            if self.digit_8 < 5:
                self.digit_7_5000 = 2
            else:
                self.digit_7_5000 = 3

        self.code_5000 = self.code_10000 + str(self.digit_7_5000)

        #  100: 拡張100mメッシュ（約100m)
        self.digit_9 = int((self.latitude * (3 / 2) - self.digit_1 - self.digit_5 * (1 / 8) \
                            - self.digit_7 * (1 / 8 / 10)) / (1 / 8 / 10 / 10))
        self.digit_10 = int((self.longitude - int(self.longitude) - self.digit_6 * (1 / 8) \
                             - self.digit_8 * (1 / 8 / 10)) / (1 / 8 / 10 / 10))
        self.code_100 = self.code_1000 + str(self.digit_9) + str(self.digit_10)

        #  10: 拡張10mメッシュ（約10m）
        self.digit_11 = int((self.latitude * (3 / 2) - self.digit_1 - self.digit_5 * (1 / 8) \
                             - self.digit_7 * (1 / 8 / 10) \
                             - self.digit_9 * (1 / 8 / 10 / 10)) / (1 / 8 / 10 / 10 / 10))
        self.digit_12 = int((self.longitude - int(self.longitude) - self.digit_6 * (1 / 8) \
                             - self.digit_8 * (1 / 8 / 10) \
                             - self.digit_10 * (1 / 8 / 10 / 10)) / (1 / 8 / 10 / 10 / 10))
        self.code_10 = self.code_100 + str(self.digit_11) + str(self.digit_12)

        # 1: 拡張1mメッシュ（約1m）
        self.digit_13 = int((self.latitude * (3 / 2) - self.digit_1 - self.digit_5 * (1 / 8) \
                             - self.digit_7 * (1 / 8 / 10) - self.digit_9 * (1 / 8 / 10 / 10) \
                             - self.digit_11 * (1 / 8 / 10 / 10 / 10)) / (1 / 8 / 10 / 10 / 10 / 10))
        self.digit_14 = int((self.longitude - int(self.longitude) - self.digit_6 * (1 / 8) \
                             - self.digit_8 * (1 / 8 / 10) - self.digit_10 * (1 / 8 / 10 / 10) \
                             - self.digit_12 * (1 / 8 / 10 / 10 / 10)) / (1 / 8 / 10 / 10 / 10 / 10))
        self.code_1 = self.code_10 + str(self.digit_13) + str(self.digit_14)

        #  500: 4次メッシュ（約500m）
        self.latitude_S = self.digit_1 / (3 / 2) + self.digit_5 * (2 / 3 / 8) + self.digit_7 * (2 / 3 / 8 / 10)
        self.longitude_W = self.digit_3 + 100 + self.digit_6 * (1 / 8) + self.digit_8 * (1 / 8 / 10)

        if self.latitude < self.latitude_S + 2 / 3 / 8 / 10 / 2:
            if self.longitude < self.longitude_W + 1 / 8 / 10 / 2:
                self.digit_9div = 1
            else:
                self.digit_9div = 2
        else:
            if self.longitude < self.longitude_W + 1 / 8 / 10 / 2:
                self.digit_9div = 3
            else:
                self.digit_9div = 4
        self.code_500 = self.code_1000 + str(self.digit_9div)

        # 250: 5次メッシュ（約250m)
        self.latitude_S_500m = self.latitude_S + ((int(self.digit_9div) - 1) // 2) * 2 / 3 / 8 / 10 / 2
        self.longitude_W_500m = self.longitude_W + ((int(self.digit_9div) - 1) % 2) * 1 / 8 / 10 / 2

        if self.latitude < self.latitude_S_500m + 2 / 3 / 8 / 10 / 2 / 2:
            if self.longitude < self.longitude_W_500m + 1 / 8 / 10 / 2 / 2:
                self.digit_10div = 1
            else:
                self.digit_10div = 2
        else:
            if self.longitude < self.longitude_W_500m + 1 / 8 / 10 / 2 / 2:
                self.digit_10div = 3
            else:
                self.digit_10div = 4
        self.code_250 = self.code_500 + str(self.digit_10div)

        # 125: 6次メッシュ（約125m）
        self.latitude_S_250m = self.latitude_S_500m + ((int(self.digit_10div) - 1) // 2) * 2 / 3 / 8 / 10 / 2 / 2
        self.longitude_W_250m = self.longitude_W_500m + ((int(self.digit_10div) - 1) % 2) * 1 / 8 / 10 / 2 / 2

        if self.latitude < self.latitude_S_250m + 2 / 3 / 8 / 10 / 2 / 2 / 2:
            if self.longitude < self.longitude_W_250m + 1 / 8 / 10 / 2 / 2 / 2:
                self.digit_11div = 1
            else:
                self.digit_11div = 2
        else:
            if self.longitude < self.longitude_W_250m + 1 / 8 / 10 / 2 / 2 / 2:
                self.digit_11div = 3
            else:
                self.digit_11div = 4
        self.code_125 = self.code_250 + str(self.digit_11div)

        # 200: 拡張200mメッシュ（約200m）
        self.digit_9_2times = int(self.digit_9/2) * 2
        self.digit_10_2times = int(self.digit_10/2) * 2
        self.code_200 = self.code_1000 + str(self.digit_9_2times) + str(self.digit_10_2times) + "5"

        # 50: 拡張50mメッシュ（約50m）
        self.digit_11_5times = int(self.digit_11/5) + int(self.digit_12/5) * 2
        self.code_50 = self.code_100 + str(self.digit_11_5times)

        # 20: 拡張20mメッシュ（約20m）
        self.digit_11_2times = int(self.digit_11 / 2) * 2
        self.digit_12_2times = int(self.digit_12 / 2) * 2
        self.code_20 = self.code_100 + str(self.digit_11_2times) + str(self.digit_12_2times) + "5"

        # 5: 拡張5mメッシュ（約5m）
        self.digit_13_5times = int(self.digit_13/5) + int(self.digit_14/5) * 2
        self.code_5 = self.code_10 + str(self.digit_13_5times)

        # 2: 拡張2mメッシュ（約2m）
        self.digit_13_2times = int(self.digit_13 / 2) * 2
        self.digit_14_2times = int(self.digit_14 / 2) * 2
        self.code_2 = self.code_10 + str(self.digit_13_2times) + str(self.digit_14_2times) + "5"

    def get_wgs_code(self, mesh_size=80000):
        if mesh_size == 80000:
            code = self.code_80000
        elif mesh_size == 10000:
            code = self.code_10000
        elif mesh_size == 1000:
            code = self.code_1000
        elif mesh_size == 2000:
            code = self.code_2000
        elif mesh_size == 5000:
            code = self.code_5000
        elif mesh_size == 100:
            code = self.code_100
        elif mesh_size == 10:
            code = self.code_10
        elif mesh_size == 1:
            code = self.code_1
        elif mesh_size == 500:
            code = self.code_500
        elif mesh_size == 250:
            code = self.code_250
        elif mesh_size == 125:
            code = self.code_125
        elif mesh_size == 200:
            code = self.code_200
        elif mesh_size == 50:
            code = self.code_50
        elif mesh_size == 20:
            code = self.code_20
        elif mesh_size == 5:
            code = self.code_5
        elif mesh_size == 2:
            code = self.code_2

        return code

    def get_coordinate(self, coefficient=1):
        self.coordinate_x = int((self.longitude- 100) * 80000/coefficient)
        self.coordinate_y = int(self.latitude * 3 / 2 * 80000/coefficient)

        return {"x": self.coordinate_x, "y": self.coordinate_y}


    @classmethod
    def get_latitudeandlongitude(cls, latitude, longitude):
        return cls(latitude, longitude)

    @staticmethod
    def distance(latitude_a, longitude_a, latitude_b, longitude_b):
        latitude_a = latitude_a
        longitude_a = longitude_a
        latitude_b = latitude_b
        longitude_b = longitude_b

        def latitude_and_longitude_2_radian(latitude, longitude):
            latitude = math.radians(latitude)
            longitude = math.radians(longitude)
            return {"latitude": latitude, "longitude": longitude}

        def convert_2_rectangular_coordinate(latitude, longitude):
            RE = 6378136.59  # 地球の赤道半径(m)
            Rp = 6356752  # 地球の曲半径(m)
            f = (RE - Rp) / RE
            e2 = f * (2 - f)
            N = RE / math.sqrt(1 - e2 * math.sin(latitude) ** 2)
            h = 0

            x = (N + h) * math.cos(latitude) * math.cos(longitude)
            y = (N + h) * math.cos(latitude) * math.sin(longitude)
            z = (N * (1 - e2) + h) * math.sin(latitude)

            return {"x": x, "y": y, "z": z}

        def distance_a2b(x_a, x_b, y_a, y_b, z_a, z_b):
            return math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2 + (z_a - z_b) ** 2)

        lati_and_longi_a = latitude_and_longitude_2_radian(latitude_a, longitude_a)
        lati_and_longi_b = latitude_and_longitude_2_radian(latitude_b, longitude_b)
        coordinate_a = convert_2_rectangular_coordinate(lati_and_longi_a["latitude"],
                                                        lati_and_longi_a["longitude"])
        coordinate_b = convert_2_rectangular_coordinate(lati_and_longi_b["latitude"],
                                                        lati_and_longi_b["longitude"])
        distance = distance_a2b(coordinate_a["x"], coordinate_b["x"], coordinate_a["y"],
                                coordinate_b["y"], coordinate_a["z"], coordinate_b["z"])
        distance = round(distance/1000, 3)

        return distance

    @staticmethod
    def triangle_area(latitude_a, longitude_a, latitude_b, longitude_b,
                      latitude_c, longitude_c):
        length_a2b = LatitudeAndLongitude.distance(latitude_a, longitude_a,
                                                   latitude_b, longitude_b)
        length_b2c = LatitudeAndLongitude.distance(latitude_b, longitude_b,
                                                   latitude_c, longitude_c)
        length_c2a = LatitudeAndLongitude.distance(latitude_c, longitude_c,
                                                   latitude_a, longitude_a)
        s = (length_a2b + length_b2c + length_c2a) / 2

        area = math.sqrt(s * (s - length_a2b) * (s - length_b2c) * (s - length_c2a))

        return area

    @staticmethod
    def rectangle_area(latitude_a, longitude_a, latitude_b, longitude_b,
                       latitude_c, longitude_c, latitude_d, longitude_d):
        triangle_area_abc = LatitudeAndLongitude.triangle_area(
            latitude_a, longitude_a, latitude_b, longitude_b, latitude_c, longitude_c)
        triangle_area_bcd = LatitudeAndLongitude.triangle_area(
            latitude_b, longitude_b, latitude_c, longitude_c, latitude_d, longitude_d)
        triangle_area_cda = LatitudeAndLongitude.triangle_area(
            latitude_c, longitude_c, latitude_d, longitude_d, latitude_a, longitude_a)
        triangle_area_dab = LatitudeAndLongitude.triangle_area(
            latitude_d, longitude_d, latitude_a, longitude_a, latitude_b, longitude_b)

        area = (triangle_area_abc + triangle_area_bcd
                + triangle_area_cda + triangle_area_dab) / 2

        return area

    @staticmethod
    def dict2json(North, South, East, West, **kwargs):
        myjson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [West, South],
                        [East, South],
                        [East, North],
                        [West, North],
                        [West, South]
                    ]
                ]
            },
            "properties": kwargs
        }

        return myjson

    @staticmethod
    def dict2wkt(North, South, East, West):
        wkt = "Polygon((" \
              + str(West) + " " + str(South) + "," \
              + str(East) + " " + str(South) + "," \
              + str(East) + " " + str(North) + "," \
              + str(West) + " " + str(North) + "," \
              + str(West) + " " + str(South) + "))"

        return wkt