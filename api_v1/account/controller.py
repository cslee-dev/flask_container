from flask_restful import Resource


class Index(Resource):
    @classmethod
    def get(cls):
        return 'account get'

    @classmethod
    def post(cls):
        return 'account post'

    @classmethod
    def delete(cls):
        return 'account delete'

    @classmethod
    def put(cls):
        return 'account put'
