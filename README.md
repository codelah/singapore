### Singapore

This project attempts to consolidate data.gov.sg data under a single unified python library.

Currently, we are linking two individual libraries into this package but we are accepting pull requests for other wrappers of other datasets.

Currently supported datasets are:

* [Onemap](http://github.com/ruiwen/onemap)
* [NEA](http://github.com/davidchua/nea_api)

To use, all you need to do is to

```
# python
from singapore import onemap
from singapore import nea_api
```

#### OneMap

```
>>>
>>> from singapore import onemap
>>> OM = onemap.OneMap("onemap_key")
>>>
>>> res = OM.search_address("city hall")
>>> type(res)
<class 'core.ext.onemap.OneMapResult'>
>>>
>>> res
[{u'searchval': u'CITY HALL', u'category': u'Building', u'y': u'30360.5886', u'x': u'30051.7694'}, {u'searchval': u'CITY HALL (MONUMENTS)', u'category': u'Culture', u'y':     u'30339.5771', u'x': u'30047.6749'}, {u'searchval': u'CITY HALL (STREET AND PLACES)', u'category': u'Culture', u'y': u'30318.8100', u'x': u'30064.6100'}, {u'searchval': u'CITY     HALL AND THE PADANG (HERITAGE SITES)', u'category': u'Culture', u'y': u'30340.3699', u'x': u'30049.0300'}, {u'searchval': u'CITY HALL MRT STATION', u'category': u'Building',     u'y': u'30597.7817', u'x': u'30139.4704'}, {u'searchval': u'CITY HALL MRT STATION (EW13/NS25) (FRIENDLY BUILDINGS)', u'category': u'Community', u'y': u'30597.7817', u'x':     u'30139.4704'}, {u'searchval': u'CITY HALL MRT STATION EXIT A', u'category': u'Building', u'y': u'30611.1767', u'x': u'30182.8492'}, {u'searchval': u'CITY HALL MRT STATION EXIT     B', u'category': u'Building', u'y': u'30610.8982', u'x': u'30073.6413'}, {u'searchval': u'CITY HALL/ESPLANADE MRT STATION EXIT A', u'category': u'Building', u'y':     u'30415.3350', u'x': u'30369.4938'}, {u'searchval': u'CITY HALL/ESPLANADE MRT STATION EXIT B', u'category': u'Building', u'y': u'30457.5147', u'x': u'30385.8054'},     {u'searchval': u'CITY HALL/ESPLANADE MRT STATION EXIT C', u'category': u'Building', u'y': u'30412.5744', u'x': u'30434.3890'}, {u'searchval': u'CITY HALL/ESPLANADE MRT STATION     EXIT D', u'category': u'Building', u'y': u'30367.6908', u'x': u'30424.1965'}, {u'searchval': u'CITY HALL/ESPLANADE MRT STATION EXIT E', u'category': u'Building', u'y':     u'30479.6293', u'x': u'30394.6855'}]
>>>
```

Queries return a OneMapResult object, containing one or more OneMapResultItems

```
>>> geo = OM.geocode("%s,%s" % (res[0]['x'], res[0]['y']))
>>> type(geo)
<class 'core.ext.onemap.OneMapResult'>
>>>
>>> geo
[{u'buildingname': u'CITY HALL', 'y': 30338.9616, u'block': u'3', u'postalcode': u'178958', 'x': 30047.2715, u'road': u"SAINT ANDREW'S ROAD"}, {u'buildingname': u'THE ADELPHI',     'y': 30398.6047, u'block': u'1', u'postalcode': u'179803', 'x': 29987.9521, u'road': u'COLEMAN STREET'}, {u'buildingname': u'THE OLD SUPREME COURT BUILDING', 'y': 30253.3835,     u'block': u'1', u'postalcode': u'178957', 'x': 30025.5209, u'road': u"SAINT ANDREW'S ROAD"}, {u'buildingname': u'SUPREME COURT BUILDING', 'y': 30322.8247, u'block': u'1',     u'postalcode': u'178879', 'x': 29938.7931, u'road': u'SUPREME COURT LANE'}, {u'buildingname': u'FORMER SUPREME COURT BUILDING', 'y': 30250.6217, u'block': u'1', u'postalcode':     u'178957', 'x': 29985.2869, u'road': u"SAINT ANDREW'S ROAD"}]
>>>
```

For more information, check out the main [README](https://github.com/ruiwen/onemap)

#### NEA_API

Sample:

```
from nea_api import NEA

nea = NEA(api_key="<api key>")
results = nea.get_pm25()

# ipdb> results
OrderedDict([('channel', OrderedDict([('title', 'PM2.5 Update'), ('source', 'Airviro'), ('item', OrderedDict([('region', [OrderedDict([('id', 'rNO'), ('latitude', '1.41803'), ('longitude', '103.82000'), ('record', OrderedDict([('@timestamp', '20160406140000'), ('reading', OrderedDict([('@type', 'PM25_RGN_1HR'), ('@value', '17')]))]))]), OrderedDict([('id', 'rCE'), ('latitude', '1.35735'), ('longitude', '103.82000'), ('record', OrderedDict([('@timestamp', '20160406140000'), ('reading', OrderedDict([('@type', 'PM25_RGN_1HR'), ('@value', '27')]))]))]), OrderedDict([('id', 'rEA'), ('latitude', '1.35735'), ('longitude', '103.94000'), ('record', OrderedDict([('@timestamp', '20160406140000'), ('reading', OrderedDict([('@type', 'PM25_RGN_1HR'), ('@value', '19')]))]))]), OrderedDict([('id', 'rWE'), ('latitude', '1.35735'), ('longitude', '103.70000'), ('record', OrderedDict([('@timestamp', '20160406140000'), ('reading', OrderedDict([('@type', 'PM25_RGN_1HR'), ('@value', '26')]))]))]), OrderedDict([('id', 'rSO'), ('latitude', '1.29587'), ('longitude', '103.82000'), ('record', OrderedDict([('@timestamp', '20160406140000'), ('reading', OrderedDict([('@type', 'PM25_RGN_1HR'), ('@value', '30')]))]))])])]))]))])
```

For more information, check out the main [README](https://github.com/davidchua/nea_api)

#### TODO

1. Setup an actual [readthedocs](https://readthedocs.org/)
2. Wrapper for Singaporepools, LTA dataset

#### Contributors

* [Ruiwen Chua](http://github.com/ruiwen)
* [David Chua](http://github.com/davidchua)
_We're not related!_
