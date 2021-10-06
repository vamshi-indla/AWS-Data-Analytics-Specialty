create external schema users_data
from data catalog
database 'users'
iam_role 'arn:aws:iam::605645534020:role/SpectrumRole'
create external database if not exists;