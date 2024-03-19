import csv
import requests

ministries = []

api_url = "https://wabi-south-africa-north-a-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true"
headers = {"X-PowerBI-ResourceKey": "7f89c321-25c7-45a0-b48e-dec06704c3b7"}

#Open the Ministries file and read the lines containing the ministries, append them to a list.
with open('../files/mdas_2024.csv', 'r') as ministries_file:
	csv_reader = csv.reader(ministries_file)
	for line in  csv_reader:
		ministries.append(line[0])

def get_query(ministry):
	query = {
	    "version": "1.0.0",
	    "queries": [
	        {
	            "Query": {
	                "Commands": [
	                    {
	                        "SemanticQueryDataShapeCommand": {
	                            "Query": {
	                                "Version": 2,
	                                "From": [
	                                    {
	                                        "Name": "m",
	                                        "Entity": "Master MDA",
	                                        "Type": 0
	                                    },
	                                    {
	                                        "Name": "m1",
	                                        "Entity": "Master Year",
	                                        "Type": 0
	                                    }
	                                ],
	                                "Select": [
	                                    {
	                                        "Column": {
	                                            "Expression": {
	                                                "SourceRef": {
	                                                    "Source": "m"
	                                                }
	                                            },
	                                            "Property": "MDA -Final List with 2021 updates"
	                                        },
	                                        "Name": "Master MDA.MDA -Final List with 2021 updates"
	                                    }
	                                ],
	                                "Where": [
	                                    {
	                                        "Condition": {
	                                            "In": {
	                                                "Expressions": [
	                                                    {
	                                                        "Column": {
	                                                            "Expression": {
	                                                                "SourceRef": {
	                                                                    "Source": "m1"
	                                                                }
	                                                            },
	                                                            "Property": "Year"
	                                                        }
	                                                    }
	                                                ],
	                                                "Values": [
	                                                    [
	                                                        {
	                                                            "Literal": {
	                                                                "Value": "2024L"
	                                                            }
	                                                        }
	                                                    ]
	                                                ]
	                                            }
	                                        }
	                                    },
	                                    {
	                                        "Condition": {
	                                            "In": {
	                                                "Expressions": [
	                                                    {
	                                                        "Column": {
	                                                            "Expression": {
	                                                                "SourceRef": {
	                                                                    "Source": "m"
	                                                                }
	                                                            },
	                                                            "Property": "Mother Ministry"
	                                                        }
	                                                    }
	                                                ],
	                                                "Values": [
	                                                    [
	                                                        {
	                                                            "Literal": {
	                                                                "Value": f"'{ministry}'"
	                                                            }
	                                                        }
	                                                    ]
	                                                ]
	                                            }
	                                        }
	                                    }
	                                ]
	                            },
	                            "Binding": {
	                                "Primary": {
	                                    "Groupings": [
	                                        {
	                                            "Projections": [
	                                                0
	                                            ]
	                                        }
	                                    ]
	                                },
	                                "DataReduction": {
	                                    "DataVolume": 3,
	                                    "Primary": {
	                                        "Window": {}
	                                    }
	                                },
	                                "IncludeEmptyGroups": "true",
	                                "Version": 1
	                            },
	                            "ExecutionMetricsKind": 1
	                        }
	                    }
	                ]
	            },
	            "QueryId": "",
	            "ApplicationContext": {
	                "DatasetId": "ee3f7950-f10f-457c-a568-5e91b6068a66",
	                "Sources": [
	                    {
	                        "ReportId": "710dc341-d6db-40f9-979d-db7a5377381e",
	                        "VisualId": "83ad6b5e264b860e2182"
	                    }
	                ]
	            }
	        }
	    ],
	    "cancelQueries": [],
	    "modelId": 303809
	}

	return query

