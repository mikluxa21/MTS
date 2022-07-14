import flatdict

class Normal():
    def For_save(self, dict_from_site: dict):
        normal_data = []
        flat_dict = flatdict.FlatDict(dict_from_site, delimiter="->")
        for one_dict in flat_dict:
                normal_data.append(one_dict.split("->") + [flat_dict[one_dict]] if type(flat_dict[one_dict]) != list else one_dict.split("->") + flat_dict[one_dict])
        return normal_data