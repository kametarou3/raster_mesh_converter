class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

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
        1: 拡張1m
        '''

    def get_mesh_code(self, mesh_size_coefficient):
        mesh_code = str(int(self.y / (80000/mesh_size_coefficient))) \
                  + str(int(self.x / (80000/mesh_size_coefficient)))
        if mesh_size_coefficient == 80000:
            mesh_code = mesh_code
        elif mesh_size_coefficient == 10000:
            mesh_code += str(int(self.y % (80000 / mesh_size_coefficient))) \
                         + str(int(self.x % (80000 / mesh_size_coefficient)))
        elif mesh_size_coefficient == 5000:
            mesh_code += str(int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[0] \
                       + str(int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[0] \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2
                               + self.y % (80000 / mesh_size_coefficient) % 2 * 2 + 1))
        elif mesh_size_coefficient == 2000:
            mesh_code += str(int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[0] \
                       + str(int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[0] \
                       + str(int(self.y % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + "5"
        elif mesh_size_coefficient == 1000: # 下２桁から値を取得するため100を加算
            mesh_code += str(100 + int(self.y % (80000 / mesh_size_coefficient)))[1] \
                       + str(100 + int(self.x % (80000 / mesh_size_coefficient)))[1] \
                       + str(100 + int(self.y % (80000 / mesh_size_coefficient)))[2] \
                       + str(100 + int(self.x % (80000 / mesh_size_coefficient)))[2]
        elif mesh_size_coefficient == 500:
            mesh_code += str(100 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(100 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(100 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(100 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2
                       + int(self.y % (80000 / mesh_size_coefficient) % 2) * 2 + 1))
        elif mesh_size_coefficient == 250:
            mesh_code += str(100 + int(self.y // 4 % (80000 / (mesh_size_coefficient * 4))))[1] \
                       + str(100 + int(self.x // 4 % (80000 / (mesh_size_coefficient * 4))))[1] \
                       + str(100 + int(self.y // 4 % (80000 / (mesh_size_coefficient * 4))))[2] \
                       + str(100 + int(self.x // 4 % (80000 / (mesh_size_coefficient * 4))))[2] \
                       + str(int(self.x % (80000 / (mesh_size_coefficient)) % 4 / 2 \
                           + int(self.y % (80000 / (mesh_size_coefficient)) % 4 / 2) * 2 + 1)) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2 \
                           + int(self.y % (80000 / mesh_size_coefficient) % 2) * 2 + 1))
        elif mesh_size_coefficient == 200:
            mesh_code += str(100 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(100 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(100 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(100 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(int(self.y % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + "5"
        elif mesh_size_coefficient == 125:
            mesh_code += str(100 + int(self.y // 8 % (80000 / (mesh_size_coefficient * 8))))[1] \
                       + str(100 + int(self.x // 8 % (80000 / (mesh_size_coefficient * 8))))[1] \
                       + str(100 + int(self.y // 8 % (80000 / (mesh_size_coefficient * 8))))[2] \
                       + str(100 + int(self.x // 8 % (80000 / (mesh_size_coefficient * 8))))[2] \
                       + str(int(self.x % (80000 / (mesh_size_coefficient)) % 8 / 4 \
                           + int(self.y % (80000 / (mesh_size_coefficient)) % 8 / 4) * 2 + 1)) \
                       + str(int(self.x % (80000 / (mesh_size_coefficient)) % 4 / 2 \
                           + int(self.y % (80000 / (mesh_size_coefficient)) % 4 / 2) * 2 + 1)) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2 \
                           + int(self.y % (80000 / mesh_size_coefficient) % 2) * 2 + 1))
        elif mesh_size_coefficient == 100:
            mesh_code += str(1000 + int(self.y % (80000 / mesh_size_coefficient)))[1] \
                       + str(1000 + int(self.x % (80000 / mesh_size_coefficient)))[1] \
                       + str(1000 + int(self.y % (80000 / mesh_size_coefficient)))[2] \
                       + str(1000 + int(self.x % (80000 / mesh_size_coefficient)))[2] \
                       + str(1000 + int(self.y % (80000 / mesh_size_coefficient)))[3] \
                       + str(1000 + int(self.x % (80000 / mesh_size_coefficient)))[3]
        elif mesh_size_coefficient == 50:
            mesh_code += str(1000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(1000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(1000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(1000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(1000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[3] \
                       + str(1000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[3] \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2
                       + int(self.y % (80000 / mesh_size_coefficient) % 2) * 2 + 1))
        elif mesh_size_coefficient == 20:
            mesh_code += str(1000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(1000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(1000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(1000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(1000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[3] \
                       + str(1000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[3] \
                       + str(int(self.y % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + "5"
        elif mesh_size_coefficient == 10:
            mesh_code += str(10000 + int(self.y % (80000 / mesh_size_coefficient)))[1] \
                       + str(10000 + int(self.x % (80000 / mesh_size_coefficient)))[1] \
                       + str(10000 + int(self.y % (80000 / mesh_size_coefficient)))[2] \
                       + str(10000 + int(self.x % (80000 / mesh_size_coefficient)))[2] \
                       + str(10000 + int(self.y % (80000 / mesh_size_coefficient)))[3] \
                       + str(10000 + int(self.x % (80000 / mesh_size_coefficient)))[3] \
                       + str(10000 + int(self.y % (80000 / mesh_size_coefficient)))[4] \
                       + str(10000 + int(self.x % (80000 / mesh_size_coefficient)))[4]
        elif mesh_size_coefficient == 5:
            mesh_code += str(10000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(10000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[1] \
                       + str(10000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(10000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[2] \
                       + str(10000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[3] \
                       + str(10000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[3] \
                       + str(10000 + int(self.y // 2 % (80000 / (mesh_size_coefficient * 2))))[4] \
                       + str(10000 + int(self.x // 2 % (80000 / (mesh_size_coefficient * 2))))[4] \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 2
                       + int(self.y % (80000 / mesh_size_coefficient) % 2) * 2 + 1))
        elif mesh_size_coefficient == 2:
            mesh_code += str(10000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(10000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[1] \
                       + str(10000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(10000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[2] \
                       + str(10000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[3] \
                       + str(10000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[3] \
                       + str(10000 + int(self.y // 5 % (80000 / (mesh_size_coefficient * 5))))[4] \
                       + str(10000 + int(self.x // 5 % (80000 / (mesh_size_coefficient * 5))))[4] \
                       + str(int(self.y % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + str(int(self.x % (80000 / mesh_size_coefficient) % 5) * 2) \
                       + "5"
        elif mesh_size_coefficient == 1:
            mesh_code += str(100000 + int(self.y % (80000 / mesh_size_coefficient)))[1] \
                       + str(100000 + int(self.x % (80000 / mesh_size_coefficient)))[1] \
                       + str(100000 + int(self.y % (80000 / mesh_size_coefficient)))[2] \
                       + str(100000 + int(self.x % (80000 / mesh_size_coefficient)))[2] \
                       + str(100000 + int(self.y % (80000 / mesh_size_coefficient)))[3] \
                       + str(100000 + int(self.x % (80000 / mesh_size_coefficient)))[3] \
                       + str(100000 + int(self.y % (80000 / mesh_size_coefficient)))[4] \
                       + str(100000 + int(self.x % (80000 / mesh_size_coefficient)))[4] \
                       + str(100000 + int(self.y % (80000 / mesh_size_coefficient)))[5] \
                       + str(100000 + int(self.x % (80000 / mesh_size_coefficient)))[5]



        return mesh_code