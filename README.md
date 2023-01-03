* 包介绍：Python语言的身份证前6位行政区划代码与地区名称对应。通过传入省市县（区）完整名称返回地区代码。

* PIP安装：```pip install citydata```

* 地区信息 json/dict 组成示例：

  ```json
            {
            "id": "110101",
            "name": "东城区",
            "parentId": "110100",
            "shortName": "",
            "letter": "",
            "cityCode": "",
            "pinyin": ""
        }
  ```

* API函数代码

  ```python
    # args 最多接受三个参数，顺序依次为省、市、县（区）
    def get_city_id(self, *args) -> tuple[str, ...]:
        if not args or len(args) > 3:
            raise ValueError("参数错误")
        # 一个参数，省级/市级/县（区）级
        # 因存在重名县（区），不建议直接查询县（区）级
        if len(args) == 1:
            province = args[0]
            for area in self.cityData:
                if area['name'] == province:
                    province_id = area['id']
                    return province_id, 
            raise ValueError("未能找到对应的行政区划代码，请检查参数")
        
        # 两个参数，省市两级或市县（区）级两级
        elif len(args) == 2:
            province, city = args
            province_id = "0"
            for area in self.cityData:
                if area['name'] == province:
                    province_id = area['id']
                    continue
                if area['name'] == city and area['parentId'] == province_id:
                    city_id = area['id']
                    return province_id, city_id
            raise ValueError("未能找到对应的行政区划代码，请检查参数")

        # 三个参数，省市县(区)三级
        else:
            province, city, county = args
            province_id, city_id = "0", "0"
            for area in self.cityData:
                if area['name'] == province:
                    province_id = area['id']
                    continue
                if area['name'] == city and area['parentId'] == province_id:
                    city_id = area['id']
                    continue
                if area['name'] == county and area['parentId'] == city_id:
                    county_id = area['id']
                    return province_id, city_id, county_id
            raise ValueError("未能找到对应的行政区划代码，请检查参数")
  
  ```

  

* 引用举例

  ```python
  from citydata import CityData
  city_data = CityData()
  city_ids = city_data.get_city_id('河北省','石家庄市','裕华区')  # 包含省\市\县（区）字样的完整行政区名，否则找不到结果
  province_id = city_ids[0] # 130000 (str)
  city_id = city_ids[1] # 130100 (str)
  county_id = county_id[2] # 130108 (str)
  ```

  

* TODO
  - 城市简称
  - 邮政编码
  - 城市拼音
