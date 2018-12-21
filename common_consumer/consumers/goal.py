from common_consumer.schemas.goal import GoalInputSchema, GoalOutputSchema


class GoalConsumer:

    @staticmethod
    def create(goal_input: 'GoalInputSchema') -> GoalOutputSchema:
        return goal_input
