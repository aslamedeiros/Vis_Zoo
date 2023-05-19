import streamlit as st
import os
import streamlit.components.v1 as components


def load_components():
  # loading my components
  root_dir = os.path.dirname(os.path.abspath(__file__))

  build_dir_family = os.path.join(root_dir, "components"+os.sep+"family_selector_component"+os.sep+"family_selector"+os.sep+"frontend"+os.sep+"build")

  family_selector_component = components.declare_component(
    "family_selector",
    path=build_dir_family,
  )

  build_dir_type = os.path.join(root_dir, "components"+os.sep+"type_selector_component"+os.sep+"type_selector"+os.sep+"frontend"+os.sep+"build")

  type_selector_component = components.declare_component(
    "type_selector",
    path=build_dir_type,
  )

  # functions definition
  def family_selector(families, key):
      component_value = family_selector_component(familias = families, default=families, key=key)
      return component_value

  def type_selector(types, key):
    component_value = type_selector_component(types = types, default = types, key=key)
    return component_value

  return family_selector, type_selector


#depending on each app_version, different selectors will be loaded
def get_selectors(data, app_version, colors):

  # loading families informations and color
  families, orders = colors
  list_families = get_selection_list(families)
  list_orders = get_selection_list(orders)
  list_types = list()

  # handling Types, creating the Type list for the Type selector
  type_names = data['type_status'].unique()
  for index in range(len(type_names)):
    new_type = dict()
    new_type['name'] = str(type_names[index])
    new_type['shape'] = "square"
    new_type['selected'] = True
    list_types.append(new_type)

  if app_version == 'reptiles' or app_version == 'polychaeta' or app_version == 'annelida':
    return [
      {
        'name':'order',
        'selector': 'family_selector',
        'list':list_orders
      },
      {
        'name':'family',
        'selector': 'family_selector',
        'list':list_families
      },
      {
        'name':'type_status',
        'selector': 'type_selector',
        'list':list_types
      }
    ]
  elif app_version == 'crustaceas':
    return [
      {
        'name':'infraorder',
        'selector': 'family_selector',
        'list':list_orders
      },
      {
        'name':'family',
        'selector': 'family_selector',
        'list':list_families
      },
      {
        'name':'type_status',
        'selector': 'type_selector',
        'list':list_types
      },
    ]
  elif app_version == 'GBIF':
    return [
      {
        'name':'order',
        'selector': 'family_selector',
        'list':list_orders
      },
      {
        'name':'family',
        'selector': 'family_selector',
        'list':list_families
      },
      {
        'name':'type_status',
        'selector': 'type_selector',
        'list':list_types
      }
    ]

#this function transforms a dict into a list of dict adding a selection field
def get_selection_list(colors_dict):
  list_name = list(colors_dict.keys())
  list_color = list(colors_dict.values())
  select_list = list()

  for index in range(len(list_name)):
    el = dict()
    el["name"] = list_name[index]
    el["color"] = list_color[index]
    el["selected"] = True
    select_list.append(el)
  return select_list

#this function transforms the output of the selector components in filter format used in the filter function
def get_filters_out(selectors_components):
  list_selector_output = list()
  for selector in selectors_components:
    st.write(selector['name'])
    selector['list'] = st.session_state[selector['selector']](selector['list'], selector['name'])
    list_selector_output.append((selector['name'], selector['list']))

  list_filter_out = list()
  for list_sel in list_selector_output:
    filter_out = list()
    for occ in list_sel[1]:
      if not(occ['selected']):
        filter_out.append(occ['name'])
    list_filter_out.append({'name_column':list_sel[0], 'filter':filter_out})

  return list_filter_out