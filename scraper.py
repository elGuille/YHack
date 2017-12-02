import urllib
file = urllib.URLopener()

for year in range(2009, 2018):
    for month in range(1, 12):
        name = "RS_" + str(year) + "-" + str(month).zfill(2) + "".bz2"
        url = "https://files.pushshift.io/reddit/submissions/" + name
        
        try:
            file.retrieve(url, name)
            print(name)
        except IOError:
            pass


#https://files.pushshift.io/reddit/submissions/RS_2006-01.bz2