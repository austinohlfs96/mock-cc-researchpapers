from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, func
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Add models here

class Research(db.Model, SerializerMixin):
    __tablename__ = "researches"
    
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    year = db.Column(db.Integer)
    page_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    
    research_authors = db.relationship("ResearchAuthors", back_populates="research", cascade="all, delete-orphan")
    
    authors = association_proxy("research_authors", "author")
    
    serialize_rules = ("-authors.researches", "-research_authors.research")
    
    @validates('year')
    def validate_year(self, _, value):
        if not isinstance(value, int):
            raise ValueError("Year must be a number")
        elif not len(str(value)) is 4:
            raise ValueError("Year must be 4 digits")
        else:
            return value
    
    def __repr__(self):
        return f"<Researcher {self.id}: {self.topic}>"
    

class Author(db.Model, SerializerMixin):
    __tablename__ = "authors"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    field_of_study = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    
    #relationship
    research_authors = db.relationship("ResearchAuthors", back_populates="author", cascade="all, delete-orphan")
    
    researches = association_proxy("research_authors", "research")
    
    serialize_only = ("id", "name", "field_of_study")
    
    @validates('field_of_study')
    def validate_fos(self, _, value):
        if not value in ["AI", "Robotics", "Machine Learning", "Vision", "Cybersecurity"]:
            raise ValueError("F.O.S. must be different")
        return value
    
    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"
    
class ResearchAuthors(db.Model, SerializerMixin):
    __tablename__ = "research_authors"
    
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    research_id = db.Column(db.Integer, db.ForeignKey("researches.id"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    
    #relationships
    research = db.relationship('Research', back_populates="research_authors")
    author = db.relationship('Author', back_populates="research_authors")
    
    #serilzer rules
    serialize_only = ("author",)
    
    def __repr__(self):
        return f"<ResearcherAuthor {self.id}: {self.name}>"