def get_query_RT(ministry, RT):
	query_RT = {
	    "version": "1.0.0",
	    "queries": [
	        {
	            "Query": {
	                "Commands": [
	                    {
	                        "SemanticQueryDataShapeCommand": {
	                            "Query": {
	                                "Version": 2,
	                                "From": [
	                                    {
	                                        "Name": "m",
	                                        "Entity": "Master MDA",
	                                        "Type": 0
	                                    },
	                                    {
	                                        "Name": "m1",
	                                        "Entity": "Master Year",
	                                        "Type": 0
	                                    }
	                                ],
	                                "Select": [
	                                    {
	                                        "Column": {
	                                            "Expression": {
	                                                "SourceRef": {
	                                                    "Source": "m"
	                                                }
	                                            },
	                                            "Property": "MDA -Final List with 2021 updates"
	                                        },
	                                        "Name": "Master MDA.MDA -Final List with 2021 updates"
	                                    }
	                                ],
	                                "Where": [
	                                    {
	                                        "Condition": {
	                                            "In": {
	                                                "Expressions": [
	                                                    {
	                                                        "Column": {
	                                                            "Expression": {
	                                                                "SourceRef": {
	                                                                    "Source": "m1"
	                                                                }
	                                                            },
	                                                            "Property": "Year"
	                                                        }
	                                                    }
	                                                ],
	                                                "Values": [
	                                                    [
	                                                        {
	                                                            "Literal": {
	                                                                "Value": "2024L"
	                                                            }
	                                                        }
	                                                    ]
	                                                ]
	                                            }
	                                        }
	                                    },
	                                    {
	                                        "Condition": {
	                                            "In": {
	                                                "Expressions": [
	                                                    {
	                                                        "Column": {
	                                                            "Expression": {
	                                                                "SourceRef": {
	                                                                    "Source": "m"
	                                                                }
	                                                            },
	                                                            "Property": "Mother Ministry"
	                                                        }
	                                                    }
	                                                ],
	                                                "Values": [
	                                                    [
	                                                        {
	                                                            "Literal": {
	                                                                "Value": f"'{ministry}'"
	                                                            }
	                                                        }
	                                                    ]
	                                                ]
	                                            }
	                                        }
	                                    }
	                                ]
	                            },
	                            "Binding": {
	                                "Primary": {
	                             "Groupings": [
	                                        {
	                                            "Projections": [
	                                                0
	                                            ]
	                                        }
	                                    ]
	                                },
	                                "DataReduction": {
	                                    "DataVolume": 3,
	                                    "Primary": {
	                                        "Window": {
	                                            "RestartTokens": [
	                                                [
	                                                    f"{RT}"
	                                                ]
	                                            ]
	                                        }
	                                    }
	                                },
	                                "IncludeEmptyGroups": "true",
	                                "Version": 1
	                            },
	                            "ExecutionMetricsKind": 1
	                        }
	                    }
	                ]
	            },
	            "QueryId": ""
	        }
	    ],
	    "cancelQueries": [],
	    "modelId": 303809
	}

	return query_RT

#This is the dictionary structure for the agencies in the response; the key for the agency is 'G0' agency['G0']
#agencies = data['results'][0]['result']['data']['dsr']['DS'][0]['PH'][0]['DM0']

def find_key_in_structure(structure, target_key):
    """
    Searches recursively for a target_key in a nested structure that may contain
    both dictionaries and lists.
    
    :param structure: The structure to search in (can be a dictionary or a list).
    :param target_key: The key to search for.
    :return: True if the key is found, False otherwise.
    """
    if isinstance(structure, dict):  # If the current structure is a dictionary
        if target_key in structure:
            return True
        for value in structure.values():
            if find_key_in_structure(value, target_key):  # Recurse into values
                return True
                
    elif isinstance(structure, list):  # If the current structure is a list
        for item in structure:
            if find_key_in_structure(item, target_key):  # Recurse into items
                return True
                
    return False

def find_value_by_key(structure, target_key):
    """
    Searches recursively for a target_key in a nested structure (dictionaries and lists)
    and returns the value associated with the target key.
    
    :param structure: The structure to search in (can be a dictionary or a list).
    :param target_key: The key to search for.
    :return: The value associated with the target key if found, otherwise None.
    """
    if isinstance(structure, dict):  # If the current structure is a dictionary
        if target_key in structure:
            return structure[target_key]
        for value in structure.values():
            found_value = find_value_by_key(value, target_key)  # Recurse into values
            if found_value is not None:
                return found_value
                
    elif isinstance(structure, list):  # If the current structure is a list
        for item in structure:
            found_value = find_value_by_key(item, target_key)  # Recurse into items
            if found_value is not None:
                return found_value
                
    return None

#RT = data['results'][0]['result']['data']['dsr']['DS'][0]['RT'][0][0]

for ministry in ministries:
	data = requests.post(api_url, json=get_query(ministry), headers=headers).json()

	#Retrieve the list of agencies in dictionary form
	agencies = data['results'][0]['result']['data']['dsr']['DS'][0]['PH'][0]['DM0']
	for agency in agencies:
		print(f"{ministry} === {agency['G0']}")

	#Check if Restart Token exists in response data.
	if find_key_in_structure(data, 'RT'):
		value = find_value_by_key(data, 'RT') #Get the value of the Restart Token
		RT = value[0][0]
		data_after_RT = requests.post(api_url, json=get_query_RT(ministry, RT), headers=headers).json()
		#Retrieve agencies in dictionary form.
		agencies_after_RT = data_after_RT['results'][0]['result']['data']['dsr']['DS'][0]['PH'][0]['DM0']
		for agency in agencies_after_RT:
			print(f"{ministry} === {agency['G0']}")


def call_api_RT():
	value = find_value_by_key(data, 'RT')
		RT = value[0][0]
		data_after_RT = requests.post(api_url, json=get_query_RT(ministry, RT), headers=headers).json()
		#print(RT)
		#print(data_after_RT)
		agencies_after_RT = data_after_RT['results'][0]['result']['data']['dsr']['DS'][0]['PH'][0]['DM0']
		for agency in agencies_after_RT:
			print(f"{ministry} === {agency['G0']}")









