#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Research, Author, ResearchAuthors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

class Researches(Resource):
    def get(self):
        research_data = [r.to_dict(rules=("-research_authors","-updated_at", "-created_at",)) for r in Research.query]
        return research_data, 200
    
api.add_resource(Researches, "/research")

class ResearchById(Resource):
    def get(self, id):
        if research := db.session.get(Research, id):
            return research.to_dict(only=('id', "topic", 'page_count', 'authors')), 200
        return {"error": "Research paper not found"}, 404
    
    def delete(self, id):
        if research := db.session.get(Research, id):
            try:
                db.session.delete(research)
                db.session.commit()
                return {}, 204
            except Exception as e:
                db.session.rollback()
                return {"error" : str(e)}
        return {"error": "Research paper not found"}, 404
    
api.add_resource(ResearchById, "/research/<int:id>")

class Authors(Resource):
    def get(self):
        author_data = [a.to_dict() for a in Author.query]
        return author_data, 200
    
api.add_resource(Authors, "/authors")

class AuthorById(Resource):
    def patch(self, id):
        if author_by_id := db.session.get(Author, id):
            try:
                for k in request.get_json():
                    setattr(author_by_id, k, request.get_json()[k])
                db.session.add(author_by_id)
                db.session.commit()
                return author_by_id.to_dict(), 200
            except Exception as e:
                db.session.rollback()
                return {'error' : [str(e)]}
        return {"error" : "Author cannot be found"}
    
api.add_resource(AuthorById, "/author/<int:id>")

class ResearchAuthor(Resource):
    def post(self):
        try:
            data=request.json
            new_ra = ResearchAuthors(**data)
            db.session.add(new_ra)
            db.session.commit()
            return new_ra.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {"error" : [str(e)]}
        
api.add_resource(ResearchAuthor, '/research_author')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
