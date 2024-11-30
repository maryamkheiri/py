import concurrent.futures
import requests
import time
images_url = [
    "https://img.freepik.com/free-photo/white-t-shirts-with-copy-space-gray-background_53876-104920.jpg",
    "https://img.freepik.com/free-photo/black-t-shirts-with-copy-space_53876-102012.jpg",
    "https://img.freepik.com/free-photo/exterior-view-modern-white-house-with-courtyard-patio-area-green-grass-lawn-garden-car-evening_174699-1485.jpg",
    "https://img.freepik.com/free-photo/abstract-grunge-decorative-relief-navy-blue-stucco-wall-texture-wide-angle-rough-colored-background_1258-28311.jpg",
    "https://img.freepik.com/free-photo/many-isolated-assorted-pizzas-collage-menu-design_219193-5937.jpg",
    "https://img.freepik.com/free-photo/hand-presenting-model-house-home-loan-campaign_53876-104970.jpg",
    "https://img.freepik.com/free-photo/sports-tools_53876-138077.jpg"
]
def download_myfile(image_url):
    url_data=requests.get(image_url).content
    url_name=image_url.split("/")[4]
    url_name=f"{url_name}.jpg"
    with open("image_url" , "wb") as img:
        img.write(url_data)
        print(url_name,"was downloding..")
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks=executor.map(download_myfile,images_url)
    
