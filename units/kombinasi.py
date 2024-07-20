from typing import List

def kombinasi_satu(dd: List[bool], hasil: bool, bagian: int):
    if dd[0] and not any(dd[1:]) and bagian == 1:
        return hasil
    elif dd[1] and not any(dd[:1] + dd[2:]) and bagian == 2:
        return hasil
    elif dd[2] and not any(dd[:2] + dd[3:]) and bagian == 3:
        return hasil
    elif dd[3] and not any(dd[:3]) and bagian == 4:
        return hasil
    else:
        return None
    
def kombinasi_dua(dd: List[bool], hasil: bool, bagian: int):
    if all(dd[:2]) and not any(dd[2:]) and bagian == 1:
        return hasil
    elif all([dd[0], dd[2]]) and not any([dd[1], dd[3]]) and bagian == 2:
        return hasil
    elif all([dd[0], dd[3]]) and not any(dd[1:3]) and bagian == 3:
        return hasil
    elif all(dd[1:3]) and not any([dd[0], dd[3]]) and bagian == 4:
        return hasil
    elif all([dd[1],dd[3]]) and not any([dd[0], dd[2]]) and bagian == 5:
        return hasil
    elif all(dd[2:]) and not any(dd[:2]) and bagian == 6:
        return hasil
    else:
        return None
    
def kombinasi_tiga(dd: List[bool], hasil: bool, bagian: int):
    if all(dd[:3]) and not any(dd[3:]) and bagian == 1:
        return hasil
    elif all(dd[:2] + dd[3:]) and not any(dd[2:3]) and bagian == 2:
        return hasil
    elif all(dd[:1] + dd[2:]) and not any(dd[1:2]) and bagian == 3:
        return hasil
    elif all(dd[1:]) and not any(dd[:1]) and bagian == 4:
        return hasil
    else:
        return None
    
    