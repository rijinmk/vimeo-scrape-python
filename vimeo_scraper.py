import urllib
import urllib2
import json
import BeautifulSoup
url_list = ["https://vimeo.com"]
for i in range(len(url_list)):
    url = url_list[i]
    print url
    print "reading page data..."
    try:
        data_url = urllib2.urlopen(url).read()
    except:
        print "\n\n"
        print "***ERROR***"
        print "\n\n"
        continue
    print "page data read"
    print "souping data"
    soup_w = BeautifulSoup.BeautifulSoup(data_url)
    print "data souped"
    print "finding scripts"
    script_w = soup_w.findAll('script')
    print "all scripts found"
    string_sc = script_w[5].text
    json_data_link = string_sc.split("GET")[-1].split("onload")[0][3:-8]
    print "getting the json data of the video profile...."
    try:
        json_link_data = urllib2.urlopen(string_sc.split("GET")[-1].split("onload")[0][3:-8]).read()
    except:
        print "\n\n"
        print "***ERROR***"
        print "\n\n"
        continue
    json_data = json.loads(json_link_data)
    for i in range(len(json_data["request"]["files"]["progressive"])):
        if( json_data["request"]["files"]["progressive"][i]["width"]>1000):
            print "VIDEO RESOLUTION:", json_data["request"]["files"]["progressive"][i]["width"],"x",json_data["request"]["files"]["progressive"][i]["height"]
            video = json_data["request"]["files"]["progressive"][i]["url"].encode("utf-8")
    print "GETTING THE VIDEO DATA........"
    try: 
        video_data = urllib2.urlopen(video).read()
    except:
        print "\n\n"
        print "***ERROR***"
        print "\n\n"
        continue
    print "VIDEO DATA ACUIRED"
    f=open("v_videos/video_"+url.split("/")[-1]+".mp4","wb")
    print "writing video data into a file..."
    f.write(video_data)
    print "video saved"
    print "next video..."
    print "-------------------------------------------------------------------------------------------------------------------"
print "DONE."
