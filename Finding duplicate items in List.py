from collections import Counter

def find_duplicates(patient_ids):
    ids_count=Counter(patient_ids)

    duplicates=[item for item,count in ids_count.items() if count>1]

    if duplicates:
        return duplicates
    else:
        return "No duplicates"





patient_ids= [
    1185, 1279, 1181, 638, 642, 1426, 1976, 4904, 1111, 770, 64, 1232, 707,
    1096, 3378, 1837, 3388, 5480, 92, 2381, 594, 2086, 4648, 768, 1510, 885,
    152, 6150, 6292, 1403, 622, 3384, 2174, 5233, 2159, 4244, 6083, 6418,
    1195, 604, 1970, 1174, 942, 434
]

print(find_duplicates(patient_ids))




