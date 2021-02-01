# coding=utf-8
import hashlib
import requests
# from samples.example_youguo import get_acos_dec, get_acos_enc
import json
import time

def get_md5(str):
    m = hashlib.md5()
    m.update(str.encode())
    m.hexdigest()
    return m.hexdigest()


strs = "Cc$nceR6qGg5^Pdv%4@C"
data = '''{"params":{"cateId":"6704026448565313536","type":"up","page":1,"debug":"0","recdebug":"0"},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609727896","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"269F3F0B0FA0DC291BA69BE81C633EA8"}}'''
# data = '''{"params":{"cateId":"6704026448565313536","type":"up","page":1,"debug":"0","recdebug":"0"},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609727896","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"%s","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"269F3F0B0FA0DC291BA69BE81C633EA8"}}'''

# data = '''{"params":{"keyword":"格斗女王"},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609819041","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"756135AE4B6D18387B00B121FE46D82B"}}'''
# data = '''{"params":{"page":"4","cateType":4},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609821803","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"53268000E1C1D25AE7521F83745C5560"}}'''

# data = '''{"params":{"pageToken":"1","objectId":"614068628494612486","cateType":1,"ytbId":"","syncStatus":0},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609827083","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"8BBF7FD08FA95B55AC3453BBF1773C81"}}'''

# data = '''{"params":{"userId":"614068628494612486","ytbId":"","syncStatus":0},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"0","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609827084","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"","_androidID":"e500853bc55c419c","_reqId":"2DBF513B4614154006046B49482CD5E2"}}'''
# data = '''{"params":{"videoId":"6693347811797045248","page":"1","size":20},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"NzRnVEFta3FKZXpJZmNjUDduVUJZUkRSdjRkUkxjc2FHOFZHQWw2dzIyMF8=","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"709593725950622752","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609828353","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"709593725950622752","_androidID":"e500853bc55c419c","_reqId":"3E90BF78461E0C6CB755CA8D535E72C4"}}'''
# data = '''{"params":{"pageToken":"1"},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"NzRnVEFta3FKZXpJZmNjUDduVUJZUkRSdjRkUkxjc2FHOFZHQWw2dzIyMF8=","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"709593725950622752","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609851047","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"709593725950622752","_androidID":"e500853bc55c419c","_reqId":"208CBA0A6D93C66E25B7F6761AC72053"}}'''
# data = '''{"params":{"labelId":"-1","pageToken":"1"},"common":{"_isVirtualApp":0,"_cpu":"arm64-v8a","_nId":"1","_localIp":"192.168.1.106","_umengId":"aia75e239f5383a0705341fd138bf2154e","_token":"NzRnVEFta3FKZXpJZmNjUDduVUJZUkRSdjRkUkxjc2FHOFZHQWw2dzIyMF8=","_imei":"e500853bc55c419c","_dId":"Redmi+Note+4","_abId":"","_vOs":"8.1.0","_vApp":"141500","_youngModel":0,"_devId":"AF3245E2DD68D57FAA0872C34FC7FBBF","_uId":"709593725950622752","_cpuId":"Qualcomm Technologies, Inc MSM8953","_lang":"zh_CN","_rt":"1","_plat":"android","_vName":"1.2.2","_pcId":"xiaomi_market_yg","_oaid":"","_deviceYear":2014,"_carrier":null,"_pcId2":"xiaomi_market_yg","_dpi":"420","_net":"1","_resolution":"1080x1920","_density":"2.625","_t":"1609851048","_facturer":"Xiaomi","_pName":"com.yixia.youguo","_appName":"油果浏览器","_udid":"A3B87ED9114E9979C36F0F4240D8C242","_model":"Redmi+Note+4","_vOsCode":"27","_aKey":"ANDROID","_pNum":"","_imei3":"","_mac":"00:0a:f5:6c:0a:10","_imei2":"","_brand":"Xiaomi","_userId":"709593725950622752","_androidID":"e500853bc55c419c","_reqId":"E0F4BE293B1B149ACA61C6D8C5168C7B"}}'''
sign = get_md5(data + strs)[2:22].lower()
headers = {
    'Sign': sign,
    'Content-Type': 'application/octet-stream',
    'Host': 'ygapi.youguotv.com',
    'User-Agent': 'okhttp/4.8.1',
}
# data2 = get_acos_enc(data)
# print(data2)

info = requests.post("http://127.0.0.1:7881/encryption", json={'args': data})
data2 = info.json().get("data")
# url = "http://ygapi.youguotv.com/v3/category/list.json"
url = 'http://ygapi.youguotv.com/v3/recommend/index.json'
# url = 'http://ygapi.youguotv.com/v3/search/video.json'#搜索
# url = "http://ygapi.youguotv.com/v3/contribute/recom.json"

# url = "http://ygapi.youguotv.com/v3/contribute/subvideos.json"
# url = "http://ygapi.youguotv.com/v3/user/home.json"
# url = "http://ygapi.youguotv.com/v3/comment/list.json"
# url = "http://ygapi.youguotv.com/v3/discover/labels.json"
# url = "http://ygapi.youguotv.com/v3/discover/themes.json"

response = requests.post(url, headers=headers, data=eval(data2))
res = response.content
# content = get_acos_dec(res)
content = str(bytearray(res))

info = requests.post("http://127.0.0.1:7881/decryption", json={'content': content})
print(info.json())
