import requests
import json

class ComputerVision(object):
    def __init__(self, subscription_key):
        self.headers = {'Ocp-Apim-Subscription-Key': subscription_key }
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
        self.analyze_url = vision_base_url + "analyze"

    def get_image_information(self, image_url, params):
        if not image_url:
            return None
        data    = {'url': image_url}

        response = requests.post(self.analyze_url, headers=self.headers, params=params, json=data)
        if not response.raise_for_status():
            json_data = response.json()
        
        return json_data

subscription_key = "Write ur key"   # need to set own key
params = {'visualFeatures': 'Categories, Description, Color'}
# Faces, Tags ...
cp = ComputerVision(subscription_key)


image_url = "https://www.newsweekjapan.jp/stories/assets_c/2018/06/BNK01-thumb-720xauto-135730.jpg"
image_url1 = "https://www.atpress.ne.jp/releases/47659/img_47659_1.jpg"
image_url2 = "https://www.atpress.ne.jp/releases/183335/LL_img_183335_1.jpg"

data = cp.get_image_information(image_url=image_url, params=params)
