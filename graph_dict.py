from altair_code.Altitude import *
from altair_code.Counts_per_researcher import *
from altair_code.Family_counts_per_year import *
from altair_code.time_spacial import *
from altair_code.Type_counts import *
from altair_code.custom_chart import custom_chart

from altair_code.newAltair1 import *
from altair_code.newAltair2 import typeY_by_timeX


def get_graph_dicts(app_version):

  if app_version == 'reptiles':
    #available graphs definition
    # graphs available in the "time" section

    graphs_time = dict()
    graphs_time['collection Registers by Top 50 collectors'] = timeX_collectorY_top50
    graphs_time['description Registers by Top 50 determiners'] = timeX_determinerY_top50
    graphs_time['collection Registers by collector'] = timeX_collectorY
    graphs_time['description Registers by determiner'] = timeX_determinerY
    graphs_time['Registers by Families'] = timeX_family_countY
    graphs_time['Registers Type by Family'] = timeX_family_countTypeY
    graphs_time['Registers Type by Genus'] = timeX_genus_countTypeY
    graphs_time['Registers Type by collector'] = timeX_collector_countTypeY
    graphs_time['Registers by Order'] = timeX_order_countY
    graphs_time['Registers by Type'] = timeX_countTypeY
    graphs_time['Registers Family by continent'] = timeX_family_continentY
    graphs_time['Registers Family by country'] = timeX_family_countryY
    graphs_time['Registers Family by Brazilian States'] = timeX_family_statesY
    graphs_time['custom chart'] = custom_chart
    # graphs_time['seasonality'] = timeX_monthY
    # graphs available in the "space" section
    graphs_space = dict()
    graphs_space['altitude per family'] = familyX_altitudeY
    graphs_space['altitude per genus'] = genusX_altitudeY

  elif app_version == 'crustaceas':
    graphs_time = dict()

        ### News
    graphs_time['colletor by time'] = time_collectedX_collectorY_dash
    graphs_time['determiner by time'] = time_catalogedX_determinatorY_dash
    graphs_time['type by time'] = typeY_by_timeX


    graphs_time['collection Registers by Top 50 collectors'] = timeX_collectorY_top50
    graphs_time['description Registers by Top 50 determiners'] = timeX_determinerY_top50
    graphs_time['collection Registers by collector'] = timeX_collectorY
    graphs_time['description Registers by determiner'] = timeX_determinerY
    graphs_time['Registers by Familiy'] = timeX_family_countY
    graphs_time['Registers Type by Family'] = timeX_family_countTypeY
    graphs_time['Registers Type by Genus'] = timeX_genus_countTypeY
    graphs_time['Registers Type by collector'] = timeX_collector_countTypeY
    graphs_time['Registers by Type'] = timeX_countTypeY
    graphs_time['Registers by Infraorder'] = timeX_infraorder_countY
    graphs_time['Registers Family by continent'] = timeX_family_continentY
    graphs_time['Registers Family by country'] = timeX_family_countryY
    graphs_time['Registers Family by Brazilian States'] = timeX_family_statesY
    graphs_time['custom chart'] = custom_chart
    # graphs_time['seasonality'] = timeX_monthY
    # graphs available in the "space" section
    graphs_space = dict()
    graphs_space['depth per family'] = familyX_depthY
    
  elif app_version == 'polychaeta':
    graphs_time = dict()
    graphs_time['colletor by time'] = collector_year_dash
    graphs_time['collection Registers by Top 50 collectors'] = timeX_collectorY_top50
    graphs_time['description Registers by Top 50 determiners'] = timeX_determinerY_top50
    graphs_time['collection Registers by collector'] = timeX_collectorY
    graphs_time['description Registers by determiner'] = timeX_determinerY
    graphs_time['Registers by Familiy'] = timeX_family_countY
    graphs_time['Registers Type by Family'] = timeX_family_countTypeY
    graphs_time['Registers Type by Genus'] = timeX_genus_countTypeY
    graphs_time['Registers Type by collector'] = timeX_collector_countTypeY
    graphs_time['Registers by Type'] = timeX_countTypeY
    graphs_time['Registers by Infraorder'] = timeX_infraorder_countY
    graphs_time['Registers Family by continent'] = timeX_family_continentY
    graphs_time['Registers Family by country'] = timeX_family_countryY
    graphs_time['Registers Family by Brazilian States'] = timeX_family_statesY
    graphs_time['custom chart'] = custom_chart
    # graphs_time['seasonality'] = timeX_monthY
    # graphs available in the "space" section
    graphs_space = dict()
    graphs_space['depth per family'] = familyX_depthY_pol

  elif app_version == 'annelida':
    graphs_time = dict()
    
    ### News
    graphs_time['colletor by time'] = time_collectedX_collectorY_dash
    graphs_time['determiner by time'] = time_catalogedX_determinatorY_dash
    graphs_time['type by time'] = typeY_by_timeX

    graphs_time['colletor by time'] = collector_year_dash
    graphs_time['collection Registers by Top 50 collectors'] = timeX_collectorY_top50
    graphs_time['description Registers by Top 50 determiners'] = timeX_determinerY_top50
    graphs_time['collection Registers by collector'] = timeX_collectorY
    graphs_time['description Registers by determiner'] = timeX_determinerY
    graphs_time['Registers by Familiy'] = timeX_family_countY
    graphs_time['Registers Type by Family'] = timeX_family_countTypeY
    graphs_time['Registers Type by Genus'] = timeX_genus_countTypeY
    graphs_time['Registers Type by collector'] = timeX_collector_countTypeY
    graphs_time['Registers by Type'] = timeX_countTypeY
    graphs_time['Registers by Infraorder'] = timeX_infraorder_countY
    graphs_time['Registers Family by continent'] = timeX_family_continentY
    graphs_time['Registers Family by country'] = timeX_family_countryY
    graphs_time['Registers Family by Brazilian States'] = timeX_family_statesY
    graphs_time['custom chart'] = custom_chart

    # graphs_time['seasonality'] = timeX_monthY


    # graphs available in the "space" section
    graphs_space = dict()
    graphs_space['depth per family'] = familyX_depthY_pol
    
  elif app_version == 'GBIF':
    graphs_time = dict()
    graphs_time['collection Registers by Top 50 collectors'] = timeX_collectorY_top50
    graphs_time['description Registers by Top 50 determiners'] = timeX_determinerY_top50
    graphs_time['collection Registers by collector'] = timeX_collectorY
    graphs_time['description Registers by determiner'] = timeX_determinerY
    graphs_time['Registers by Families'] = timeX_family_countY
    graphs_time['Registers Type by Family'] = timeX_family_countTypeY
    graphs_time['Registers Type by Genus'] = timeX_genus_countTypeY
    graphs_time['Registers Type by collector'] = timeX_collector_countTypeY
    graphs_time['Registers by Order'] = timeX_order_countY
    graphs_time['Registers by Type'] = timeX_countTypeY
    graphs_time['Registers Family by country'] = timeX_family_countryY
    graphs_time['custom chart'] = custom_chart
    # graphs_time['seasonality'] = timeX_monthY
    # graphs available in the "space" section
    graphs_space = dict()
    graphs_space['altitude per family'] = familyX_altitudeY
    graphs_space['altitude per genus'] = genusX_altitudeY

  return graphs_time, graphs_space