from collections import defaultdict

def dot_split_sections(cfg, default=None):
    """ Splits a configparser dict into dot-separated sections"""
    cfg_section_dict = cfg._sections
    new_dict = defaultdict(lambda: default)
    for full_section in cfg_section_dict.keys():
        split_section = full_section.split('.')
        cur_dict = new_dict
        for subsection in split_section:
            if subsection not in cur_dict:
                cur_dict[subsection] = defaultdict(lambda:default)
            cur_dict = cur_dict[subsection]
        cur_dict.update(
            defaultdict(lambda: default, cfg_section_dict[full_section])
        )
    return new_dict
