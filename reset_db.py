# to be run when database structure changes
from app import db
import db.user
db.drop_all()
db.create_all()
# something like this


