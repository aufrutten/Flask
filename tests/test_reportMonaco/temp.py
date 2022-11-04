import importlib
class TestCompareStartEndTime:

    def test_with_atypical_argument(self):
        with pytest.raises(TypeError):
            report.compare_start_end_time('123')

    def test_with_typical_argument(self):
        argument = {'SVF': {'start': {'date': '2018-05-24', 'time': '12:02:58.917'},
                            'end': {'date': '2018-05-24', 'time': '12:04:03.332'},
                            'name': 'Sebastian Vettel',
                            'car': 'FERRARI'
                            }
                    }

        result_zero = {'SVF': {'start': {'date': '2018-05-24', 'time': '12:02:58.917'},
                               'end': {'date': '2018-05-24', 'time': '12:04:03.332'},
                               'name': 'Sebastian Vettel',
                               'car': 'FERRARI',
                               'result': '0:01:04.415000'
                               }
                       }

        result_one = {'0:01:04.415000': 'SVF'}

        result_of_function = report.compare_start_end_time(argument)
        assert result_of_function[0] == result_zero
        assert result_of_function[1] == result_one


class TestMergeDicts:

    # def test_with_atypical_argument(self):
    #     with pytest.raises(TypeError):
    #         report.merge_dicts('123', 123, [])

    def test_with_two_dicts(self):
        first_dict = {'TEST': {'name': 'ihor',
                               'age': 90,
                               }
                      }
        second_dict = {'TEST': {'family': 'Four',
                                'live': True}
                       }

        third_dict = {'TEST': {'sex': 'M',
                               'country': 'DE'}
                      }

        result = {'TEST': {'name': 'ihor',
                           'age': 90,
                           'family': 'Four',
                           'live': True,
                           'sex': 'M',
                           'country': 'DE'}
                  }

        assert report.merge_dicts(first_dict, second_dict, third_dict) == result