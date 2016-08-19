from cvrminer.cvrfile import CvrFile
from cvrminer.virksomhed import Virksomhed
filename = '/home/folzd/CVR/cvr-permanent.json'  # or whatever
data = next(CvrFile(filename))
virksomhed = Virksomhed(data)
cvr_file = CvrFile(filename)
cvr_file.write_virksomhed_features_file()   # and wait