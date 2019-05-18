import requests
import json

class ComputerVision(object):
    def __init__(self, subscription_key):
        self.headers = {'Ocp-Apim-Subscription-Key': subscription_key }

    def get_image_information(self, image_url, params):
        if not image_url:
            return None
            
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
        analyze_url = vision_base_url + "analyze"
        data = {'url': image_url}
        response = requests.post(analyze_url, headers=self.headers, params=params, json=data)
        if not response.raise_for_status():
            json_data = response.json()
        
        return json_data
    
    def extract_text_from_image(self, image_url, params):
        if not image_url:
            return None
        
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
        ocr_url = vision_base_url + "ocr"
        data    = {'url': image_url}
        response = requests.post(ocr_url, headers=self.headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()
        # Extract the word bounding boxes and text.
        line_infos = [region["lines"] for region in analysis["regions"]]
        word_infos = []
        for line in line_infos:
            for word_metadata in line:
                for word_info in word_metadata["words"]:
                    word_infos.append(word_info)
        return word_infos


subscription_key = "e7d14872058a4883ae37ba5efe41a5d8"   # need to set own key

# get info into image
params = {'visualFeatures': 'Categories, Description, Color'} # Faces, Tags ...
cp = ComputerVision(subscription_key)

image_url = "https://www.newsweekjapan.jp/stories/assets_c/2018/06/BNK01-thumb-720xauto-135730.jpg"
#image_url1 = "https://www.atpress.ne.jp/releases/47659/img_47659_1.jpg"
#image_url2 = "https://www.atpress.ne.jp/releases/183335/LL_img_183335_1.jpg"
data = cp.get_image_information(image_url=image_url, params=params)

# exxtract text from image
params  = {'language': 'unk', 'detectOrientation': 'true'}

image_url = "https://www.giants.jp/xml/img/img_20190207140307246_3048947343092514774.jpg"
data = cp.extract_text_from_image(image_url=image_url, params=params)
