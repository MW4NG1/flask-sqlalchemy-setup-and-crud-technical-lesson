from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Initialize MetaData to manage schema constructs and naming conventions
metadata = MetaData()

# Create the Flask-SQLAlchemy extension instance using our metadata
db = SQLAlchemy(metadata=metadata)

# Define the Pet model class by inheriting from db.Model
class Pet(db.Model):
    # Specify the name of the database table
    __tablename__ = 'pets'

    # Define columns, data types, and constraints for the table
    id = db.Column(db.Integer, primary_key=True)          
    name = db.Column(db.String(50))                      
    species = db.Column(db.String)                      

    # Define a custom string representation for easy debugging and shell output
    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
