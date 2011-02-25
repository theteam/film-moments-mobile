import urllib2
import simplejson
req = urllib2.Request("http://moments.findanyfilm.com/api/moments/all/latest")
opener = urllib2.build_opener()
f = opener.open(req)
data = simplejson.load(f)

moments = ""
for m in data:
    moments += '<li><h3><a href="%(uri)s">%(film)s</a><p>%(moment)s</p></h3></li>' % {"uri": m['url'], "film": m['film']['title'], "moment": m['moment']}

print '<!DOCTYPE html><html><body><div data-role="page" id="latest"><div data-role="header"><h1>Moments worth paying for</h1></div><div data-role="content"><ul data-role="listview">%(m)s</div></div></div></body></html>'  % {"m": moments}
