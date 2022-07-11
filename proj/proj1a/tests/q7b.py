test = {   'name': 'q7b',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> training_data.shape == (168931, 72)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> expected_ohe_cols = set(['x0_Other', 'x0_Shake', 'x0_Shingle/Asphalt' ,'x0_Slate', 'x0_Tar&Gravel', 'x0_Tile'])\n"
                                               '>>> expected_ohe_cols.issubset(set(training_data.columns)) == True\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
