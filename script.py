import pandas as pd
import requests
import json

RT = []
api_url = "https://wabi-south-africa-north-a-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true"

def get_query(RT):
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
                    "Name": "2",
                    "Entity": "National Projects",
                    "Type": 0
                  },
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
                          "Source": "2"
                        }
                      },
                      "Property": "PROJECT NAME"
                    },
                    "Name": "2022 Agric Project.PROJECT NAME"
                  },
                  {
                    "Column": {
                      "Expression": {
                        "SourceRef": {
                          "Source": "2"
                        }
                      },
                      "Property": "CODE"
                    },
                    "Name": "2022 Agric Project.CODE"
                  },
                  {
                    "Aggregation": {
                      "Expression": {
                        "Column": {
                          "Expression": {
                            "SourceRef": {
                              "Source": "2"
                            }
                          },
                          "Property": "AMOUNT"
                        }
                      },
                      "Function": 0
                    },
                    "Name": "Sum(2022 Agric Project.AMOUNT)"
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
                                  "Source": "m"
                                }
                              },
                              "Property": "MDA -Final List with 2021 updates"
                            }
                          }
                        ],
                        "Values": [
                          [
                            {
                              "Literal": {
                                "Value": "'FEDERAL MEDICAL CENTRE - ABUJA'"
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
                                "Value": "'FEDERAL MINISTRY OF HEALTH AND SOCIAL WELFARE'"
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
                  }
                ],
                "OrderBy": [
                  {
                    "Direction": 2,
                    "Expression": {
                      "Column": {
                        "Expression": {
                          "SourceRef": {
                            "Source": "2"
                          }
                        },
                        "Property": "PROJECT NAME"
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
                        0,
                        1,
                        2
                      ],
                      "Subtotal": 1
                    }
                  ]
                },
                "DataReduction": {
                  "DataVolume": 2,
                  "Primary": {
                    "Window": {
                      "Count": 500
                    }
                  }
                },
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
            "VisualId": "e7555fa811c380789d46"
          }
        ]
      }
    }
  ],
  "cancelQueries": [],
  "modelId": 303809
}

    return query


headers = {"X-PowerBI-ResourceKey": "7f89c321-25c7-45a0-b48e-dec06704c3b7"}


def find_key_recursively(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            yield obj[key]

        for v in obj.values():
            yield from find_key_recursively(v, key)
    elif isinstance(obj, list):
        for v in obj:
            yield from find_key_recursively(v, key)


all_data = []
while True:
    data = requests.post(api_url, json=get_query(RT), headers=headers).json()
    proj_name = data['results'][0]['result']['data']['dsr']['DS'][0]['ValueDicts']['D0']
    proj_code = data['results'][0]['result']['data']['dsr']['DS'][0]['ValueDicts']['D1']
    appr_amnt = data['results'][0]['result']['data']['dsr']['DS'][0]['PH'][1]['DM1']
    print(appr_amnt)
    amnt_appr = []
    for appr in appr_amnt:
    	if len(appr['C']) > 2:
    		amnt_appr.append(appr['C'][2])
    print(amnt_appr)

    print(proj_code, '\n')
    print(proj_name, '\n')


    print(f"The amount of projects found ==> {len(proj_code)}, {len(proj_name)}, {len(amnt_appr)}")
    #print(data)
    break

    #print(RT)

#df = pd.DataFrame(all_data, columns=["Name", "Count"])
#print(df)