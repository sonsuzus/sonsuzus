import requests
import discord
import datetime
import time

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2023-12-31&minmagnitude=4&limit=1&orderby=time&latitude=39&longitude=35&maxradiuskm=1000"

# Her döngüden sonra beklenecek saniye sayısı
# Eğer hiç beklemezseniz site sizi kısa süreliğine banlıyor.
delay = 60

def get_earthquake_info():
    try:
        response = requests.get(url)
        data = response.json()
        # Eğer site hata döndürürse None döndür.
        if response.status_code != 200:
            return None
        earthquake_info = data['features'][0]['properties']
        return earthquake_info
    except:
        return None

def on_ready():
    last_earthquake_timestamp = None
    
    while True:
        # Siteye çok fazla request attığım için kısa süreli ban yedim.
        # Bunun için her döngüye 10 dk'lık bir delay ekledim
        earthquake_info = get_earthquake_info()
        
        # Eğer info alamadıysak bir sonraki döngye geç
        if earthquake_info is None:
            time.sleep(delay)
            continue
        
        magnitude = earthquake_info['mag']
        place = earthquake_info['place']
        # Milisaniyeden saniyeye çevirir
        earthquake_time = earthquake_info['time'] // 1000
        
        # Eğer önceki yazdırılan depremin zamanı ile şimdiki depremin zamanı aynıysa aynı depremlerdir.
        # Bu yüzden tekrar yazdırmak yerine bir sonraki döngüye geçer.
        # Eğer değilse aşağıya devam eder ve last_earthquake_timestamp değişkenine şimdiki zamanı eşitler.
        if last_earthquake_timestamp == earthquake_time:
            time.sleep(delay)
            continue
        last_earthquake_timestamp = earthquake_time
        
        # Epoch zamanından alıp datetime objesine çevirir.
        earthquake_time = datetime.datetime.fromtimestamp(earthquake_time)
        
        # Tarih ve saati yazdırabilmek için
        date_str = earthquake_time.strftime('%Y/%m/%d')
        time_str = earthquake_time.strftime('%H:%M:%S')
        
        detailed_info_url = earthquake_info['url']
        message = '**DİKKAT! TÜRKİYEDE DEPREM!!**\n' + \
        f'Büyüklk: {magnitude}\n' + \
        f'Lokasyon: {place}\n' + \
        f'Tarih: {date_str}\n' + \
        f'Saat: {time_str}\n' + \
        f'Detaylı bilgi: {detailed_info_url}'
        
        print(message)
        time.sleep(delay)
on_ready()
