from gwa_framework.schemas.base import BaseSchema
from schematics.types import StringType


class GoalInputSchema(BaseSchema):
    goal_id = StringType(required=False, serialized_name='goalId')
    description = StringType(required=True, serialized_name='description', max_length=100, min_length=0)


class GoalOutputSchema(BaseSchema):

    goal_id = StringType(required=True, serialized_name='goalId')
    description = StringType(required=True, serialized_name='description')

    def __init__(self, **kwargs):
        super(GoalOutputSchema, self).__init__(**kwargs)
