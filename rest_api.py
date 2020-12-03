from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class TasksModel(db.Model):
	__tablename__ = "tasks"
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime)
	name = db.Column(db.String(50))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	success = db.Column(db.Boolean)

db.create_all()

next_id = TasksModel.query.count()

task_fields = {
	'id': fields.Integer,
	'created_at': fields.DateTime,
	'name': fields.String,
	'start_date': fields.DateTime,
	'end_date': fields.DateTime,
	'success': fields.Boolean
}

task_create = reqparse.RequestParser()
task_create.add_argument("name", type=str, help="Task name is required", required=True)

#route: /create_task
class Create_Task(Resource):
	@marshal_with(task_fields)
	def post(self):
		global next_id
		args = task_create.parse_args()
		task = TasksModel(id=next_id, created_at=datetime.datetime.now(), name=args['name'])
		db.session.add(task)
		db.session.commit()
		next_id += 1
		return task

#route: /tasks
class Tasks(Resource): 
	@marshal_with(task_fields)
	def get(self):
		result = TasksModel.query.filter_by(success=None).all()
		return result

#route: /task/<task_id>
class Task(Resource):
	@marshal_with(task_fields)
	def put(self, task_id):
		result = TasksModel.query.filter_by(id=task_id).first()
		if not result:
			abort(404, message="Task does not exist")
		result.start_date = datetime.datetime.now()
		db.session.add(result)
		db.session.commit()
		return result

	@marshal_with(task_fields)
	def patch(self, task_id):
		result = TasksModel.query.filter_by(id=task_id).first()
		if not result:
			abort(404, message="Task does not exist")
		result.end_date = datetime.datetime.now()
		db.session.add(result)
		db.session.commit()
		return result


api.add_resource(Create_Task, "/create_task/")
api.add_resource(Tasks, "/tasks/")
api.add_resource(Task, "/task/<int:task_id>")


if __name__ == "__main__":
	app.run(debug=True);