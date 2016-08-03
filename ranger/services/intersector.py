# todo: try numba (JIT compiliation for python)

import numpy as np
from services import storage


def get_intersections_v1(data):
    if len(data) != 2:
        raise NotImplemented("")
    # todo: validate input
    data_array = np.array(xrange(data[0],data[1]+1))

    stor = storage.get_storage()
    total_intersections = 0
    intersection_counts = {}
    ret = []
    for k in stor:
        ranges = stor[k]['ranges']
        range_arrays = stor[k]['arrays']
        for i, r_array in enumerate(range_arrays):
            r = ranges[i]
            inter = np.intersect1d(data_array, r_array)
            if len(inter) > 0:
                if intersection_counts.get(tuple(r)):
                    raise NotImplemented("Need to handle duplicate range counts")
                range_key = tuple(r)
                intersection_count = len(inter)
                intersection_counts[range_key] = {
                    'count': intersection_count,
                    'intersection': inter
                }
                total_intersections = intersection_count

        key_data = {
            "identifier": k,
            "ranges": intersection_counts.keys(),
            "intersection": total_intersections
        }
        ret.append(key_data)
    return ret

LATEST = 'v1'
funcs = {
    'v1': get_intersections_v1
}

def get_intersections(data, version=None):
    if not version:
        version = LATEST
    return funcs[version](data)

